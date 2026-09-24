"""Judging a theme placement against the author's own historical labels.

Most of this corpus was labelled by its author years before any model touched
it: Blogspot and WordPress labels on the archive pages, blog.hu tags on the
Kereső Világ rows. Those labels are the yardstick. A placement is good to the
extent that writings it puts together are writings he put together.

The metric is **extended BCubed** (Amigó, Gonzalo, Artiles & Verdejo, 2009),
which handles the case both sides have here: a writing may carry several themes
and several labels. For every writing it asks two questions —

* of the writings that share a theme with it, how many also share a label
  (precision), and
* of the writings that share a label with it, how many also share a theme
  (recall),

weighting by how many themes and labels a pair shares. A writing with no theme
is treated as a cluster of its own, so leaving it out costs recall rather than
vanishing from the score.

Only writings that carry at least one cleaned label are scored. Every function
returns the counts it was computed from, not just a number.
"""

from __future__ import annotations

import hashlib
from collections import Counter
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import numpy as np

#: Bootstrap resamples for confidence intervals.
N_BOOTSTRAP = 2000

#: Seed for every resampling in this module.
SEED = 42


@dataclass(frozen=True)
class LabelRules:
    """How raw labels are cleaned before they are used as the yardstick.

    Attributes:
        genres: Labels that name a kind of post rather than a subject.
        merges: Variant spelling mapped to its canonical form.
        min_df: A label on fewer writings than this is dropped.
    """

    genres: frozenset[str]
    merges: Mapping[str, str]
    min_df: int


def load_label_rules(path: Path) -> LabelRules:
    """Read the committed clean-up rules.

    Args:
        path: ``analysis/eval/cimke_normalizalas.yaml``.

    Returns:
        The rules, casefolded.
    """
    import yaml

    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    return LabelRules(
        genres=frozenset(str(g).casefold() for g in raw.get("mufaj", [])),
        merges={
            str(k).casefold(): str(v).casefold()
            for k, v in (raw.get("osszevonas") or {}).items()
        },
        min_df=int(raw.get("min_df", 2)),
    )


def clean_labels(
    raw: Mapping[str, Iterable[str]], rules: LabelRules
) -> dict[str, frozenset[str]]:
    """Apply the clean-up rules to one source's labels.

    Casefold, merge variants, drop genre labels, then drop any label used on
    fewer than ``rules.min_df`` writings of this source. A writing left with no
    label is dropped too: there is nothing to judge it against.

    Args:
        raw: Writing key mapped to its labels as written.
        rules: The committed rules.

    Returns:
        Writing key mapped to its cleaned, non-empty label set.

    Example:
        >>> rules = LabelRules(frozenset({"ajánló"}), {"nlp": "nyelvtechnológia"}, 2)
        >>> out = clean_labels(
        ...     {"a": ["NLP", "ajánló"], "b": ["nyelvtechnológia"], "c": ["egyszeri"]},
        ...     rules,
        ... )
        >>> sorted(out), sorted(out["a"])
        (['a', 'b'], ['nyelvtechnológia'])
    """
    staged: dict[str, set[str]] = {}
    for key, labels in raw.items():
        cleaned = set()
        for label in labels:
            folded = label.strip().casefold()
            folded = rules.merges.get(folded, folded)
            if folded and folded not in rules.genres:
                cleaned.add(folded)
        staged[key] = cleaned
    df = Counter(label for labels in staged.values() for label in labels)
    out: dict[str, frozenset[str]] = {}
    for key, labels in staged.items():
        kept = frozenset(label for label in labels if df[label] >= rules.min_df)
        if kept:
            out[key] = kept
    return out


