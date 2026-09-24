"""Properties the BCubed yardstick must have for any placement.

The doctests pin hand-computed cases; these pin the contracts that make the
scores comparable at all — bounds, a perfect score for a perfect placement, and
the symmetry between precision and recall.
"""

from __future__ import annotations

from hypothesis import given
from hypothesis import strategies as st

from karogasok_temak.evaluate import LabelRules, bcubed, clean_labels, split_of

keys = st.sampled_from([f"w{i}" for i in range(12)])
label_sets = st.frozensets(st.sampled_from(list("pqrst")), min_size=1, max_size=3)
gold_maps = st.dictionaries(keys, label_sets, min_size=1, max_size=12)
pred_maps = st.dictionaries(
    keys, st.lists(st.sampled_from(list("ABCD")), max_size=3, unique=True), max_size=12
)


@given(pred_maps, gold_maps)
def test_scores_are_bounded(pred: dict, gold: dict) -> None:
    s = bcubed(pred, gold)
    for value in (s.precision, s.recall, s.f):
        assert 0.0 <= value <= 1.0 + 1e-12
    assert s.n == len(gold)


@given(gold_maps)
def test_a_placement_equal_to_the_labels_is_perfect(gold: dict) -> None:
    s = bcubed({k: sorted(v) for k, v in gold.items()}, gold)
    assert abs(s.f - 1.0) < 1e-12


@given(gold_maps, gold_maps)
def test_swapping_sides_swaps_precision_and_recall(a: dict, b: dict) -> None:
    common = sorted(set(a) & set(b))
    if not common:
        return
    ab = bcubed({k: sorted(a[k]) for k in common}, {k: b[k] for k in common})
    ba = bcubed({k: sorted(b[k]) for k in common}, {k: a[k] for k in common})
    assert abs(ab.precision - ba.recall) < 1e-12
    assert abs(ab.recall - ba.precision) < 1e-12


@given(st.lists(st.text(min_size=1, max_size=20), min_size=1, max_size=30))
def test_split_is_a_pure_function_of_the_key(xs: list[str]) -> None:
    for x in xs:
        assert split_of(x) == split_of(x) in {"dev", "test"}


@given(
    st.dictionaries(keys, st.lists(st.sampled_from(["A", "a", "g", "z"]), max_size=4))
)
def test_cleaned_labels_are_never_empty_and_never_genres(raw: dict) -> None:
    rules = LabelRules(frozenset({"g"}), {"z": "a"}, 2)
    for labels in clean_labels(raw, rules).values():
        assert labels
        assert "g" not in labels and "z" not in labels
