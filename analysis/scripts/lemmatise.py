"""Lemmatise the whole corpus with emtsv, caching to ``out/lemmas.json``.

Resumable: documents already in the cache are skipped, so an interrupted run
costs only the documents it had not reached. Start the server with
``make emtsv-up`` first.

Usage:
    uv run python scripts/lemmatise.py
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from karogasok_temak.corpus import load_corpus
from karogasok_temak.emtsv import EmtsvError, lemmatize

OUT = Path(__file__).resolve().parents[1] / "out" / "lemmas.json"

#: emtsv slows down superlinearly on very long inputs, so anything longer is
#: analysed in paragraph-sized pieces and the lemma lists concatenated.
MAX_CHARS = 6000


def _chunks(text: str, limit: int = MAX_CHARS) -> list[str]:
    """Split text on paragraph breaks into pieces under ``limit`` characters."""
    if len(text) <= limit:
        return [text]
    pieces: list[str] = []
    current = ""
    for paragraph in text.split("\n"):
        if len(current) + len(paragraph) + 1 > limit and current:
            pieces.append(current)
            current = paragraph
        else:
            current = f"{current}\n{paragraph}" if current else paragraph
    if current:
        pieces.append(current)
    return pieces


def main() -> int:
    """Lemmatise every document, writing the cache as it goes."""
    documents = load_corpus()
    cache: dict[str, list[str]] = {}
    if OUT.exists():
        cache = json.loads(OUT.read_text(encoding="utf-8"))
    todo = [d for d in documents if d.doc_id not in cache]
    print(
        f"{len(documents)} documents, {len(cache)} cached, {len(todo)} to do",
        flush=True,
    )

    failures: list[str] = []
    started = time.monotonic()
    for index, document in enumerate(todo, start=1):
        try:
            lemmas: list[str] = []
            for piece in _chunks(document.text):
                lemmas.extend(lemmatize(piece))
            cache[document.doc_id] = lemmas
        except (EmtsvError, OSError) as error:
            failures.append(f"{document.doc_id}: {error}")
            continue
        if index % 25 == 0 or index == len(todo):
            rate = index / (time.monotonic() - started)
            print(
                f"  {index}/{len(todo)}  {rate:.1f} docs/s  "
                f"eta {(len(todo) - index) / rate:.0f}s",
                flush=True,
            )
            OUT.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")

    OUT.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    empty = sum(1 for lemmas in cache.values() if not lemmas)
    print(f"wrote {OUT} — {len(cache)} documents, {empty} with no content words")
    if failures:
        print(f"{len(failures)} failed:", *failures[:10], sep="\n  ")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
