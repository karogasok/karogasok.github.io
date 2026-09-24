"""Contracts for theme placement, for any vector and any calibration."""

from __future__ import annotations

import numpy as np
from hypothesis import given
from hypothesis import strategies as st

from karogasok_temak.placement import Calibration, place, unit

DIM, THEMES = 6, 4
floats = st.floats(-3, 3, allow_nan=False, allow_infinity=False)
vectors = st.lists(floats, min_size=DIM, max_size=DIM).map(np.array)


@st.composite
def calibrations(draw: st.DrawFn) -> Calibration:
    rows = np.array([draw(vectors) for _ in range(THEMES)])
    if not np.all(np.linalg.norm(rows, axis=1) > 0):
        rows = np.eye(THEMES, DIM)
    return Calibration(
        mean=draw(vectors) * 0.1,
        theme_keys=tuple(f"t{i}" for i in range(THEMES)),
        vectors=unit(rows),
        seed_counts=tuple(draw(st.integers(3, 8)) for _ in range(THEMES)),
        tau={"long": draw(st.floats(-0.5, 0.9)), "short": draw(st.floats(-0.5, 0.9))},
        g={3: 0.55, 5: 0.6, 8: 0.65},
        delta=draw(st.floats(0.0, 0.3)),
    )


@given(vectors, calibrations(), st.sampled_from(["long", "short"]))
def test_placement_is_well_formed(v: np.ndarray, cal: Calibration, klass: str) -> None:
    p = place(v, klass, cal)
    assert len(p.themes) <= cal.cap
    assert len(set(p.themes)) == len(p.themes)
    assert set(p.themes) <= set(cal.theme_keys)
    assert list(p.scores) == sorted(p.scores, reverse=True)
    assert (p.role == "none") == (not p.themes)


@given(vectors, calibrations(), st.sampled_from(["long", "short"]))
def test_placement_is_deterministic(
    v: np.ndarray, cal: Calibration, klass: str
) -> None:
    assert place(v, klass, cal) == place(v, klass, cal)


@given(vectors, calibrations(), st.integers(0, THEMES - 1))
def test_a_seed_always_carries_its_theme(
    v: np.ndarray, cal: Calibration, i: int
) -> None:
    p = place(v, "long", cal, seed_of=[cal.theme_keys[i]])
    assert cal.theme_keys[i] in p.themes
    assert p.role == "seed"


@given(vectors, calibrations())
def test_every_placed_theme_clears_its_threshold(
    v: np.ndarray, cal: Calibration
) -> None:
    p = place(v, "long", cal)
    for key, score in zip(p.themes, p.scores, strict=True):
        i = cal.theme_keys.index(key)
        assert score >= round(cal.threshold(i, "long"), 4) - 1e-4
        assert p.best - score <= cal.delta + 1e-4
