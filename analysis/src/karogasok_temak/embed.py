"""Embed Hungarian documents with huBERT, working around its 128-token window.

The model is ``NYTK/sentence-transformers-experimental-hubert-hungarian``, the
same one used in ``parlamonitor``, ``kmdb_dashboard`` and ``music_networks``.

Its ``max_seq_length`` is **128 tokens** -- roughly 65 to 85 Hungarian words --
against a corpus whose median document is 480 words. Encoding a document
directly would therefore throw away five sixths of it and silently return a
vector for the opening paragraph. So each document is cut into word windows,
every window is encoded, and the windows belonging to one document are averaged
and L2-normalised.

This is a port of ``parlamonitor/src/parlamonitor/topics.py::embed_documents``.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import Protocol

import numpy as np

MODEL_NAME = "NYTK/sentence-transformers-experimental-hubert-hungarian"
"""The Hungarian sentence encoder used across the Crow repositories."""

CHUNK_WORDS = 80
"""Words per window.

Under the model's 128-token limit with room to spare: Hungarian is
agglutinative, so a word is often more than one wordpiece.
"""


class SentenceEncoder(Protocol):
    """Anything with a ``SentenceTransformer``-shaped ``encode``."""

    def encode(
        self,
        sentences: Sequence[str],
        *,
        batch_size: int = ...,
        show_progress_bar: bool = ...,
        convert_to_numpy: bool = ...,
    ) -> np.ndarray:
        """Encode sentences into vectors."""
        ...


def chunk_words(words: Sequence[str], size: int = CHUNK_WORDS) -> Iterator[list[str]]:
    """Split a word list into consecutive windows.

    Args:
        words: The document's words.
        size: Window length. Defaults to :data:`CHUNK_WORDS`.

    Yields:
        Windows of at most ``size`` words. A short document yields one window.

    Raises:
        ValueError: If ``size`` is not positive.

    Example:
        >>> [len(w) for w in chunk_words(["a"] * 200, 80)]
        [80, 80, 40]
        >>> [w for w in chunk_words(["egy", "kettő"], 80)]
        [['egy', 'kettő']]
    """
    if size <= 0:
        raise ValueError(f"window size must be positive, got {size}")
    for start in range(0, len(words), size):
        yield list(words[start : start + size])


def embed_documents(
    texts: Sequence[str],
    model: SentenceEncoder,
    *,
    chunk_size: int = CHUNK_WORDS,
    batch_size: int = 32,
    show_progress_bar: bool = False,
) -> np.ndarray:
    """Embed documents by chunking, encoding and mean-pooling.

    Every chunk of every document is encoded in one batched call, then the
    chunks of a document are averaged and the result L2-normalised so cosine
    behaves downstream.

    Args:
        texts: The documents. Each needs at least one non-whitespace token.
        model: The encoder.
        chunk_size: Words per window. Defaults to :data:`CHUNK_WORDS`.
        batch_size: Encoder batch size. Defaults to 32.
        show_progress_bar: Passed to the encoder. Defaults to ``False``.

    Returns:
        Array of shape ``(len(texts), dim)``, each row unit length.

    Raises:
        ValueError: If ``texts`` is empty or a document has no tokens.
    """
    if len(texts) == 0:
        raise ValueError("cannot embed an empty document collection")

    chunks: list[str] = []
    offsets: list[tuple[int, int]] = []
    for index, text in enumerate(texts):
        words = text.split()
        if not words:
            raise ValueError(f"document {index} has no tokens to embed")
        start = len(chunks)
        chunks.extend(" ".join(window) for window in chunk_words(words, chunk_size))
        offsets.append((start, len(chunks)))

    encoded = np.asarray(
        model.encode(
            chunks,
            batch_size=batch_size,
            show_progress_bar=show_progress_bar,
            convert_to_numpy=True,
        ),
        dtype=np.float32,
    )

    pooled = np.stack([encoded[start:stop].mean(axis=0) for start, stop in offsets])
    norms = np.linalg.norm(pooled, axis=1, keepdims=True)
    # A zero vector cannot be normalised. It would take an encoder returning all
    # zeros, but staying silent here turns that into NaNs much further on.
    norms[norms == 0] = 1.0
    return pooled / norms