def split_of(key: str) -> str:
    """Assign a writing to the tuning or the held-out half, permanently.

    The half is a function of the key alone, so it never depends on the order
    rows come in, and a row cannot drift between halves as the corpus grows.

    Args:
        key: The writing's URL or page path.

    Returns:
        ``"dev"`` or ``"test"``.

    Example:
        >>> split_of("https://kereses.blog.hu/x") in {"dev", "test"}
        True
        >>> split_of("a") == split_of("a")
        True
    """
    digest = hashlib.sha1(key.encode("utf-8")).digest()
    return "test" if digest[-1] % 2 else "dev"


@dataclass(frozen=True)
class BCubed:
    """Extended BCubed scores and what they were computed from.

    Attributes:
        precision: Mean per-writing BCubed precision.
        recall: Mean per-writing BCubed recall.
        f: Harmonic mean of the two.
        n: Writings scored.
        unplaced: Scored writings with no theme, counted as singletons.
    """

    precision: float
    recall: float
    f: float
    n: int
    unplaced: int


def _membership(
    items: Sequence[str], assignment: Mapping[str, Iterable[str]]
) -> tuple[np.ndarray, int]:
    """Binary item×cluster matrix; an unassigned item gets its own column."""
    clusters: dict[str, int] = {}
    rows: list[list[int]] = []
    unplaced = 0
    for item in items:
        assigned = list(dict.fromkeys(assignment.get(item, ())))
        if not assigned:
            unplaced += 1
            assigned = [f"\0singleton:{item}"]
        rows.append([clusters.setdefault(c, len(clusters)) for c in assigned])
    matrix = np.zeros((len(items), max(len(clusters), 1)), dtype=np.float64)
    for i, cols in enumerate(rows):
        matrix[i, cols] = 1.0
    return matrix, unplaced


def _bcubed_matrices(pred: np.ndarray, gold: np.ndarray) -> tuple[float, float]:
    """Precision and recall from item×cluster and item×label matrices."""
    shared_pred = pred @ pred.T
    shared_gold = gold @ gold.T
    agree = np.minimum(shared_pred, shared_gold)
    with np.errstate(divide="ignore", invalid="ignore"):
        prec_pairs = np.where(shared_pred > 0, agree / shared_pred, np.nan)
        rec_pairs = np.where(shared_gold > 0, agree / shared_gold, np.nan)
    precision = float(np.mean(np.nanmean(prec_pairs, axis=1)))
    recall = float(np.mean(np.nanmean(rec_pairs, axis=1)))
    return precision, recall


def _f(precision: float, recall: float) -> float:
    return (
        0.0
        if precision + recall == 0
        else 2 * precision * recall / (precision + recall)
    )


def bcubed(
    pred: Mapping[str, Iterable[str]],
    gold: Mapping[str, frozenset[str]],
    items: Sequence[str] | None = None,
) -> BCubed:
    """Score a placement against the gold labels.

    Args:
        pred: Writing key mapped to its themes. A missing or empty entry means
            no theme, scored as a singleton.
        gold: Writing key mapped to its cleaned labels.
        items: Which writings to score. Defaults to every writing with gold
            labels. Writings without gold labels are always skipped.

    Returns:
        The scores and their counts.

    Raises:
        ValueError: If there is nothing to score.

    Example:
        Two writings share a theme but not a label; the third stands apart.

        >>> gold = {"a": frozenset({"p"}), "b": frozenset({"q"}),
        ...         "c": frozenset({"q"})}
        >>> s = bcubed({"a": ["X"], "b": ["X"], "c": ["Y"]}, gold)
        >>> round(s.precision, 4), round(s.recall, 4), s.n
        (0.6667, 0.6667, 3)

        A placement identical to the labels scores perfectly:

        >>> g = {"a": frozenset({"p"}), "b": frozenset({"p", "q"})}
        >>> bcubed({k: sorted(v) for k, v in g.items()}, g).f
        1.0
    """
    keys = [k for k in (items if items is not None else gold) if k in gold]
    if not keys:
        msg = "no writing with gold labels to score"
        raise ValueError(msg)
    pred_m, unplaced = _membership(keys, pred)
    gold_m, _ = _membership(keys, gold)
    precision, recall = _bcubed_matrices(pred_m, gold_m)
    return BCubed(precision, recall, _f(precision, recall), len(keys), unplaced)


