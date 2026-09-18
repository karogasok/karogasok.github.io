#!/usr/bin/env python3
"""Start a new post: the file, the image folder, and the URL it will have.

``make new`` only created the file, and named it after the title. A post called
"Az egész világ egy muslicát kínoz mostanában" therefore lived at a filename and
a URL of that length, and shortening either by hand meant renaming the file,
editing the front matter and remembering that Hugo takes the URL from the title
unless told otherwise. That is three chances to get it wrong before a word is
written.

Here the slug is one decision, made once, and everything follows from it: the
filename, the ``slug`` in the front matter, the URL, and the folder the images
go in.

Usage::

    python3 scripts/start_post.py -t "A cím" [-s rovid-slug] [--date 2026-09-18]

``-s`` is optional; without it the slug is made from the title.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from archive_common import slugify, yaml_quote  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "content" / "posts"
IMAGES = ROOT / "static" / "img"

#: Hour the drip publisher releases a post, matching the cron in deploy.yml.
PUBLISH_HOUR = 7


def front_matter(title: str, slug: str, when: dt.datetime) -> str:
    """The post's front matter, with the slug already decided.

    Args:
        title: The headline, as written.
        slug: The URL segment.
        when: Publication moment.

    Returns:
        The full front-matter block, newline-terminated.

    Example:
        >>> block = front_matter("A cím", "a-cim", dt.datetime(2026, 9, 18, 7, 0))
        >>> block.splitlines()[:4]
        ['---', 'title: "A cím"', 'slug: "a-cim"', 'date: 2026-09-18T07:00:00']
        >>> block.rstrip().endswith("---")
        True
    """
    stamp = when.isoformat()
    return (
        "---\n"
        f"title: {yaml_quote(title)}\n"
        f"slug: {yaml_quote(slug)}\n"
        f"date: {stamp}\n"
        f"publishDate: {stamp}\n"
        'author: "Varjú Zoltán"\n'
        'forras: ""\n'
        'forras_cim: ""\n'
        "tags: []\n"
        "draft: false\n"
        "---\n\n"
    )


def main() -> int:
    """Create the post and its image folder."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t", "--title", required=True)
    parser.add_argument("-s", "--slug", default="")
    parser.add_argument("--date", default="", help="ÉÉÉÉ-HH-NN, defaults to today")
    args = parser.parse_args()

    title = args.title.strip()
    if not title:
        print("kell egy cím", file=sys.stderr)
        return 1
    slug = slugify(args.slug or title)

    day = (
        dt.date.fromisoformat(args.date)
        if args.date
        else dt.datetime.now().astimezone().date()
    )
    when = dt.datetime.combine(day, dt.time(hour=PUBLISH_HOUR)).astimezone()

    path = POSTS / f"{day.isoformat()}-{slug}.md"
    if path.exists():
        print(f"már létezik: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    path.write_text(front_matter(title, slug, when), encoding="utf-8")

    # Git does not track an empty directory, so the folder would vanish between
    # creating it and putting the first picture in it.
    images = IMAGES / slug
    images.mkdir(parents=True, exist_ok=True)
    keep = images / ".gitkeep"
    if not any(p for p in images.iterdir() if p.name != ".gitkeep"):
        keep.touch()

    url = f"/{day.year}/{day.month:02d}/{slug}/"
    print(path.relative_to(ROOT))
    print(f"  URL          {url}")
    print(f"  képek        {images.relative_to(ROOT)}/  →  ![alt](/img/{slug}/abra.png)")
    print(f"  megjelenik   {when:%Y-%m-%d %H:%M} (állítsd a publishDate-et későbbre,")
    print("               ha várnia kell — a cron hétfő–csütörtök reggel enged ki)")
    print("  utána        make og · make youtube · analysis: infer.py, export_temak.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
