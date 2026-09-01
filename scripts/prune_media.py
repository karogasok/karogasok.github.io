#!/usr/bin/env python3
"""Delete archive media that nothing links to any more.

``static/archivum/img/`` is derived entirely from the two importers, but an
import only ever adds. When a conversion changes — a widget stops being carried
over, a URL stops being localised — the files it used to produce stay on disk,
referenced by nothing, shipped to every visitor's browser in the sitemap-sized
repository and never requested.

This is the other half of the import: scan the content for the files it actually
mentions, and remove the rest. Safe to run after any import, and safe to run
twice.

Nothing outside ``static/archivum/img/`` is touched, and a file is only removed
when no file under ``content/`` mentions its name at all — the test is the
filename, not a parsed link, so a reference inside raw HTML or a front-matter
field counts just as much as a Markdown image.

Usage::

    python3 scripts/prune_media.py           # report and delete
    python3 scripts/prune_media.py --dry-run # report only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "static" / "archivum" / "img"
CONTENT = ROOT / "content"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="list what would go, delete nothing")
    args = ap.parse_args()

    if not IMG_DIR.is_dir():
        print(f"prune_media: {IMG_DIR} does not exist, nothing to do")
        return 0

    files = sorted(p for p in IMG_DIR.iterdir() if p.is_file())
    if not files:
        print("prune_media: no media on disk")
        return 0

    # One pass over the content, rather than one grep per file: at 364 posts and
    # 138 media files the naive version is 50,000 file reads.
    haystack = "\n".join(
        p.read_text(encoding="utf-8", errors="replace")
        for p in CONTENT.rglob("*.md")
    )

    orphans = [p for p in files if p.name not in haystack]
    if not orphans:
        print(f"prune_media: all {len(files)} files are referenced, nothing to remove")
        return 0

    freed = sum(p.stat().st_size for p in orphans)
    verb = "would remove" if args.dry_run else "removing"
    print(f"prune_media: {verb} {len(orphans)} of {len(files)} files ({freed / 1024:.0f} KB)")
    for p in orphans:
        print(f"  {p.name:<28} {p.stat().st_size:>9,} bytes")
        if not args.dry_run:
            p.unlink()

    kept = len(files) - len(orphans)
    print(f"prune_media: {kept} files kept")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
