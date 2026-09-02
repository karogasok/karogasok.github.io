"""Per-document keywords from the lemma cache, into ``out/keywords.json``.

Each document's keywords are its lemmas ranked against the rest of the corpus,
so a keyword is a word this piece leans on and the others do not. Documents too
short for any lemma to occur twice get an empty list, which is the honest
result for a two-sentence blurb.

Usage:
    uv run python scripts/extract_keywords.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from karogasok_temak.keywords import TOP_N, corpus_counts, document_keywords
from karogasok_temak.stopwords import hungarian_stopwords
from karogasok_temak.topics import is_wordlike

OUT = Path(__file__).resolve().parents[1] / "out"


def main() -> int:
    """Rank every document's lemmas against the rest of the corpus."""
    lemma_path = OUT / "lemmas.json"
    if not lemma_path.exists():
        print("out/lemmas.json missing — run scripts/lemmatise.py first")
        return 1
    lemmas: dict[str, list[str]] = json.loads(lemma_path.read_text(encoding="utf-8"))

    stops = hungarian_stopwords()
    filtered = {
        doc_id: [
            lemma
            for lemma in words
            if lemma.casefold() not in stops and is_wordlike(lemma)
        ]
        for doc_id, words in lemmas.items()
    }
    totals = corpus_counts(list(filtered.values()))
    print(f"{len(filtered)} documents, {len(totals)} distinct lemmas", flush=True)

    result: dict[str, list[dict[str, object]]] = {}
    for doc_id, words in filtered.items():
        result[doc_id] = [
            {
                "term": keyword.term,
                "score": round(keyword.score, 4),
                "effect_size": round(keyword.effect_size, 4),
                "count": keyword.count,
            }
            for keyword in document_keywords(words, totals, top_n=TOP_N)
        ]

    (OUT / "keywords.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    empty = sum(1 for keywords in result.values() if not keywords)
    print(f"wrote {OUT / 'keywords.json'}")
    print(f"  {len(result) - empty} documents with keywords, {empty} too short")
    return 0


if __name__ == "__main__":
    sys.exit(main())
