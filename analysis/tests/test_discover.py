"""Contracts for theme discovery, on arbitrary vectors, labels and texts."""

from __future__ import annotations

import numpy as np
from hypothesis import given, settings
from hypothesis import strategies as st

from karogasok_temak.discover import (
    MAX_QUOTE_CHARS,
    central,
    clusters,
    cohesion_threshold,
    evidence_sentence,
    over_represented,
)
from karogasok_temak.placement import unit

DIM = 5
floats = st.floats(-3, 3, allow_nan=False, allow_infinity=False)
row = st.lists(floats, min_size=DIM, max_size=DIM).filter(
    lambda r: float(np.linalg.norm(r)) > 1e-3
)
matrices = st.lists(row, min_size=2, max_size=25).map(lambda r: unit(np.array(r)))


# The first call imports scikit-learn, which takes about a second.
@settings(deadline=None)
@given(x=matrices, threshold=st.floats(0.05, 1.95), min_size=st.integers(1, 5))
def test_clusters_are_disjoint_big_enough_and_deterministic(
    x: np.ndarray, threshold: float, min_size: int
) -> None:
    groups = clusters(x, threshold, min_size=min_size)
    flat = [i for g in groups for i in g]
    assert len(flat) == len(set(flat))
    assert all(0 <= i < len(x) for i in flat)
    assert all(len(g) >= min_size for g in groups)
    assert groups == clusters(x, threshold, min_size=min_size)


@given(x=matrices, n=st.integers(1, 5))
def test_central_picks_distinct_members(x: np.ndarray, n: int) -> None:
    members = list(range(len(x)))
    picked = central(x, members, n=n)
    assert len(picked) == min(n, len(members))
    assert len(set(picked)) == len(picked)
    assert set(picked) <= set(members)


@given(groups=st.lists(matrices, min_size=1, max_size=4))
def test_cohesion_is_a_cosine_distance(groups: list[np.ndarray]) -> None:
    assert 0.0 - 1e-9 <= cohesion_threshold(groups) <= 2.0 + 1e-9


labels = st.lists(st.sampled_from(["agy", "Agy", "nyelv", "gép", "ESSLLI"]), max_size=3)


@given(
    group=st.lists(labels, min_size=1, max_size=8),
    rest=st.lists(labels, max_size=20),
    min_count=st.integers(1, 3),
)
def test_over_represented_returns_its_counts(
    group: list[list[str]], rest: list[list[str]], min_count: int
) -> None:
    pool = group + rest
    for c in over_represented(group, pool, min_count=min_count):
        assert min_count <= c.in_group <= c.overall <= c.pool_size == len(pool)
        assert c.group_size == len(group)
        assert c.ratio > 1
        expected = (c.in_group / c.group_size) / (c.overall / c.pool_size)
        assert abs(c.ratio - expected) < 1e-12


@given(
    text=st.text(alphabet="abcágé .!?\n", max_size=600),
    terms=st.lists(st.text(alphabet="abcá", min_size=1, max_size=4), max_size=4),
)
def test_evidence_is_verbatim_and_short(text: str, terms: list[str]) -> None:
    quote = evidence_sentence(text, terms)
    if quote is not None:
        assert quote in text
        assert len(quote) <= MAX_QUOTE_CHARS
