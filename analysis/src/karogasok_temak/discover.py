"""Find candidate new themes among the writings no theme fits.

The curated list only grows by hand, but a hand needs something to look at. This
module groups the author's own writings that got no theme, and describes each
group with evidence the author can check rather than trust:

* the group's members, and the three most central as proposed seeds;
* keyness terms of the group against the rest of the corpus, with how many
  members use each;
* the author's own old labels that are over-represented in the group, with the
  counts behind the ratio;
* the nearest existing themes, in case the group is a missing seed rather than
  a missing theme;
* for each proposed seed, one sentence quoted **verbatim** from it, so that
  checking the proposal is a string match, not a reread.

Nothing here names a theme. A name is the author's call.

Clustering is agglomerative with average linkage on cosine distance, which is
deterministic: the same vectors give the same groups. The default cut is
measured, not chosen — see :func:`cohesion_threshold`.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

import numpy as np

from karogasok_temak.placement import unit

#: Fewest members a group needs to be proposed: a theme needs three seeds.
MIN_SIZE = 3

#: Sentences longer than this are not offered as evidence: a quote should be
#: checkable at a glance.
MAX_QUOTE_CHARS = 400

_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def cohesion_threshold(groups: Sequence[np.ndarray]) -> float:
    """The cosine distance at which a new group hangs together like an old one.

    For each group of unit vectors (the seeds of one existing theme), every
    pairwise similarity is taken; the threshold is one minus their median. A
    proposed group whose average pairwise distance stays under it is at least as
    coherent as a typical existing theme's seeds.

    Args:
        groups: One ``(members, dim)`` array of unit vectors per theme.

    Returns:
        A cosine distance in ``[0, 2]``.

    Raises:
        ValueError: If no group has two members.

    Example:
        >>> a = np.array([[1.0, 0.0], [0.8, 0.6]])
        >>> round(cohesion_threshold([a]), 3)
        0.2
    """
    sims: list[float] = []
    for group in groups:
        if len(group) < 2:
            continue
        s = group @ group.T
        sims.extend(s[np.triu_indices(len(group), 1)].tolist())
    if not sims:
        msg = "need at least one group with two members"
        raise ValueError(msg)
    return float(1.0 - np.median(sims))


def clusters(
    vectors: np.ndarray, threshold: float, *, min_size: int = MIN_SIZE
) -> list[list[int]]:
    """Group rows by average-linkage cosine distance, keeping groups big enough.

    Args:
        vectors: ``(n, dim)`` rows, n ≥ 2.
        threshold: Cut distance; groups merge while their average distance is
            below it.
        min_size: Smallest group returned. Defaults to :data:`MIN_SIZE`.

    Returns:
        Row indices per group, each sorted; groups by size, largest first, ties
        by their first index. Rows in smaller groups are left out.

    Raises:
        ValueError: If there are fewer than two rows.

    Example:
        >>> x = np.array([[1, 0], [0.99, 0.1], [0.98, 0.2], [0, 1], [0.1, 0.99]])
        >>> clusters(x, 0.1)
        [[0, 1, 2]]
        >>> clusters(x, 0.1, min_size=2)
        [[0, 1, 2], [3, 4]]
    """
    if len(vectors) < 2:
        msg = f"need at least two writings to cluster, got {len(vectors)}"
        raise ValueError(msg)
    from sklearn.cluster import AgglomerativeClustering

    labels = AgglomerativeClustering(
        n_clusters=None,
        metric="cosine",
        linkage="average",
        distance_threshold=threshold,
    ).fit_predict(np.asarray(vectors, dtype=float))
    groups: dict[int, list[int]] = {}
    for row, label in enumerate(labels):
        groups.setdefault(int(label), []).append(row)
    kept = [sorted(g) for g in groups.values() if len(g) >= min_size]
    return sorted(kept, key=lambda g: (-len(g), g[0]))


def central(vectors: np.ndarray, members: Sequence[int], n: int = 3) -> list[int]:
    """The ``n`` members closest to the group's centroid, closest first.

    Example:
        >>> x = np.array([[1.0, 0.0], [0.7, 0.7], [0.0, 1.0]])
        >>> central(x, [0, 1, 2], n=1)
        [1]
    """
    rows = unit(np.asarray(vectors, dtype=float)[list(members)])
    centre = unit(rows.mean(axis=0)[None, :])[0]
    sims = rows @ centre
    order = sorted(range(len(members)), key=lambda i: (-sims[i], members[i]))
    return [members[i] for i in order[:n]]


@dataclass(frozen=True)
class LabelCount:
    """An author label's share in a group against its share overall.

    Attributes:
        label: The label, casefolded.
        in_group: Group members carrying it.
        group_size: Members in the group.
        overall: Writings carrying it in the whole pool.
        pool_size: Writings in the whole pool.
        ratio: ``(in_group / group_size) / (overall / pool_size)``.
    """

    label: str
    in_group: int
    group_size: int
    overall: int
    pool_size: int
    ratio: float


def over_represented(
    group: Sequence[Iterable[str]],
    pool: Sequence[Iterable[str]],
    *,
    min_count: int = 2,
) -> list[LabelCount]:
    """Author labels the group carries more often than the pool does.

    Args:
        group: Each member's labels.
        pool: Each writing's labels, the group included.
        min_count: Fewest members that must carry a label. Defaults to 2 — one
            member is an anecdote.

    Returns:
        Labels with ratio above 1, strongest first (ties: more members, then
        alphabetical).

    Raises:
        ValueError: If the pool is empty.

    Example:
        >>> g = [["Kognitív"], ["kognitív", "agy"], ["agy"]]
        >>> p = g + [["nyelv"]] * 7
        >>> [(c.label, c.in_group, c.overall) for c in over_represented(g, p)]
        [('agy', 2, 2), ('kognitív', 2, 2)]
    """
    if not pool:
        msg = "the pool of writings is empty"
        raise ValueError(msg)

    def doc_freq(docs: Sequence[Iterable[str]]) -> Counter[str]:
        c: Counter[str] = Counter()
        for labels in docs:
            c.update({label.casefold() for label in labels})
        return c

    in_group, overall = doc_freq(group), doc_freq(pool)
    n, big_n = len(group), len(pool)
    out = [
        LabelCount(
            label, k, n, overall[label], big_n, (k / n) / (overall[label] / big_n)
        )
        for label, k in in_group.items()
        if k >= min_count
    ]
    out = [c for c in out if c.ratio > 1]
    return sorted(out, key=lambda c: (-c.ratio, -c.in_group, c.label))


def evidence_sentence(text: str, terms: Sequence[str]) -> str | None:
    """One sentence from ``text``, verbatim, that uses the most of ``terms``.

    Terms are lemmas; Hungarian inflects by suffixing, so a term counts as used
    when a word in the sentence starts with it (case-insensitively). Sentences
    over :data:`MAX_QUOTE_CHARS` are skipped. The result is always a substring
    of ``text``, so a reader can find it with a search.

    Returns:
        The sentence, or ``None`` if no short sentence uses any term.

    Example:
        >>> t = "Bevezető mondat. A metaforák és az agy kapcsolata izgalmas! Vége."
        >>> evidence_sentence(t, ["metafora", "agy"])
        'A metaforák és az agy kapcsolata izgalmas!'
        >>> evidence_sentence(t, ["kvantum"]) is None
        True
    """
    best: tuple[int, str] | None = None
    for raw in _SENTENCE_END.split(text):
        sentence = raw.strip()
        if not sentence or len(sentence) > MAX_QUOTE_CHARS:
            continue
        words = [w.casefold() for w in re.findall(r"\w+", sentence)]
        used = sum(
            1 for term in terms if any(w.startswith(term.casefold()) for w in words)
        )
        if used and (best is None or used > best[0]):
            best = (used, sentence)
    return best[1] if best else None
