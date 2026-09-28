"""Keywords for new writings, and themes for every writing, from frozen artefacts.

Two things happen, and neither refits anything:

1. **Keywords.** Anything without an entry in ``out/keywords.json`` (or named
   on the command line) is lemmatised with emtsv and its keywords are ranked
   by keyness against the whole corpus.
2. **Themes.** Every writing is placed on the curated theme list
   (``temalista.yaml``) with the calibration frozen in
   ``temalista_kalibracio.json`` — see :mod:`karogasok_temak.assign`. Only
   writings whose text the encoder has not seen are encoded, so this is quick
   after the first run. Because the calibration is frozen, a new writing never
   moves an old one; an old writing moves only if its own text changed.

The result goes to ``out/placement.json``, which the export reads:

    uv run python scripts/infer.py [paths...]
    uv run python scripts/export_temak.py

Usage:
    uv run python scripts/infer.py [--dry-run] [paths ...]

Fails if the theme list changed after the calibration was frozen: placing with a
calibration built for other seeds would be confident nonsense.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from karogasok_temak import themes as theme_list
from karogasok_temak.assign import SUBJECTLESS_LABELS, assign_corpus, key_of
from karogasok_temak.corpus import SITE, Document, load_corpus
from karogasok_temak.embed import EncoderSpec, encode_cached
from karogasok_temak.emtsv import lemmatize
from karogasok_temak.gold import archive_labels, kereses_labels
from karogasok_temak.keywords import (
    TOP_N,
    corpus_counts,
    document_keywords,
    keyword_lemmas,
)
from karogasok_temak.placement import StaleCalibrationError, load_calibration
from karogasok_temak.stopwords import hungarian_stopwords

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "out"
THEMES = HERE / "temalista.yaml"
CALIBRATION = HERE / "temalista_kalibracio.json"

#: emtsv slows down superlinearly on long inputs, so anything longer is analysed
#: in paragraph-sized pieces, as ``lemmatise.py`` does.
MAX_CHARS = 6000


def _pieces(text: str, limit: int = MAX_CHARS) -> list[str]:
    r"""Split text on paragraph breaks into pieces under ``limit`` characters.

    Example:
        >>> _pieces("aaa\nbbb\nccc", limit=7)
        ['aaa\nbbb', 'ccc']
    """
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
    """Read a JSON artefact; a missing one is an empty start."""
    path = OUT / name
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def main() -> int:  # noqa: C901, PLR0915
    """Keywords for what is new, themes for everything."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "paths",
        nargs="*",
        help="specific writings to redo; without any, everything not yet done",
    )
    args = parser.parse_args()

    try:
        cal, record = load_calibration(CALIBRATION, THEMES)
    except StaleCalibrationError as error:
        print(f"{error}", file=sys.stderr)
        return 1
    themes = theme_list.load(THEMES)
    names = {t.kulcs: t.nev for t in themes}

    keywords: dict[str, list[dict[str, object]]] = _load("keywords.json")
    lemmas: dict[str, list[str]] = _load("lemmas.json")
    documents = [d for d in load_corpus() if d.text.strip()]
    by_id = {d.doc_id: d for d in documents}

    if args.paths:
        fresh: list[Document] = []
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
        fresh = [d for d in documents if d.doc_id not in keywords]
        redo = set()

    if fresh:
        print(f"{len(fresh)} item(s) need keywords:")
        for document in fresh:
            print(f"  {document.doc_id}  ({document.word_count} words)")
    for document in fresh:
        if document.doc_id in lemmas and document.doc_id not in redo:
            continue
        found: list[str] = []
        for piece in _pieces(document.text):
            found.extend(lemmatize(piece))
        lemmas[document.doc_id] = found
        print(f"  lemmatised {document.doc_id}: {len(found)} content words", flush=True)

    # Keyness is measured against the whole corpus, so a new piece is compared
    # with everything already written rather than with itself.
    stops = hungarian_stopwords()
    filtered = {
        doc_id: keyword_lemmas(words, stops) for doc_id, words in lemmas.items()
    }
    totals = corpus_counts(list(filtered.values()))
    for document in fresh:
        found_kw = document_keywords(filtered[document.doc_id], totals, top_n=TOP_N)
        keywords[document.doc_id] = [
            {
                "term": k.term,
                "score": round(k.score, 4),
                "effect_size": round(k.effect_size, 4),
                "count": k.count,
            }
            for k in found_kw
        ]

    spec = EncoderSpec(**record["encoder"])
    vectors = encode_cached(spec, [d.text for d in documents])
    labels = {**archive_labels(), **kereses_labels()}
    placed = assign_corpus(documents, vectors, cal, themes, author_labels=labels)

    for document in fresh:
        a = placed[key_of(document)]
        shown = ", ".join(
            f"{names[t]} ({s:.2f})" for t, s in zip(a.themes, a.scores, strict=True)
        )
        terms = ", ".join(str(k["term"]) for k in keywords[document.doc_id][:TOP_N])
        print(f"\n  {document.doc_id}")
        print(f"    themes  : {shown or f'(nincs téma — legjobb: {a.best:.2f})'}")
        print(f"    keywords: {terms or '(none)'}")

    counts: dict[str, int] = {}
    for a in placed.values():
        counts[a.role] = counts.get(a.role, 0) + 1
    print(
        f"\n  {len(placed)} writings placed: "
        + ", ".join(f"{role} {n}" for role, n in sorted(counts.items()))
    )

    if args.dry_run:
        print("dry run — nothing written.")
        return 0

    payload = {
        "reproducibility": {
            "temalista_sha256": record["temalista_sha256"],
            "calibration_sha256": hashlib.sha256(CALIBRATION.read_bytes()).hexdigest(),
            "encoder": record["encoder"],
            "subjectless_labels": sorted(SUBJECTLESS_LABELS),
        },
        "placement": {
            key: {
                "temak": list(a.themes),
                "scores": list(a.scores),
                "best": a.best,
                "role": a.role,
            }
            for key, a in sorted(placed.items())
        },
    }
    (OUT / "placement.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    (OUT / "keywords.json").write_text(
        json.dumps(keywords, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (OUT / "lemmas.json").write_text(
        json.dumps(lemmas, ensure_ascii=False), encoding="utf-8"
    )
    print("wrote out/placement.json. Now run scripts/export_temak.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
