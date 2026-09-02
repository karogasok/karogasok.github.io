"""Fit the topic model and write ``out/topics.json``.

Run ``scripts/lemmatise.py`` first. Embeddings are cached in ``out/`` so
re-fitting with different clustering settings does not re-run the encoder.

The split matters: the model is **fitted** only on documents long enough to
carry a theme, and the short ones — search-blog leads, media blurbs — are then
placed onto the fitted topics. Fitting on everything would let 37-word blurbs,
which are the majority of the corpus by count, define what the themes are.

Usage:
    uv run python scripts/fit_topics.py [--min-cluster-size N]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

from karogasok_temak.corpus import Document, load_corpus
from karogasok_temak.embed import MODEL_NAME, embed_documents
from karogasok_temak.naming import evidence_quote
from karogasok_temak.stopwords import hungarian_stopwords
from karogasok_temak.topics import (
    MIN_CLUSTER_SIZE,
    OUTLIER,
    RANDOM_SEED,
    assign,
    build_model,
    drop_stopwords,
    fit_topics,
    summarise,
)

OUT = Path(__file__).resolve().parents[1] / "out"

#: Representative documents kept per topic, for naming and for the review file.
N_REPRESENTATIVE = 6

#: Topic terms kept per topic.
N_TERMS = 12


def _fingerprint(documents: list[Document]) -> str:
    """Hash the exact texts that will be encoded.

    Keying the cache on document ids alone is not enough: changing
    :func:`strip_markup` changes the text without changing a single id, and the
    stale vectors would be reused in silence.
    """
    digest = hashlib.sha256()
    for document in documents:
        digest.update(document.doc_id.encode("utf-8"))
        digest.update(b"\0")
        digest.update(document.text.encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def _embeddings(documents: list[Document]) -> np.ndarray:
    """Encode every document, caching against the exact texts encoded."""
    cache = OUT / "embeddings.npz"
    ids = [d.doc_id for d in documents]
    fingerprint = _fingerprint(documents)
    if cache.exists():
        stored = np.load(cache, allow_pickle=True)
        if str(stored["fingerprint"]) == fingerprint:
            print("  embeddings: cache hit", flush=True)
            return stored["vectors"]
        print("  embeddings: corpus text changed, re-encoding", flush=True)

    from sentence_transformers import SentenceTransformer

    print(f"  embeddings: loading {MODEL_NAME}", flush=True)
    model = SentenceTransformer(MODEL_NAME)
    vectors = embed_documents(
        [d.text for d in documents], model, show_progress_bar=True
    )
    np.savez(
        cache,
        doc_ids=np.array(ids, dtype=object),
        vectors=vectors,
        fingerprint=np.array(fingerprint),
    )
    return vectors


def main() -> int:
    """Fit, place the short documents, and write the review file."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-cluster-size", type=int, default=MIN_CLUSTER_SIZE)
    args = parser.parse_args()

    lemma_path = OUT / "lemmas.json"
    if not lemma_path.exists():
        print("out/lemmas.json missing — run scripts/lemmatise.py first")
        return 1
    lemmas: dict[str, list[str]] = json.loads(lemma_path.read_text(encoding="utf-8"))

    documents = [d for d in load_corpus() if lemmas.get(d.doc_id)]
    print(f"{len(documents)} documents with lemmas", flush=True)

    vectors = _embeddings(documents)
    lemma_docs = drop_stopwords(
        [" ".join(lemmas[d.doc_id]) for d in documents], hungarian_stopwords()
    )

    fit_idx = [i for i, d in enumerate(documents) if d.fittable]
    rest_idx = [i for i, d in enumerate(documents) if not d.fittable]
    print(f"  fitting on {len(fit_idx)}, placing {len(rest_idx)}", flush=True)

    model = build_model(min_cluster_size=args.min_cluster_size, seed=RANDOM_SEED)
    fit_topics_list, probabilities = fit_topics(
        model,
        [lemma_docs[i] for i in fit_idx],
        vectors[fit_idx],
    )

    reduced = model.reduce_outliers(
        [lemma_docs[i] for i in fit_idx], fit_topics_list, strategy="c-tf-idf"
    )
    placed = assign(model, [lemma_docs[i] for i in rest_idx], vectors[rest_idx])

    summary = summarise(fit_topics_list)
    print(
        f"\n  topics: {summary.n_topics}"
        f"\n  outliers: {summary.outlier_share:.1%}"
        f"\n  largest topic: {summary.largest_share:.1%}"
        f"\n  healthy: {summary.healthy}",
        flush=True,
    )

    assignments: dict[str, dict[str, object]] = {}
    for position, index in enumerate(fit_idx):
        assignments[documents[index].doc_id] = {
            "topic": int(fit_topics_list[position]),
            "topic_reduced": int(reduced[position]),
            "role": "fitted",
        }
    for position, index in enumerate(rest_idx):
        assignments[documents[index].doc_id] = {
            "topic": int(placed[position]),
            "topic_reduced": int(placed[position]),
            "role": "placed",
        }

    topics: list[dict[str, object]] = []
    for topic_id in sorted({t for t in fit_topics_list if t != OUTLIER}):
        terms = [term for term, _ in model.get_topic(topic_id)[:N_TERMS]]
        members = [
            (position, index)
            for position, index in enumerate(fit_idx)
            if fit_topics_list[position] == topic_id
        ]
        strengths = [
            float(probabilities[position].max())
            if probabilities.ndim == 2
            else float(probabilities[position])
            for position, _ in members
        ]
        ranked = sorted(zip(members, strengths), key=lambda pair: -pair[1])
        representative = []
        for (_, index), strength in ranked[:N_REPRESENTATIVE]:
            document = documents[index]
            representative.append(
                {
                    "doc_id": document.doc_id,
                    "title": document.title,
                    "year": document.year,
                    "strength": round(strength, 3),
                    "quote": evidence_quote(document.text, terms),
                }
            )
        topics.append(
            {
                "id": int(topic_id),
                "terms": terms,
                "size_fitted": len(members),
                "size_total": sum(
                    1 for a in assignments.values() if a["topic_reduced"] == topic_id
                ),
                "representative": representative,
                "name": None,
                "checked_by_human": False,
            }
        )

    payload = {
        "model": {
            "embedder": MODEL_NAME,
            "min_cluster_size": args.min_cluster_size,
            "seed": RANDOM_SEED,
        },
        "summary": {
            "n_topics": summary.n_topics,
            "n_fitted": summary.n_documents,
            "n_placed": len(rest_idx),
            "outlier_share": round(summary.outlier_share, 4),
            "largest_share": round(summary.largest_share, 4),
            "healthy": summary.healthy,
        },
        "topics": topics,
        "assignments": assignments,
    }
    (OUT / "topics.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\nwrote {OUT / 'topics.json'}")
    for topic in topics:
        terms = ", ".join(topic["terms"][:8])
        print(f"  {topic['id']:>3}  n={topic['size_fitted']:<4} {terms}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
