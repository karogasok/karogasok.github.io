#!/usr/bin/env python3
"""Draw the OpenGraph card.

Generated rather than hand-designed so it cannot drift from the site: it reads
the same two typefaces out of static/fonts/ and uses the same paper, ink and
maroon as assets/css/site.css. Run it again after changing either.

Usage::

    python3 scripts/make_og.py
"""

from __future__ import annotations

import io
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "assets" / "og.png"

PAPER = "#f1f2ee"
INK = "#191b18"
MUTED = "#55594f"
ACCENT = "#7a1f1f"

TITLE = "Varjú Károgások"
LEDE = "Olvasónapló a mesterséges intelligenciáról,\na megismerésről és a következményeikről."
FOOT = "karogasok.github.io"

# Pillow cannot read woff2, and the repo deliberately ships woff2 only. The
# upstream TTFs are fetched here just to draw this one image; they are not
# committed and never reach the site.
UPSTREAM = {
    "display": "https://raw.githubusercontent.com/google/fonts/main/ofl/archivo/Archivo%5Bwdth%2Cwght%5D.ttf",
    "text": "https://raw.githubusercontent.com/google/fonts/main/ofl/spectral/Spectral-Regular.ttf",
}


def load(kind: str, size: int) -> ImageFont.FreeTypeFont:
    cache = Path("/tmp") / f"karogasok-og-{kind}.ttf"
    if not cache.exists():
        cache.write_bytes(urllib.request.urlopen(UPSTREAM[kind], timeout=60).read())
    return ImageFont.truetype(str(cache), size)


def main() -> int:
    img = Image.new("RGB", (1200, 630), PAPER)
    d = ImageDraw.Draw(img)

    # The same mark as the favicon and the nav: a crow's footprint, three toes
    # from a point. Not a stock bird silhouette.
    d.line([(96, 250), (96, 176)], fill=ACCENT, width=9)
    d.line([(96, 176), (46, 106)], fill=ACCENT, width=9)
    d.line([(96, 176), (146, 106)], fill=ACCENT, width=9)

    d.text((200, 150), TITLE, font=load("display", 92), fill=INK)
    d.multiline_text((200, 280), LEDE, font=load("text", 40), fill=MUTED, spacing=16)

    d.line([(96, 520), (1104, 520)], fill="#c9ccc2", width=2)
    d.text((96, 548), FOOT, font=load("display", 28), fill=MUTED)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
