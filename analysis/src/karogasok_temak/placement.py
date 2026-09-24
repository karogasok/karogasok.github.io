"""Placing writings on the curated themes, by similarity to each theme's seeds.

This replaces the topic model's own placement. That path — project into five
UMAP dimensions, read HDBSCAN's soft cluster memberships, normalise — did not
follow similarity for new writings: the Jev post's nearest theme was
*Tudományfilozófia*, and it came out as *Logika és matematika*, which was not
even among its three nearest.

The method here is deliberately plain, so that every placement can be explained
by pointing at numbers:

1. **Centre.** Sentence-embedding spaces are anisotropic — everything is fairly
   similar to everything, so no threshold means much. Subtracting the mean of
   the author's own pages spreads them out. The mean is frozen at calibration,
   so adding a writing never moves the others.
2. **Theme vectors.** A theme is the normalised mean of its seeds' centred
   vectors. Seeds only: folding confident members back in would drift towards
   dense regions and leak into the evaluation.
3. **Threshold.** A writing belongs to a theme if its similarity clears
   ``τ(class) + g(k) − g(k_ref)``: a base level per length class (long pages,
   short blurbs), corrected by ``g``, the measured typical member similarity of
   a theme with ``k`` seeds — a centroid of more seeds sits closer to its
   members, so one global level would penalise the thinly seeded themes.
4. **Several themes.** The best theme that clears its threshold is primary; a
   second or third must clear its own threshold *and* score within ``δ`` of the
   best. At most three. A seed always carries its own theme. A writing that
   clears nothing gets no theme at all, which is the honest answer.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import numpy as np

#: Most themes a writing may carry.
CAP = 3

#: Seed count at which the seed-count correction is zero.
K_REF = 5


def unit(rows: np.ndarray) -> np.ndarray:
    """Normalise each row to length 1; a zero row stays zero.

    Example:
        >>> unit(np.array([[3.0, 4.0], [0.0, 0.0]])).tolist()
        [[0.6, 0.8], [0.0, 0.0]]
    """
    norms = np.linalg.norm(rows, axis=-1, keepdims=True)
    return np.divide(rows, norms, out=np.zeros_like(rows, dtype=float), where=norms > 0)


def theme_vectors(
    centred: Mapping[str, np.ndarray], seeds: Sequence[Sequence[str]]
) -> np.ndarray:
    """One unit vector per theme: the mean of its seeds' centred vectors.

    Args:
        centred: Writing key mapped to its centred vector.
        seeds: For each theme, its seed keys.

    Returns:
        A ``(themes, dim)`` array.

    Raises:
        KeyError: If a seed has no vector.

    Example:
        >>> v = {"a": np.array([1.0, 0.0]), "b": np.array([0.0, 1.0])}
        >>> theme_vectors(v, [["a"], ["a", "b"]]).round(3).tolist()
        [[1.0, 0.0], [0.707, 0.707]]
    """
    return unit(
        np.array([np.mean([centred[s] for s in group], axis=0) for group in seeds])
    )


def seed_count_curve(
    vectors: np.ndarray,
    groups: Sequence[Sequence[int]],
    ks: Sequence[int],
    *,
    reps: int = 20,
    seed: int = 42,
) -> dict[int, float]:
    """How similar a theme's members are to a centroid built from ``k`` seeds.

    For each group of rows (a cluster of writings) and each ``k``, ``k`` members
    are drawn as seeds, the rest are held out, and the median similarity of the
    held-out members to the seeds' centroid is recorded. The curve is the mean
    over groups and repetitions.

    Args:
        vectors: Unit, centred row vectors.
        groups: Row indices of each cluster. Groups too small for a ``k`` are
            skipped for that ``k``.
        ks: Seed counts to measure.
        reps: Draws per group and ``k``. Defaults to 20.
        seed: RNG seed. Defaults to 42.

    Returns:
        ``k`` mapped to typical member similarity.

    Example:
        >>> rng = np.random.default_rng(0)
        >>> x = unit(np.vstack([rng.normal(3, 1, (12, 4)), rng.normal(-3, 1, (12, 4))]))
        >>> g = seed_count_curve(x, [range(12), range(12, 24)], [1, 5])
        >>> g[5] > g[1]
        True
    """
    rng = np.random.default_rng(seed)
    curve: dict[int, float] = {}
    for k in ks:
        values = []
        for group in groups:
            members = np.array(list(group))
            if len(members) < k + 2:
                continue
            for _ in range(reps):
                picked = rng.choice(members, k, replace=False)
                rest = np.setdiff1d(members, picked)
                centre = unit(vectors[picked].mean(axis=0))
                values.append(float(np.median(vectors[rest] @ centre)))
        curve[k] = float(np.mean(values)) if values else float("nan")
    return curve


@dataclass(frozen=True)
class Calibration:
    """Everything placement needs, frozen so later writings do not move earlier ones.

    Attributes:
        mean: Subtracted from every raw vector before placement.
        theme_keys: Themes, in file order.
        vectors: Unit theme vectors, one row per theme.
        seed_counts: Seeds behind each theme vector.
        tau: Base threshold per length class, ``"long"`` and ``"short"``.
        g: Typical member similarity by seed count (see :func:`seed_count_curve`).
        delta: A secondary theme must score within this of the best.
        cap: Most themes per writing.
    """

    mean: np.ndarray
    theme_keys: tuple[str, ...]
    vectors: np.ndarray
    seed_counts: tuple[int, ...]
    tau: Mapping[str, float]
    g: Mapping[int, float]
    delta: float
    cap: int = CAP

    def threshold(self, theme: int, klass: str) -> float:
        """The similarity a writing of ``klass`` needs to join ``theme``."""
        k = self.seed_counts[theme]
        nearest = min(self.g, key=lambda x: abs(x - k))
        ref = min(self.g, key=lambda x: abs(x - K_REF))
        return self.tau[klass] + self.g[nearest] - self.g[ref]


@dataclass(frozen=True)
class Placement:
    """Where one writing landed, and why.

    Attributes:
        themes: Theme keys, strongest first; empty if none cleared.
        scores: Similarity to each of those themes.
        best: The best similarity over all themes, placed or not.
        role: ``"seed"``, ``"placed"`` or ``"none"``.
    """

    themes: tuple[str, ...]
    scores: tuple[float, ...]
    best: float
    role: str


def place(
    raw: np.ndarray,
    klass: str,
    cal: Calibration,
    *,
    seed_of: Sequence[str] = (),
) -> Placement:
    """Place one writing.

    Args:
        raw: Its embedding, as the encoder produced it.
        klass: ``"long"`` or ``"short"``.
        cal: The frozen calibration.
        seed_of: Themes this writing seeds; it always carries those.

    Returns:
        The placement.

    Example:
        >>> cal = Calibration(np.zeros(2), ("a", "b"), np.eye(2), (5, 5),
        ...                   {"long": 0.5, "short": 0.3}, {5: 0.6}, 0.1)
        >>> place(np.array([0.9, 0.2]), "long", cal).themes
        ('a',)
        >>> place(np.array([0.7, 0.65]), "long", cal).themes
        ('a', 'b')

        Just outside the margin (0.759 vs 0.651), the second theme is dropped:

        >>> place(np.array([0.7, 0.6]), "long", cal).themes
        ('a',)
        >>> place(np.array([-1.0, -1.0]), "long", cal).role
        'none'
        >>> place(np.array([-1.0, -1.0]), "long", cal, seed_of=["b"]).themes
        ('b',)
    """
    vector = unit((raw - cal.mean)[None, :])[0]
    sims = cal.vectors @ vector
    order = np.argsort(-sims, kind="stable")
    best = float(sims[order[0]])
    chosen: list[int] = [
        cal.theme_keys.index(t) for t in seed_of if t in cal.theme_keys
    ]
    for i in order:
        if len(chosen) >= cal.cap:
            break
        if i in chosen:
            continue
        clears = sims[i] >= cal.threshold(int(i), klass)
        if not chosen and clears:
            chosen.append(int(i))
        elif chosen and clears and best - sims[i] <= cal.delta:
            chosen.append(int(i))
    chosen.sort(key=lambda i: -sims[i])
    role = "seed" if seed_of else ("placed" if chosen else "none")
    return Placement(
        tuple(cal.theme_keys[i] for i in chosen),
        tuple(round(float(sims[i]), 4) for i in chosen),
        round(best, 4),
        role,
    )


class StaleCalibrationError(RuntimeError):
    """The theme list changed after the calibration was frozen."""


def load_calibration(path: Path, themes_path: Path) -> tuple[Calibration, dict]:
    """Read the frozen calibration, refusing it if the theme list has moved on.

    The calibration's theme vectors were built from particular seeds, and its
    thresholds tuned against them. Placing writings with a calibration frozen for
    a different theme list would produce confident nonsense, so the list's hash
    is checked first.

    Args:
        path: ``analysis/temalista_kalibracio.json``.
        themes_path: ``analysis/temalista.yaml``.

    Returns:
        The calibration and the full record, including the encoder spec.

    Raises:
        StaleCalibrationError: If ``temalista.yaml`` changed since freezing.
    """
    import hashlib
    import json

    record = json.loads(path.read_text(encoding="utf-8"))
    current = hashlib.sha256(themes_path.read_bytes()).hexdigest()
    if current != record["temalista_sha256"]:
        msg = (
            "temalista.yaml changed after the calibration was frozen; "
            "re-run scripts/place.py and scripts/freeze.py"
        )
        raise StaleCalibrationError(msg)
    cal = Calibration(
        mean=np.array(record["mean"]),
        theme_keys=tuple(record["theme_keys"]),
        vectors=np.array(record["vectors"]),
        seed_counts=tuple(record["seed_counts"]),
        tau=dict(record["tau"]),
        g={int(k): float(v) for k, v in record["g"].items()},
        delta=float(record["delta"]),
    )
    return cal, record
