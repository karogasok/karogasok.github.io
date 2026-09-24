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

import hashlib
import time
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, cast

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


def fingerprint(items: Sequence[tuple[str, str]]) -> str:
    """Hash the exact texts an embedding cache was built from.

    Keying a cache on document ids alone is not enough: changing
    :func:`~karogasok_temak.corpus.strip_markup` changes the text without
    changing a single id, and the stale vectors would be reused in silence.

    Takes ``(id, text)`` pairs rather than documents so the cache can be
    validated without importing the corpus loader, and so both the fitting
    script and the inference script compute it the same way.

    Args:
        items: ``(doc_id, text)`` in the order they are stored.

    Returns:
        A hex digest.

    Example:
        >>> fingerprint([("a", "szöveg")]) == fingerprint([("a", "szöveg")])
        True
        >>> fingerprint([("a", "szöveg")]) == fingerprint([("a", "más")])
        False
        >>> one = fingerprint([("a", "x"), ("b", "y")])
        >>> one == fingerprint([("b", "y"), ("a", "x")])
        False
    """
    digest = hashlib.sha256()
    for doc_id, text in items:
        digest.update(doc_id.encode("utf-8"))
        digest.update(b"\0")
        digest.update(text.encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


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


# --- Cached encoders -------------------------------------------------------
#
# Every vector is cached under the sha256 of the text it came from, one file per
# encoder, so adding a writing encodes that writing only and an interrupted run
# resumes. The encoder's id is stored alongside, and a cache is never shared
# between encoders.

#: Where the per-encoder caches live.
CACHE = Path(__file__).resolve().parents[2] / "out" / "embeddings"


@dataclass(frozen=True)
class EncoderSpec:
    """One embedder configuration.

    Attributes:
        name: Short label for reports and the cache file.
        model: Hugging Face model id.
        chunk_words: Words per chunk; chunks are mean-pooled.
        prefix: Prepended to every chunk, as the model's card asks.
        max_seq_length: Tokens the encoder may read per chunk.
    """

    name: str
    model: str
    chunk_words: int
    prefix: str
    max_seq_length: int


SPECS: list[EncoderSpec] = [
    EncoderSpec(
        "hubert",
        "NYTK/sentence-transformers-experimental-hubert-hungarian",
        80,
        "",
        128,
    ),
    # The card says symmetric tasks such as clustering use "query: ".
    EncoderSpec("e5-large", "intfloat/multilingual-e5-large", 200, "query: ", 512),
    # Capped well below the model's 8192: attention on CPU is quadratic, and
    # nearly every writing here fits in 2048 tokens anyway.
    EncoderSpec("bge-m3", "BAAI/bge-m3", 1100, "", 2048),
]


class _Prefixed:
    """Wrap an encoder so every chunk gets the model's required prefix."""

    def __init__(self, model: SentenceEncoder, prefix: str) -> None:
        self.model = model
        self.prefix = prefix

    def encode(  # noqa: D102
        self,
        sentences: Sequence[str],
        *,
        batch_size: int = 32,
        show_progress_bar: bool = False,
        convert_to_numpy: bool = True,
    ) -> np.ndarray:
        return self.model.encode(
            [self.prefix + s for s in sentences],
            batch_size=batch_size,
            show_progress_bar=show_progress_bar,
            convert_to_numpy=convert_to_numpy,
        )


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _load_cache(spec: EncoderSpec) -> dict[str, np.ndarray]:
    path = CACHE / f"{spec.name}.npz"
    if not path.exists():
        return {}
    stored = np.load(path, allow_pickle=True)
    return dict(zip([str(h) for h in stored["hashes"]], stored["vectors"], strict=True))


def _save_cache(spec: EncoderSpec, cache: dict[str, np.ndarray]) -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    hashes = sorted(cache)
    np.savez(
        CACHE / f"{spec.name}.npz",
        hashes=np.array(hashes, dtype=object),
        vectors=np.array([cache[h] for h in hashes]),
        model=np.array(spec.model),
    )


def encode_cached(spec: EncoderSpec, texts: list[str]) -> np.ndarray:
    """Vectors for ``texts``, encoding only what the cache does not hold."""
    cache = _load_cache(spec)
    todo = [t for t in dict.fromkeys(texts) if _digest(t) not in cache]
    if todo:
        from sentence_transformers import SentenceTransformer

        loaded = SentenceTransformer(spec.model, device="cpu")
        loaded.max_seq_length = spec.max_seq_length
        # SentenceTransformer.encode accepts far more than the protocol names,
        # so it does not satisfy it structurally although every call is valid.
        model = cast("SentenceEncoder", loaded)
        encoder: SentenceEncoder = (
            _Prefixed(model, spec.prefix) if spec.prefix else model
        )

        probe = todo[:20]
        start = time.monotonic()
        vectors = embed_documents(
            probe, encoder, chunk_size=spec.chunk_words, batch_size=4
        )
        per_doc = (time.monotonic() - start) / len(probe)
        cache.update({_digest(t): v for t, v in zip(probe, vectors, strict=True)})
        _save_cache(spec, cache)
        rest = todo[len(probe) :]
        print(
            f"  {spec.name}: {per_doc:.2f} s/writing, "
            f"~{per_doc * len(rest) / 60:.0f} min "
            f"for the remaining {len(rest)}",
            flush=True,
        )
        for i in range(0, len(rest), 50):
            batch = rest[i : i + 50]
            vectors = embed_documents(
                batch, encoder, chunk_size=spec.chunk_words, batch_size=4
            )
            cache.update({_digest(t): v for t, v in zip(batch, vectors, strict=True)})
            _save_cache(spec, cache)
            print(f"    {spec.name}: {min(i + 50, len(rest))}/{len(rest)}", flush=True)
    return np.array([cache[_digest(t)] for t in texts])


def spec_named(name: str) -> EncoderSpec:
    """The configured encoder called ``name``."""
    for spec in SPECS:
        if spec.name == name:
            return spec
    msg = f"no encoder spec named {name!r}"
    raise KeyError(msg)
