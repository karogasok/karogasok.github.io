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

#: One document's membership scores. Not constrained to sum to 1: HDBSCAN's
#: soft-cluster vectors do not, and code that assumes they do would be wrong
#: about the real data.
probability_rows = st.lists(
    st.floats(min_value=0.0, max_value=1.0, allow_nan=False, allow_infinity=False),
    min_size=1,
    max_size=20,
)

#: A corpus's worth of label lists.
label_corpora = st.lists(
    st.lists(
        st.integers(min_value=0, max_value=18), min_size=0, max_size=4, unique=True
    ),
    min_size=0,
    max_size=40,
)
