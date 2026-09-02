"""Hypothesis strategies for the corpus types."""

from __future__ import annotations

from hypothesis import strategies as st

#: A word is any run of non-whitespace, since that is exactly what the
#: whitespace-splitting vectoriser and :func:`chunk_words` treat as one token.
words = st.text(
    alphabet=st.characters(blacklist_categories=("Cc", "Cs", "Zs")),
    min_size=1,
    max_size=12,
)

#: A non-empty document, as a list of words.
word_lists = st.lists(words, min_size=1, max_size=400)
