"""Contracts for keyword lemma clean-up, over arbitrary tokens."""

from __future__ import annotations

from hypothesis import given
from hypothesis import strategies as st

from karogasok_temak.keywords import HYPHEN_SUFFIXES, normalise_lemma

tokens = st.text(
    alphabet=st.sampled_from(list("abcdeLLMAPIéőűö0123-.")), min_size=1, max_size=14
)


@given(tokens)
def test_idempotent(token: str) -> None:
    once = normalise_lemma(token)
    if once is not None:
        assert normalise_lemma(once) == once


@given(tokens)
def test_never_returns_empty(token: str) -> None:
    assert normalise_lemma(token) != ""


@given(
    st.text(alphabet=st.characters(blacklist_characters="-"), min_size=3, max_size=20)
)
def test_hyphen_free_tokens_longer_than_two_are_untouched(token: str) -> None:
    assert normalise_lemma(token) == token


@given(
    st.text(alphabet=st.sampled_from(list("ABCDEFGHXYZ")), min_size=2, max_size=6),
    st.sampled_from(sorted(HYPHEN_SUFFIXES)),
)
def test_acronym_endings_are_stripped(stem: str, ending: str) -> None:
    assert normalise_lemma(f"{stem}-{ending}") == stem
