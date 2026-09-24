"""Encode every writing in the corpus with the named encoders, filling the cache.

Placement needs a vector for every writing, not only the labelled ones the
embedder comparison used. The cache is keyed by text, so this only encodes what
is missing and can be interrupted.

Usage:
    uv run python scripts/encode_all.py e5-large [bge-m3 ...]
"""

from __future__ import annotations

import sys

from karogasok_temak.corpus import load_corpus
from karogasok_temak.embed import encode_cached, spec_named


def main() -> int:
    """Encode the whole corpus with each encoder named on the command line."""
    texts = [d.text for d in load_corpus() if d.text.strip()]
    for name in sys.argv[1:]:
        print(f"== {name}: {len(texts)} writings", flush=True)
        vectors = encode_cached(spec_named(name), texts)
        print(f"   done: {vectors.shape}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
