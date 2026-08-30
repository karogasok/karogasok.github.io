#!/usr/bin/env python3
"""Import the Hungarian posts from the WordPress blog into content/archivum/.

Source: a WXR export of ``blog.crowintelligence.org``, kept in ``scripts/raw/``.
That blog is bilingual and mostly English. Only the Hungarian posts belong on
this site, and deciding which those are is a judgement call that a stopword
ratio should not be allowed to make on its own.

So this script will not write anything on its first run. It classifies every
published post, writes a manifest, and stops. You read the manifest, correct any
row you disagree with, and re-run with the corrected file::

    python3 scripts/import_wordpress.py                       # classify, write manifest, stop
    # edit scripts/out/wordpress-manifest.csv — the `decision` column
    python3 scripts/import_wordpress.py --review scripts/out/wordpress-manifest.csv --write

The English posts are never touched under any invocation. The most a mistake
here can do is import a Hungarian post you wanted left out, or leave one out you
wanted in; neither is destructive and both are visible in the manifest.

The blog is still online, so every imported post points its canonical at the
original URL taken from the export.
"""

from __future__ import annotations

import argparse
import collections
import csv
import html as html_mod
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_common import (  # noqa: E402
    CONTENT_DIR,
    OUT_DIR,
    ROOT,
    MediaResolver,
    Report,
    slugify,
    to_markdown,
    validate_markdown,
    write_post,
)

EXPORT = ROOT / "scripts" / "raw" / "wordpress-export.xml"
BLOG_NAME = "Crow Intelligence blog"

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
}

# The WordPress login names, mapped to the bylines used on this site.
# crowintelligenceteam is the company account on the company's own blog; on this
# site those posts carry the author's name. This mapping is printed in the
# manifest precisely because it is an assumption and not a fact from the export.
AUTHORS = {
    "crowintelligenceteam": "Varjú Zoltán",
    "zoltanvarju": "Varjú Zoltán",
    "putzorsi": "Putz Orsolya",
}
DEFAULT_AUTHOR = "Varjú Zoltán"

LABEL_PAGE_MIN = 3

# Function words, which is what actually separates the two languages here. Both
# lists are deliberately short and common: a longer list would not change any
# decision, and the ambiguous cases are ambiguous because they are *short*, not
# because the vocabulary is exotic.
HU_WORDS = set("""
és hogy nem egy az volt van csak már meg még ez azt mint amely ahol ezt ami vagy de így
nagyon lehet kell aki mert néhány között szerint után előtt mikor amikor minden ilyen
olyan lesz lenne volna vannak voltak arra ebben ennek ahhoz szó dolog ezért illetve
""".split())
EN_WORDS = set("""
the and that not for with this from have are was were which where but very can must who
because some their there here when what would could should about into than then them they
""".split())
# ő and ű exist in no other language that could plausibly appear here.
HU_CHARS = re.compile(r"[őűŐŰ]")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--write", action="store_true",
                   help="actually write the posts. Without it the script only classifies.")
    p.add_argument("--review", type=Path,
                   help="a manifest CSV whose `decision` column overrides the detector")
    p.add_argument("--no-download", action="store_true", help="do not fetch images")
    return p.parse_args()


def strip_html(raw: str) -> str:
    return re.sub(r"<[^>]+>", " ", html_mod.unescape(raw))


def classify(title: str, body: str) -> tuple[str, int, int, int]:
    """Return (language, hungarian hits, english hits, word count).

    A fallback, and a cross-check. The authoritative signal is the URL — see
    ``language_of``.
    """
    words = re.findall(r"[a-zA-ZáéíóöőúüűÁÉÍÓÖŐÚÜŰ]+", f"{title} {body}".lower())
    hu = sum(1 for w in words if w in HU_WORDS)
    en = sum(1 for w in words if w in EN_WORDS)
    # A single ő or ű is worth a couple of stopwords: no English text contains one.
    hu += min(6, len(HU_CHARS.findall(f"{title} {body}"))) * 2
    if hu >= 3 and hu > en * 1.2:
        lang = "hu"
    elif en >= 3 and en > hu * 1.2:
        lang = "en"
    else:
        lang = "?"
    return lang, hu, en, len(words)