@dataclass(frozen=True)
class Delta:
    """Difference in BCubed F between two placements, with its uncertainty.

    Attributes:
        observed: F(b) − F(a) on the full item set.
        low: 2.5th percentile of the bootstrapped difference.
        high: 97.5th percentile.
        n: Writings scored.
        resamples: Bootstrap resamples drawn.
    """

    observed: float
    low: float
    high: float
    n: int
    resamples: int


def paired_bootstrap(
    pred_a: Mapping[str, Iterable[str]],
    pred_b: Mapping[str, Iterable[str]],
    gold: Mapping[str, frozenset[str]],
    items: Sequence[str] | None = None,
    *,
    n: int = N_BOOTSTRAP,
    seed: int = SEED,
) -> Delta:
    """How much better placement ``b`` is than ``a``, and how sure we are.

    Both placements are scored on the *same* resampled writings each round, so
    the interval reflects the difference between them rather than the noise
    each would have on its own.

    Args:
        pred_a: The baseline placement.
        pred_b: The candidate placement.
        gold: Cleaned labels.
        items: Which writings to score. Defaults to all with gold labels.
        n: Resamples. Defaults to :data:`N_BOOTSTRAP`.
        seed: RNG seed. Defaults to :data:`SEED`.

    Returns:
        The observed difference and its 95% interval.
    """
    keys = [k for k in (items if items is not None else gold) if k in gold]
    a_m, _ = _membership(keys, pred_a)
    b_m, _ = _membership(keys, pred_b)
    g_m, _ = _membership(keys, gold)
    observed = _f(*_bcubed_matrices(b_m, g_m)) - _f(*_bcubed_matrices(a_m, g_m))
    rng = np.random.default_rng(seed)
    diffs = np.empty(n)
    for r in range(n):
        idx = rng.integers(0, len(keys), len(keys))
        diffs[r] = _f(*_bcubed_matrices(b_m[idx], g_m[idx])) - _f(
            *_bcubed_matrices(a_m[idx], g_m[idx])
        )
    low, high = np.percentile(diffs, [2.5, 97.5])
    return Delta(observed, float(low), float(high), len(keys), n)


def knn_agreement(
    vectors: np.ndarray,
    keys: Sequence[str],
    gold: Mapping[str, frozenset[str]],
    *,
    k: int = 5,
) -> tuple[float, int]:
    """Share of each writing's nearest neighbours that share one of its labels.

    A property of an embedding, not of a placement: it asks whether writings
    the author labelled alike end up near each other.

    Args:
        vectors: One row per key, in the same order.
        keys: Writing keys.
        gold: Cleaned labels; writings without any are skipped.
        k: Neighbours per writing. Defaults to 5.

    Returns:
        The mean share and the number of writings scored.

    Example:
        >>> v = np.array([[1.0, 0.0], [0.9, 0.1], [0.0, 1.0], [0.1, 0.9]])
        >>> g = {"a": frozenset({"x"}), "b": frozenset({"x"}),
        ...      "c": frozenset({"y"}), "d": frozenset({"y"})}
        >>> knn_agreement(v, ["a", "b", "c", "d"], g, k=1)
        (1.0, 4)
    """
    rows = [i for i, key in enumerate(keys) if key in gold]
    x = vectors[rows]
    x = x / np.linalg.norm(x, axis=1, keepdims=True)
    sims = x @ x.T
    np.fill_diagonal(sims, -np.inf)
    neighbours = np.argsort(-sims, axis=1)[:, :k]
    labels = [gold[keys[i]] for i in rows]
    shares = [
        np.mean([bool(labels[i] & labels[j]) for j in row])
        for i, row in enumerate(neighbours)
    ]
    return float(np.mean(shares)), len(rows)
