"""Chunking, mean-pooling and normalisation.

The encoder truncates at 128 word pieces — roughly 65–85 Hungarian words —
against a corpus whose median document is 414 words. So most of a post would be
thrown away by a naive ``encode(text)``. These tests pin the behaviour that
stops that happening.
"""

from __future__ import annotations

import numpy as np
import pytest
from hypothesis import given

from karogasok_temak.embed import CHUNK_WORDS, chunk_words, embed_documents

from .strategies import word_lists


class FakeEncoder:
    """A deterministic stand-in that records what it was asked to encode.

    Each sentence maps to a vector derived from its length and first character,
    which is enough to tell two different chunkings apart without loading a
    500 MB transformer.
    """

    def __init__(self) -> None:
        self.seen: list[str] = []

    def encode(
        self,
        sentences,  # noqa: ANN001 - matches SentenceTransformer's loose signature
        *,
        batch_size: int = 32,
        show_progress_bar: bool = False,
        convert_to_numpy: bool = True,
    ) -> np.ndarray:
        self.seen.extend(sentences)
        return np.array(
            [[len(s), ord(s[0]) if s else 0.0, 1.0] for s in sentences],
            dtype=np.float32,
        )


@given(word_lists)
def test_chunks_reconstruct_the_document(words: list[str]) -> None:
    """Chunking loses no word and reorders none."""
    rebuilt = [word for chunk in chunk_words(words) for word in chunk]
    assert rebuilt == list(words)


@given(word_lists)
def test_chunks_are_full_except_the_last(words: list[str]) -> None:
    chunks = list(chunk_words(words))
    assert chunks, "a non-empty document must produce at least one chunk"
    assert all(len(c) == CHUNK_WORDS for c in chunks[:-1])
    assert 0 < len(chunks[-1]) <= CHUNK_WORDS


def test_vectors_are_unit_length() -> None:
    texts = ["egy rövid szöveg", " ".join(["szó"] * 300)]
    vectors = embed_documents(texts, FakeEncoder())
    norms = np.linalg.norm(vectors, axis=1)
    assert np.allclose(norms, 1.0, atol=1e-6)


def test_a_long_document_is_pooled_not_truncated() -> None:
    """The whole document reaches the encoder, in several chunks."""
    long_text = " ".join(f"szo{i}" for i in range(300))
    encoder = FakeEncoder()
    embed_documents([long_text], encoder)
    assert len(encoder.seen) == np.ceil(300 / CHUNK_WORDS)
    assert "szo299" in encoder.seen[-1], "the tail of the document must be encoded"


def test_empty_document_raises() -> None:
    with pytest.raises(ValueError):
        embed_documents(["   "], FakeEncoder())


@pytest.mark.slow
def test_real_encoder_pools_rather_than_truncates() -> None:
    """A 400-word post embeds differently from its first 80 words.

    If the two matched, the extra chunks would be contributing nothing and the
    pooling would be decorative.
    """
    from sentence_transformers import SentenceTransformer

    from karogasok_temak.embed import MODEL_NAME

    model = SentenceTransformer(MODEL_NAME)
    head = "A nyelvi modellek statisztikai eszközök. " * 10
    tail = "A metafora a megismerés alapja, nem díszítés. " * 40
    full, prefix = embed_documents([head + tail, head], model)
    assert np.linalg.norm(full - prefix) > 0.05
