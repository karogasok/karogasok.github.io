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
import re
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "assets" / "og.png"
CARDS = ROOT / "static" / "assets" / "og"
POSTS = ROOT / "content" / "posts"

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


def wrap(draw, text, font, width):
    """Greedy wrap to a pixel width. Long Hungarian compounds are why this
    measures rather than counting characters."""
    words, lines, line = text.split(), [], ""
    for w in words:
        trial = f"{line} {w}".strip()
        if draw.textlength(trial, font=font) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def post_cards() -> int:
    """One card per post, titled with the post's own headline.

    Posts only. The archive points its canonical at the blog that owns each
    piece, so giving those a card in this site's type would be putting this
    site's name on somebody else's writing.
    """
    if not POSTS.is_dir():
        return 0
    CARDS.mkdir(parents=True, exist_ok=True)
    display, text = load("display", 60), load("text", 30)
    made = 0
    for md in sorted(POSTS.glob("*.md")):
        if md.name == "_index.md":
            continue
        head = md.read_text(encoding="utf-8").split("---", 2)
        if len(head) < 3:
            continue
        m = re.search(r'^title:\s*"(.*)"\s*$', head[1], re.M)
        if not m or not m.group(1).strip():
            continue
        title = m.group(1)

        img = Image.new("RGB", (1200, 630), PAPER)
        d = ImageDraw.Draw(img)
        d.line([(96, 250), (96, 176)], fill=ACCENT, width=9)
        d.line([(96, 176), (46, 106)], fill=ACCENT, width=9)
        d.line([(96, 176), (146, 106)], fill=ACCENT, width=9)

        lines = wrap(d, title, display, 1000)[:4]
        y = 300 - (len(lines) - 1) * 38
        for ln in lines:
            d.text((96, y), ln, font=display, fill=INK)
            y += 76

        d.line([(96, 520), (1104, 520)], fill="#c9ccc2", width=2)
        d.text((96, 548), TITLE, font=text, fill=MUTED)

        (CARDS / f"{md.stem}.png").write_bytes(b"")
        img.save(CARDS / f"{md.stem}.png", optimize=True)
        made += 1
    return made


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
    n = post_cards()
    print(f"wrote {n} per-post card(s) into {CARDS.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