def main() -> int:
    args = parse_args()
    if not EXPORT.exists():
        print(f"error: {EXPORT} not found. Put the WXR export there and re-run.", file=sys.stderr)
        return 1

    channel = ET.parse(EXPORT).getroot().find("channel")
    report = Report("wordpress")

    overrides: dict[str, str] = {}
    if args.review:
        if not args.review.exists():
            print(f"error: review file {args.review} not found", file=sys.stderr)
            return 1
        with args.review.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                overrides[row["post_id"]] = (row.get("decision") or "").strip().lower()
        print(f"review: {len(overrides)} decisions read from {args.review}")

    candidates = []
    for item in channel.findall("item"):
        if item.findtext("wp:post_type", namespaces=NS) != "post":
            report.count("skipped: not a post")
            continue
        status = item.findtext("wp:status", namespaces=NS)
        if status != "publish":
            report.count(f"skipped: {status}")
            continue

        post_id = item.findtext("wp:post_id", namespaces=NS) or ""
        title = (item.findtext("title") or "").strip()
        raw = item.findtext("content:encoded", namespaces=NS) or ""
        url = item.findtext("link") or ""
        guess, hu, en, nwords = classify(title, strip_html(raw))

        # The blog is a multilingual WordPress, and its Hungarian permalinks
        # carry a /hu/ prefix. That is the site's own declaration of what
        # language a post is in, which beats counting function words — and it
        # settles the short posts, which are exactly the ones a word-count
        # heuristic cannot call. The stopword guess is kept alongside it as a
        # cross-check: the two agree on all 176 posts either can decide, and any
        # future disagreement is flagged rather than silently resolved.
        lang = "hu" if "/hu/" in url else "en"
        flag = "" if guess in (lang, "?") else f"detector says {guess}"

        decision = overrides.get(post_id) or ("import" if lang == "hu" else "skip")
        candidates.append({
            "post_id": post_id, "title": title,
            "date": (item.findtext("wp:post_date", namespaces=NS) or "")[:10],
            "wp_author": item.findtext("dc:creator", namespaces=NS) or "",
            "byline": AUTHORS.get(item.findtext("dc:creator", namespaces=NS) or "", DEFAULT_AUTHOR),
            "lang_from_url": lang, "stopword_guess": guess,
            "hu_hits": hu, "en_hits": en, "words": nwords,
            "disagreement": flag,
            "decision": decision,
            "url": url,
            "_item": item,
        })

    counts = collections.Counter(c["lang_from_url"] for c in candidates)
    chosen = [c for c in candidates if c["decision"] == "import"]
    disagree = [c for c in candidates if c["disagreement"]]
    print(f"wordpress: {len(candidates)} published posts — "
          f"{counts['hu']} Hungarian, {counts['en']} English (by URL prefix)")
    print(f"           {len(chosen)} marked for import, "
          f"{len(disagree)} where the stopword check disagrees")

    report.rows = [{k: v for k, v in c.items() if not k.startswith("_")} for c in candidates]

    if not args.write:
        report.write()
        print()
        print("Nothing was written. Read the manifest, fix any `decision` cell that is")
        print("wrong (`import` or `skip`), then re-run with:")
        print(f"  python3 {Path(__file__).name} --review {(OUT_DIR / 'wordpress-manifest.csv').relative_to(ROOT)} --write")
        print()
        if disagree:
            print("Rows where the URL and the word counts disagree — worth your time:")
            for c in disagree:
                print(f"  [{c['decision']:>6}] {c['date']}  url={c['lang_from_url']} "
                      f"hu={c['hu_hits']:<3} en={c['en_hits']:<3} {c['title'][:60]}")
        else:
            print("The URL prefix and the word counts agree on every post.")
        return 0

    media = MediaResolver(report, download=not args.no_download)
    label_counts: collections.Counter[str] = collections.Counter()
    for c in chosen:
        for cat in c["_item"].findall("category"):
            if cat.get("domain") == "post_tag" and cat.text:
                label_counts[cat.text.strip()] += 1
    paged_labels = {l for l, n in label_counts.items() if n >= LABEL_PAGE_MIN}

    seen: set[str] = set()
    for c in chosen:
        item = c["_item"]
        raw = item.findtext("content:encoded", namespaces=NS) or ""
        published = item.findtext("wp:post_date_gmt", namespaces=NS) or item.findtext("wp:post_date", namespaces=NS) or ""
        published = published.strip().replace(" ", "T") + "Z"

        labels = sorted({(cat.text or "").strip() for cat in item.findall("category")
                         if cat.get("domain") == "post_tag" and cat.text} - {""})
        paged = [l for l in labels if l in paged_labels]

        slug = slugify(item.findtext("wp:post_name", namespaces=NS) or c["title"])
        base, n = slug, 2
        while slug in seen:
            slug = f"{base}-{n}"; n += 1
        seen.add(slug)

        body = to_markdown(raw, media, context=c["url"] or c["title"])
        validate_markdown(body, c["url"] or c["title"], report)
        front = {
            "title": c["title"],
            "date": published,
            "publishDate": published,
            "author": c["byline"],
            "archiv": True,
            "forras_platform": "wordpress",
            "forras_cim": BLOG_NAME,
            "canonical": c["url"],
            "regi_cimkek": paged,
            "regi_cimkek_mind": labels,
        }
        path = CONTENT_DIR / f"{c['date']}-{slug}.md"
        write_post(path, front, body)
        report.count("posts imported")

    print("\n" + report.summary())
    print()
    report.write()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
