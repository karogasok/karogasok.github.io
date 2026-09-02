"""Properties of the multi-label assignment.

The doctests pin the worked examples; these pin the invariants that must hold
for every document in the corpus, including the ones nobody thought to check.
"""

from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis import strategies as st

from karogasok_temak.topics import (
    MULTI_LABEL_CAP,
    OUTLIER,
    label_set,
    label_spread,
    labels_above,
    probability_columns,
)

from .strategies import label_corpora, probability_rows


@given(probability_rows, st.floats(min_value=0.0, max_value=1.0))
def test_labels_above_is_sorted_and_respects_the_floor(
    row: list[float], floor: float
) -> None:
    columns = list(range(len(row)))
    result = labels_above(row, columns, floor=floor)
    assert all(score >= floor for _, score in result)
    assert [score for _, score in result] == sorted(
        (score for _, score in result), reverse=True
    )


@given(probability_rows)
def test_labels_above_rejects_a_mismatched_row(row: list[float]) -> None:
    """The off-by-one that would silently shift every score by one topic."""
    with pytest.raises(ValueError, match="disagree"):
        labels_above(row, list(range(len(row) + 1)))


@given(probability_rows, st.integers(min_value=-1, max_value=19))
def test_label_set_leads_with_the_primary(row: list[float], primary: int) -> None:
    columns = list(range(len(row)))
    ids, scores = label_set(row, columns, primary)
    assert len(ids) == len(scores)
    assert len(ids) == len(set(ids)), "a topic must not be labelled twice"
    assert len(ids) <= MULTI_LABEL_CAP
    if primary != OUTLIER and primary in columns:
        assert ids[0] == primary
    for topic in ids:
        assert topic in columns or topic == primary


@given(probability_rows)
def test_label_set_never_invents_a_label_for_an_empty_row(row: list[float]) -> None:
    """All-zero scores and no primary must give no theme at all."""
    zeros = [0.0] * len(row)
    ids, scores = label_set(zeros, list(range(len(row))), OUTLIER)
    assert ids == []
    assert scores == []


@given(label_corpora)
def test_label_spread_is_internally_consistent(corpus: list[list[int]]) -> None:
    spread = label_spread(corpus)
    assert sum(spread.counts.values()) == len(corpus)
    if corpus:
        assert spread.largest == max(len(labels) for labels in corpus)
        assert 0.0 <= spread.coverage <= 1.0
        assert spread.mean >= 0.0


@given(st.lists(st.integers(min_value=-1, max_value=25), max_size=50))
def test_probability_columns_excludes_the_outlier_bin(fitted: list[int]) -> None:
    columns = probability_columns(fitted)
    assert OUTLIER not in columns
    assert columns == sorted(set(columns))
