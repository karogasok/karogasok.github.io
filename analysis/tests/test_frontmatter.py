"""Contracts for reading back the list keys the front-matter writer produces."""

from __future__ import annotations

from hypothesis import given
from hypothesis import strategies as st

from karogasok_temak.frontmatter import read_list_key, update_front_matter

#: One-line values: anything a keyword or theme name could plausibly hold,
#: including the YAML-significant characters that force quoting.
values = st.text(
    alphabet=st.characters(blacklist_categories=("Cc", "Cs", "Zl", "Zp")),
    max_size=20,
)


@given(st.lists(values, max_size=6))
def test_reads_back_what_was_written(items: list[str]) -> None:
    text = update_front_matter("---\ntitle: A\n---\n\nSzöveg.\n", {"k": items})
    assert read_list_key(text, "k") == items


@given(st.lists(values, min_size=1, max_size=6))
def test_other_keys_are_not_read(items: list[str]) -> None:
    text = update_front_matter("---\ntitle: A\n---\n", {"kk": items, "k2": ["x"]})
    assert read_list_key(text, "k") == []
