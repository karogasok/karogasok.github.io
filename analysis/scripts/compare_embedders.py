"""Which embedder puts writings the author labelled alike near each other?

Run once, to decide whether theme placement should keep huBERT or move to a
stronger multilingual model. Each candidate is judged by the share of a
writing's five nearest neighbours that carry one of the same cleaned labels —
the author's own labels, not a model's — separately for the archive pages and for
the tuning half of the Kereső Világ rows. The held-out half is not read.

Candidates are timed on 20 writings before any full encode, and every vector is
cached by the sha256 of the text it came from, so an interrupted run resumes.

Usage:
    uv run python scripts/compare_embedders.py [--only NAME ...]

Writes analysis/eval/embedder_comparison.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from karogasok_temak.corpus import load_corpus
from karogasok_temak.embed import embed_documents
from karogasok_temak.evaluate import (
    clean_labels,
    knn_shares,
    load_label_rules,
    paired_mean_delta,
    split_of,
)
from karogasok_temak.gold import archive_labels, kereses_labels

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "out"
EVAL = HERE / "eval"
CACHE = OUT / "embeddings"

#: Switch away from the current embedder only for at least this gain.
MIN_GAIN = 0.03


@dataclass(frozen=True)
class Spec:
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


SPECS = [
    Spec(
        "hubert",
        "NYTK/sentence-transformers-experimental-hubert-hungarian",
        80,
        "",
        128,
    ),
    # The card says symmetric tasks such as clustering use "query: ".
    Spec("e5-large", "intfloat/multilingual-e5-large", 200, "query: ", 512),
    # Capped well below the model's 8192: attention on CPU is quadratic, and
    # nearly every writing here fits in 2048 tokens anyway.
    Spec("bge-m3", "BAAI/bge-m3", 1100, "", 2048),
]


class _Prefixed:
    """Wrap an encoder so every chunk gets the model's required prefix."""

    def __init__(self, model: object, prefix: str) -> None:
        self.model = model
        self.prefix = prefix

    def encode(self, sentences: list[str], **kwargs: object) -> np.ndarray:  # noqa: D102
        return self.model.encode([self.prefix + s for s in sentences], **kwargs)


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _load_cache(spec: Spec) -> dict[str, np.ndarray]:
    path = CACHE / f"{spec.name}.npz"
    if not path.exists():
        return {}
    stored = np.load(path, allow_pickle=True)
    return dict(zip([str(h) for h in stored["hashes"]], stored["vectors"], strict=True))


def _save_cache(spec: Spec, cache: dict[str, np.ndarray]) -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    hashes = sorted(cache)
    np.savez(
        CACHE / f"{spec.name}.npz",
        hashes=np.array(hashes, dtype=object),
        vectors=np.array([cache[h] for h in hashes]),
        model=np.array(spec.model),
    )


def encode(spec: Spec, texts: list[str]) -> np.ndarray:
    """Vectors for ``texts``, encoding only what the cache does not hold."""
    cache = _load_cache(spec)
    todo = [t for t in dict.fromkeys(texts) if _digest(t) not in cache]
    if todo:
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(spec.model, device="cpu")
        model.max_seq_length = spec.max_seq_length
        encoder = _Prefixed(model, spec.prefix) if spec.prefix else model

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


def main() -> int:
    """Encode with each candidate and compare them on the author's labels."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", nargs="*", default=None)
    args = parser.parse_args()

    rules = load_label_rules(EVAL / "cimke_normalizalas.yaml")
    documents = [d for d in load_corpus() if d.text.strip()]
    by_key = {d.key or d.doc_id: d for d in documents}

    pages_gold = clean_labels(archive_labels(), rules)
    rows_gold = {
        k: v
        for k, v in clean_labels(kereses_labels(), rules).items()
        if split_of(k) == "dev"
    }
    sources = {
        "oldalak": [k for k in sorted(pages_gold) if k in by_key],
        "sorok": [k for k in sorted(rows_gold) if k in by_key],
    }
    gold = {"oldalak": pages_gold, "sorok": rows_gold}

    specs = [s for s in SPECS if not args.only or s.name in args.only]
    results: dict[str, dict[str, object]] = {}
    shares: dict[tuple[str, str, str], np.ndarray] = {}
    for spec in specs:
        print(f"== {spec.name} ({spec.model})", flush=True)
        keys = sources["oldalak"] + sources["sorok"]
        vectors = encode(spec, [by_key[k].text for k in keys])
        # Centre on the pages only, as placement will: adding blurbs must not
        # move the origin the author's own writing is measured from.
        centre = vectors[: len(sources["oldalak"])].mean(axis=0)
        for variant, space in (("raw", vectors), ("centred", vectors - centre)):
            row: dict[str, object] = {}
            offset = 0
            for source in ("oldalak", "sorok"):
                n = len(sources[source])
                s, _ = knn_shares(
                    space[offset : offset + n], sources[source], gold[source]
                )
                shares[(spec.name, variant, source)] = s
                row[source] = {"agreement": float(s.mean()), "n": int(len(s))}
                offset += n
            results[f"{spec.name}/{variant}"] = row
            print(
                f"   {variant:<8} pages {row['oldalak']['agreement']:.3f}   "
                f"rows {row['sorok']['agreement']:.3f}",
                flush=True,
            )

    baseline = ("hubert", "centred")
    comparisons: dict[str, dict[str, object]] = {}
    for (name, variant, source), s in shares.items():
        if (name, variant) == baseline or (
            baseline[0],
            baseline[1],
            source,
        ) not in shares:
            continue
        d = paired_mean_delta(shares[(baseline[0], baseline[1], source)], s)
        comparisons.setdefault(f"{name}/{variant}", {})[source] = {
            "delta": d.observed,
            "ci95": [d.low, d.high],
            "n": d.n,
            "clears_rule": d.observed >= MIN_GAIN and d.low > 0,
        }

    record = {
        "yardstick": "share of 5 nearest neighbours sharing a cleaned author label",
        "baseline": "/".join(baseline),
        "rule": f"switch only for a gain of at least {MIN_GAIN}, 95% CI above 0",
        "specs": {s.name: s.__dict__ for s in specs},
        "results": results,
        "vs_baseline": comparisons,
    }
    (EVAL / "embedder_comparison.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("\n  vs huBERT centred:")
    for name, per in comparisons.items():
        for source, c in per.items():
            flag = "CLEARS" if c["clears_rule"] else ""
            print(
                f"   {name:<18} {source:<8} Δ {c['delta']:+.3f}  "
                f"[{c['ci95'][0]:+.3f}, {c['ci95'][1]:+.3f}] {flag}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
