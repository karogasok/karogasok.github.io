"""Place newly written pieces onto the themes that are already published.

Reads the corpus, finds anything that has no entry in ``out/topics.json`` yet,
and works out its themes and keywords by **transforming it onto the saved
model** rather than fitting a new one. That distinction is the whole point: a
refit with one extra document can move cluster boundaries, and the writings
already tagged on the live site would silently change theme.

The artefacts are extended in place, so the ordinary export runs afterwards
unchanged:

    make emtsv-up
    uv run python scripts/infer.py
    uv run python scripts/export_temak.py
    make emtsv-down

Usage:
    uv run python scripts/infer.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import cast

import numpy as np

from karogasok_temak.corpus import SITE, Document, load_corpus
from karogasok_temak.embed import (
    MODEL_NAME,
    SentenceEncoder,
    embed_documents,
    fingerprint,
)
from karogasok_temak.emtsv import lemmatize
from karogasok_temak.keywords import TOP_N, corpus_counts, document_keywords
from karogasok_temak.stopwords import hungarian_stopwords
from karogasok_temak.topics import (
    OUTLIER,
    PROBABILITY_FLOOR,
    as_mixture,
    drop_stopwords,
    is_wordlike,
    label_set,
)

OUT = Path(__file__).resolve().parents[1] / "out"

#: emtsv slows down superlinearly on long inputs, so anything longer is analysed
#: in paragraph-sized pieces, as ``lemmatise.py`` does.
MAX_CHARS = 6000


def _pieces(text: str, limit: int = MAX_CHARS) -> list[str]:
    """Split text on paragraph breaks into pieces under ``limit`` characters."""
    if len(text) <= limit:
        return [text]
    out: list[str] = []
    current = ""
    for paragraph in text.split("\n"):
        if len(current) + len(paragraph) + 1 > limit and current:
            out.append(current)
            current = paragraph
        else:
            current = f"{current}\n{paragraph}" if current else paragraph
    if current:
        out.append(current)
    return out


def _doc_id(raw: str) -> str | None:
    """Turn what a person types into a corpus id.

    Accepts a path relative to the site, an absolute path, or a bare filename in
    ``content/posts/`` — the three things anyone would reasonably type.

    Args:
        raw: What was given on the command line.

    Returns:
        The id used in the artefacts, or ``None`` if there is no such file.
    """
    candidates = [Path(raw), SITE / raw, SITE / "content" / "posts" / raw]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate.resolve().relative_to(SITE))
    return None


def _load(name: str) -> dict:
    """Read a JSON artefact, failing with a usable message."""
    path = OUT / name
    if not path.exists():
        msg = f"{path} missing — run scripts/fit_topics.py first"
        raise SystemExit(msg)
    return json.loads(path.read_text(encoding="utf-8"))


def _vectors(documents: list[Document], fresh: list[Document]) -> np.ndarray:
    """Embeddings for the whole corpus, encoding only what is missing.

    The cache is rewritten in full corpus order with a new fingerprint, so a
    later refit still finds it valid instead of re-encoding all 814 documents.
    """
    cache = OUT / "embeddings.npz"
    cached: dict[str, np.ndarray] = {}
    if cache.exists():
        stored = np.load(cache, allow_pickle=True)
        cached = dict(
            zip([str(d) for d in stored["doc_ids"]], stored["vectors"], strict=True)
        )
    # Whatever is being done now is re-encoded, because its text may have
    # changed since it was last seen.
    for document in fresh:
        cached.pop(document.doc_id, None)
    known = cached

    from sentence_transformers import SentenceTransformer

    print(f"  encoding {len(fresh)} new document(s)", flush=True)
    encoder = cast("SentenceEncoder", SentenceTransformer(MODEL_NAME))
    new = embed_documents([d.text for d in fresh], encoder)
    known.update(zip([d.doc_id for d in fresh], new, strict=True))

    ordered = np.array([known[d.doc_id] for d in documents])
    np.savez(
        cache,
        doc_ids=np.array([d.doc_id for d in documents], dtype=object),
        vectors=ordered,
        fingerprint=np.array(fingerprint([(d.doc_id, d.text) for d in documents])),
    )
    return ordered


def main() -> int:
    """Infer themes and keywords for anything not yet in the artefacts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "paths",
        nargs="*",
        help="specific writings to do; without any, everything not yet done",
    )
    args = parser.parse_args()

    topics = _load("topics.json")
    keywords = _load("keywords.json")
    lemmas: dict[str, list[str]] = _load("lemmas.json")
    model_path = OUT / "model.pkl"
    if not model_path.exists():
        print(f"{model_path} missing — run scripts/fit_topics.py first")
        return 1

    documents = load_corpus()
    known = set(topics["assignments"])
    by_id = {d.doc_id: d for d in documents}

    if args.paths:
        fresh = []
        for raw in args.paths:
            doc_id = _doc_id(raw)
            if doc_id is None or doc_id not in by_id:
                print(f"nem találom a korpuszban: {raw}", file=sys.stderr)
                return 1
            fresh.append(by_id[doc_id])
        # A writing named outright is done again even if it was done before:
        # asking for it by name means it has changed since.
        redo = {d.doc_id for d in fresh}
    else:
        fresh = [d for d in documents if d.doc_id not in known]
        redo = set()
        if not fresh:
            print(f"nothing new — all {len(documents)} items already have themes.")
            return 0

    print(f"{len(fresh)} item(s) to do:")
    for document in fresh:
        again = " (again)" if document.doc_id in known else ""
        print(f"  {document.doc_id}  ({document.word_count} words){again}")

    for document in fresh:
        if document.doc_id in lemmas and document.doc_id not in redo:
            continue
        found: list[str] = []
        for piece in _pieces(document.text):
            found.extend(lemmatize(piece))
        lemmas[document.doc_id] = found
        print(f"  lemmatised {document.doc_id}: {len(found)} content words", flush=True)

    vectors = _vectors(documents, fresh)
    order = {d.doc_id: i for i, d in enumerate(documents)}

    from bertopic import BERTopic

    model = BERTopic.load(str(model_path))
    columns = [int(c) for c in topics["topic_columns"]]
    stops = hungarian_stopwords()
    lemma_docs = drop_stopwords([" ".join(lemmas[d.doc_id]) for d in fresh], stops)
    assigned, probabilities = model.transform(
        lemma_docs, vectors[[order[d.doc_id] for d in fresh]]
    )
    probabilities = np.asarray(probabilities)

    # Keyness is measured against the whole corpus, so the new piece is compared
    # with everything already written rather than with itself.
    filtered = {
        doc_id: [w for w in words if w.casefold() not in stops and is_wordlike(w)]
        for doc_id, words in lemmas.items()
    }
    totals = corpus_counts(list(filtered.values()))

    results: dict[str, dict[str, object]] = {}
    for position, document in enumerate(fresh):
        row = (
            probabilities[position]
            if probabilities.ndim == 2 and probabilities.shape[1] == len(columns)
            else np.zeros(len(columns))
        )
        strength = float(row.max()) if row.size else 0.0
        primary = int(assigned[position]) if strength >= PROBABILITY_FLOOR else OUTLIER
        ids, scores = label_set(as_mixture(row), columns, primary)
        found = document_keywords(filtered[document.doc_id], totals, top_n=TOP_N)
        results[document.doc_id] = {
            "topic": primary,
            "topic_reduced": primary,
            "role": "inferred",
            "topics": ids,
            "scores": scores,
        }
        keywords[document.doc_id] = [
            {
                "term": k.term,
                "score": round(k.score, 4),
                "effect_size": round(k.effect_size, 4),
                "count": k.count,
            }
            for k in found
        ]
        names = {int(t["id"]): t for t in topics["topics"]}
        labels = ", ".join(
            f"{', '.join(names[t]['terms'][:2])} ({s:.0%})"
            for t, s in zip(ids, scores, strict=True)
            if t in names
        )
        print(f"\n  {document.doc_id}")
        print(f"    themes  : {labels or '(none above the floor)'}")
        print(f"    keywords: {', '.join(k.term for k in found[:TOP_N]) or '(none)'}")

    if args.dry_run:
        print("\ndry run — nothing written.")
        return 0

    topics["assignments"].update(results)
    (OUT / "topics.json").write_text(
        json.dumps(topics, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (OUT / "keywords.json").write_text(
        json.dumps(keywords, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (OUT / "lemmas.json").write_text(
        json.dumps(lemmas, ensure_ascii=False), encoding="utf-8"
    )

    # The probability matrix is rebuilt in corpus order so report_multilabel.py
    # keeps working; rows for documents fitted earlier are carried across.
    stored = np.load(OUT / "probabilities.npz", allow_pickle=True)
    old = dict(zip([str(d) for d in stored["doc_ids"]], stored["matrix"], strict=True))
    for position, document in enumerate(fresh):
        old[document.doc_id] = (
            probabilities[position]
            if probabilities.ndim == 2 and probabilities.shape[1] == len(columns)
            else np.zeros(len(columns), dtype=np.float32)
        )
    np.savez(
        OUT / "probabilities.npz",
        doc_ids=np.array([d.doc_id for d in documents], dtype=object),
        columns=np.array(columns),
        matrix=np.array([old[d.doc_id] for d in documents], dtype=np.float32),
    )
    print(f"\nwrote {len(results)} inference(s). Now run scripts/export_temak.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
