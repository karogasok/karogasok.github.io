#!/usr/bin/env python3
"""Import the Blogspot archive into content/archivum/.

Source: the Blogger export inside a Google Takeout archive, kept in
``scripts/raw/``. Note that this is the **2018** Blogger export schema
(``blogger:type``, ``blogger:status``, ``blogger:filename``) and not the older
2005 Atom format that most instructions on the internet describe. The 2018 file
is better for this job in one specific way: ``blogger:filename`` gives the
post's exact original path, so the canonical URL is read from the export rather
than reconstructed from the title and hoped to match.

The blog was a group blog with six bylines. Only Varjú Zoltán's posts are
imported; the other authors' work is theirs, and republishing it under this
site's name is not the importer's call to make. The manifest lists every post
that was skipped and why.

Nothing is curated. Every one of the author's live posts comes across, weak
ones included, with its original date, title and labels.

Usage::

    python3 scripts/import_blogspot.py [--no-download] [--limit N]
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_common import (  # noqa: E402
    CONTENT_DIR,
    ROOT,
    MediaResolver,
    Report,
    slugify,
    to_markdown,
    validate_markdown,
    write_post,
)

FEED = ROOT / "scripts" / "raw" / "blogspot-feed.atom"
BLOG_URL = "https://szamitogepesnyelveszet.blogspot.com"
BLOG_NAME = "Számítógépes Nyelvészet"

# The blog's own byline for the author of this site. The export writes the
# Blogger display name, which is unaccented.
AUTHOR_IN_EXPORT = "Zoltan Varju"
AUTHOR_ON_SITE = "Varjú Zoltán"

# An old label earns a browsable page once at least this many posts carry it.
# Below the threshold the label is still written to the post — nothing is lost —
# it just does not generate a page holding one item. The 2010 tag vocabulary ran
# to 452 distinct labels, most used once.
LABEL_PAGE_MIN = 3

A = "{http://www.w3.org/2005/Atom}"
B = "{http://schemas.google.com/blogger/2018}"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--no-download", action="store_true",
                   help="do not fetch images; leave every URL pointing at its original host")
    p.add_argument("--limit", type=int, default=0, help="import at most N posts (for a trial run)")
    return p.parse_args()


def text_of(entry: ET.Element, tag: str) -> str:
    return (entry.findtext(tag) or "").strip()


def main() -> int:
    args = parse_args()
    if not FEED.exists():
        print(f"error: {FEED} not found.", file=sys.stderr)
        print("  Put the Blogger feed.atom from the Takeout archive there and re-run.", file=sys.stderr)
        return 1

    root = ET.parse(FEED).getroot()
    entries = root.findall(A + "entry")
    report = Report("blogspot")

    # Two passes. The first counts labels across everything that will actually be
    # imported, because the page threshold has to be decided on the imported set
    # rather than on the whole export.
    keep: list[ET.Element] = []
    for entry in entries:
        kind = text_of(entry, B + "type")
        status = text_of(entry, B + "status")
        author_el = entry.find(A + "author")
        author = author_el.findtext(A + "name") if author_el is not None else ""
        title = text_of(entry, A + "title")

        if kind != "POST":
            report.count(f"skipped: not a post ({kind.lower()})")
            continue
        if status != "LIVE":
            report.count(f"skipped: {status.lower()}")
            report.rows.append({"title": title, "date": "", "author": author,
                                "status": "skipped", "reason": status.lower(), "file": ""})
            continue
        if author != AUTHOR_IN_EXPORT:
            report.count("skipped: another author on the group blog")
            report.rows.append({"title": title, "date": text_of(entry, A + "published")[:10],
                                "author": author, "status": "skipped",
                                "reason": "different author", "file": ""})
            continue
        keep.append(entry)

    if args.limit:
        keep = keep[: args.limit]

    label_counts: collections.Counter[str] = collections.Counter()
    for entry in keep:
        for cat in entry.findall(A + "category"):
            term = (cat.get("term") or "").strip()
            if term:
                label_counts[term] += 1
    paged_labels = {l for l, n in label_counts.items() if n >= LABEL_PAGE_MIN}

    print(f"blogspot: {len(keep)} posts to import, "
          f"{len(label_counts)} distinct labels, "
          f"{len(paged_labels)} of them above the page threshold ({LABEL_PAGE_MIN})")

    media = MediaResolver(report, download=not args.no_download)
    seen: set[str] = set()

    for entry in keep:
        title = text_of(entry, A + "title") or "(cím nélkül)"
        published = text_of(entry, A + "published")
        updated = text_of(entry, A + "updated")
        filename = text_of(entry, B + "filename")
        raw = entry.findtext(A + "content") or ""

        labels = sorted({(c.get("term") or "").strip() for c in entry.findall(A + "category")} - {""})
        paged = [l for l in labels if l in paged_labels]

        slug = slugify(title)
        # The original path is the most reliable slug source there is: it is what
        # the URLs of the last fifteen years actually pointed at.
        if filename:
            stem = Path(filename).stem
            if stem:
                slug = slugify(stem)
        base = slug
        n = 2
        while slug in seen:
            slug = f"{base}-{n}"
            n += 1
        seen.add(slug)

        canonical = f"{BLOG_URL}{filename}" if filename else ""
        body = to_markdown(raw, media, context=canonical or title)
        validate_markdown(body, canonical or title, report)

        front = {
            "title": title,
            "date": published or updated,
            "publishDate": published or updated,
            "author": AUTHOR_ON_SITE,
            "archiv": True,
            "forras_platform": "blogspot",
            "forras_cim": BLOG_NAME,
            "canonical": canonical,
            "regi_cimkek": paged,
            # Every label the post carried, including the ones too rare to get a
            # page. The record stays complete even where the navigation does not.
            "regi_cimkek_mind": labels,
        }
        path = CONTENT_DIR / f"{published[:10]}-{slug}.md"
        write_post(path, front, body)
        report.count("posts imported")
        report.rows.append({
            "title": title, "date": published[:10], "author": AUTHOR_ON_SITE,
            "status": "imported", "reason": "",
            "file": str(path.relative_to(ROOT)),
        })

    print("\n" + report.summary())
    print()
    report.write()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
