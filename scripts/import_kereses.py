#!/usr/bin/env python3
"""Collect the author's Kereső Világ posts as excerpt-and-link entries.

Between 2011 and mid-2018 he wrote on ``kereses.blog.hu`` as an employee of
Precognox. **That content is not his.** So unlike the Blogspot and WordPress
imports, nothing is copied here: this produces a list of leads and links, and
the full posts stay where they are and where they belong.

Which is also why the output is ``data/kereses.yaml`` and not files under
``content/``. These entries appear in the archive listing and in the year spine,
but they get no page of their own. Giving them pages would mean hosting several
hundred thin pages of somebody else's excerpt, each competing with the original
in search results and each needing a canonical pointing away from itself. A list
row hosts nothing and sends every reader to the original.

The blog is a group blog and he was the most frequent but not the only author,
so the filter is his numeric blog.hu user id rather than a display name or a
date range — authorship is the actual criterion, and an id does not get
misspelled. The dates in the result are an observation, not an input.

``robots.txt`` on that host disallows ``/admin/``, ``/api/`` and ``/reader``
only; post pages are fair game. Fetches are one at a time with a pause between
them and an identifying User-Agent, and every page is cached, so a re-run costs
the blog nothing.

Usage::

    python3 scripts/import_kereses.py            # resume from cache, fetch what is missing
    python3 scripts/import_kereses.py --limit 20 # a small trial run
    python3 scripts/import_kereses.py --refresh  # ignore the cache
"""

from __future__ import annotations

import argparse
import collections
import datetime
import html
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archive_common import ROOT, Report, yaml_quote  # noqa: E402

BLOG = "https://kereses.blog.hu"
BLOG_NAME = "Kereső Világ"
SITEMAP = f"{BLOG}/sitemap/urls.0.xml"
ARCHIVE = f"{BLOG}/archive"
CACHE = ROOT / "scripts" / "raw" / "kereses"
OUT = ROOT / "data" / "kereses.yaml"

# The author, as blog.hu knows him. A numeric id rather than "Zoltán Varjú":
# it is what the markup actually carries, and it cannot be mistyped or
# accent-folded into somebody else.
AUTHOR_UID = "555969"
AUTHOR_NAME = "Varjú Zoltán"

# blog.hu already truncates og:description, but for a very short post that
# summary *is* the whole post. This file should never hold more than a taste of
# work that is not ours, so it is capped again here.
LEAD_MAX = 300

DELAY = 0.5
USER_AGENT = "karogasok-index/1.0 (+https://karogasok.github.io/; collecting one author's own post list)"

AUTHOR_RE = re.compile(
    r'<span class="author">\s*<a href="[^"]*?user/(\d+)[^"]*">\s*(.*?)\s*</a>', re.S
)
OG_DESC_RE = re.compile(r'<meta property="og:description" content="([^"]*)"')
OG_TITLE_RE = re.compile(r'<meta property="og:title" content="([^"]*)"')
DATE_RE = re.compile(r"/(\d{4})/(\d{2})/(\d{2})/")
# The post's own tags live inside its <h3 class="date"> header, after "Címkék:".
# Matching /tags/ links across the whole page instead picks up the sidebar tag
# cloud, which belongs to the blog rather than to the post.
HEADER_RE = re.compile(r'<h3 class="date">(.*?)</h3>', re.S)
TAG_RE = re.compile(r'<a href="[^"]*/tags/[^"]*">([^<]+)</a>')


def check_coverage(post_urls: list[str], report: Report, refresh: bool) -> None:
    """Check the sitemap against the blog's own archive index.

    A sitemap is a courtesy file. If it were ever truncated or stale the import
    would quietly produce a smaller archive and nothing would look wrong, which
    is the failure worth guarding against here.

    ``/archive`` lists one link per week that has posts, which is the blog's own
    statement of what exists. Every declared week should contain at least one of
    the posts we crawled.

    The comparison allows a week either side: blog.hu does not number weeks the
    way ISO 8601 does — it emits a ``w0``, and its boundaries sit a week off in
    places. Those offsets are a numbering convention, not missing content, and
    were confirmed by hand against the weeks that disagreed.

    A gap is reported, not fatal. One odd week is an artefact of that numbering;
    refusing to write the output over it would be the wrong trade. A real
    truncation shows up as many weeks at once, and now says so.
    """
    page = fetch(ARCHIVE, cache_key="_archive", refresh=refresh)
    if not page:
        report.count("coverage check skipped: /archive unreachable")
        print("  ! could not read /archive — coverage unverified", file=sys.stderr)
        return

    declared = sorted({(int(y), int(w)) for y, w in re.findall(r"/(\d{4})/w(\d+)", page)})
    dates = sorted({
        datetime.date(*map(int, m.groups()))
        for m in (DATE_RE.search(u) for u in post_urls) if m
    })

    def covered(year: int, week: int) -> bool:
        """Is there a crawled post anywhere near this declared week?

        The week is turned into an approximate date rather than compared as a
        week number, because blog.hu does not number weeks the way ISO 8601
        does — it emits a ``w0``, and a 31 December post lands in the next
        year's first ISO week. Anchoring on a date and allowing ten days either
        side sidesteps the convention entirely, which is the point: the question
        is whether that stretch of the blog's history was crawled, not whose
        definition of "week 53" is right.
        """
        try:
            anchor = datetime.date(year, 1, 1) + datetime.timedelta(days=(week - 1) * 7)
        except ValueError:
            return True
        lo, hi = anchor - datetime.timedelta(days=10), anchor + datetime.timedelta(days=10)
        return any(lo <= d <= hi for d in dates)

    if not declared:
        # An empty declared set would make every check below pass by saying
        # nothing, which is the one result this function must never report.
        report.count("coverage check failed: /archive listed no weeks")
        print("  ! /archive listed no weeks — coverage NOT verified", file=sys.stderr)
        return

    gaps = [k for k in declared if not covered(*k)]
    print(f"  coverage: {len(declared)} weeks declared by /archive, "
          f"{len(dates)} distinct post dates across the {len(post_urls)} posts crawled")
    if gaps:
        print(f"  ! {len(gaps)} declared week(s) with nothing crawled near them "
              f"— check these by hand:", file=sys.stderr)
        for y, w in gaps:
            url = f"{BLOG}/{y}/w{w}"
            print(f"      {url}", file=sys.stderr)
            report.todo(f"COVERAGE nothing crawled near declared week  {url}")
        report.count("declared weeks with nothing crawled nearby", len(gaps))
    else:
        print("  coverage: every declared week is represented — the sitemap is complete")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--limit", type=int, default=0, help="only look at N posts")
    p.add_argument("--refresh", action="store_true", help="ignore the cache and refetch")
    return p.parse_args()


def fetch(url: str, cache_key: str | None = None, refresh: bool = False) -> str | None:
    """Fetch a page, via the on-disk cache unless told otherwise."""
    path = CACHE / f"{cache_key}.html" if cache_key else None
    if path and path.exists() and not refresh:
        return path.read_text(encoding="utf-8", errors="replace")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", "replace")
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
        print(f"  ! {url}: {exc}", file=sys.stderr)
        return None
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    time.sleep(DELAY)
    return body


def clean(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    args = parse_args()
    report = Report("kereses")
    CACHE.mkdir(parents=True, exist_ok=True)

    sitemap = fetch(SITEMAP, cache_key="_sitemap", refresh=args.refresh)
    if not sitemap:
        print("error: could not read the sitemap", file=sys.stderr)
        return 1
    urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sitemap) if DATE_RE.search(u)]
    if args.limit:
        urls = urls[: args.limit]
    print(f"kereses: {len(urls)} posts on the blog, checking each one's author")
    check_coverage(urls, report, args.refresh)

    authors: collections.Counter[str] = collections.Counter()
    entries: list[dict] = []

    for i, url in enumerate(urls, 1):
        key = re.sub(r"[^A-Za-z0-9]+", "_", url.replace(BLOG, "")).strip("_")
        page = fetch(url, cache_key=key, refresh=args.refresh)
        if not page:
            report.count("could not be fetched")
            report.todo(f"FETCH FAILED  {url}")
            continue

        m = AUTHOR_RE.search(page)
        uid = m.group(1) if m else "?"
        name = clean(m.group(2)) if m else "?"
        authors[f"{uid} {name}"] += 1
        if uid != AUTHOR_UID:
            report.count("skipped: another author")
            continue

        y, mo, d = DATE_RE.search(url).groups()
        og = OG_DESC_RE.search(page)
        lead = clean(og.group(1)) if og else ""
        if len(lead) > LEAD_MAX:
            lead = lead[:LEAD_MAX].rsplit(" ", 1)[0] + "…"
            report.count("lead truncated to the cap")
        if not lead:
            report.count("no lead on the page")
            report.todo(f"NO LEAD  {url}")

        hm = HEADER_RE.search(page)
        header = hm.group(1) if hm else ""
        title = OG_TITLE_RE.search(page)
        title = clean(title.group(1)) if title else url.rstrip("/").rsplit("/", 1)[-1]

        entries.append({
            "cim": title,
            "datum": f"{y}-{mo}-{d}",
            "link": url,
            "lead": lead,
            "cimkek": sorted({clean(t) for t in TAG_RE.findall(header)} - {""})[:6],
        })
        report.count("his posts")
        report.rows.append({"date": f"{y}-{mo}-{d}", "uid": uid, "title": title,
                            "lead_chars": len(lead), "url": url})

        if i % 100 == 0:
            print(f"  … {i}/{len(urls)} checked, {len(entries)} his so far")

    entries.sort(key=lambda e: e["datum"], reverse=True)

    lines = [
        "# Kereső Világ (kereses.blog.hu) — a szerző ottani bejegyzései.",
        "#",
        "# FONTOS: ezek a bejegyzések NEM a szerző tulajdonai. A Precognox",
        "# alkalmazottjaként írta őket, a teljes szövegek a Kereső Világ blogon",
        "# maradnak és ahhoz tartoznak. Itt csak a blog saját ajánlója (lead) és a",
        "# hivatkozás szerepel — se teljes szöveg, se saját oldal.",
        "#",
        "# Generálva: scripts/import_kereses.py — ezt szerkeszd, ne ezt a fájlt.",
        "",
        "irasok:",
    ]
    for e in entries:
        lines.append(f"  - cim: {yaml_quote(e['cim'])}")
        lines.append(f"    datum: {e['datum']}")
        lines.append(f"    link: {yaml_quote(e['link'])}")
        if e["lead"]:
            lines.append(f"    lead: {yaml_quote(e['lead'])}")
        if e["cimkek"]:
            lines.append("    cimkek:")
            lines.extend(f"      - {yaml_quote(t)}" for t in e["cimkek"])
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    years = collections.Counter(e["datum"][:4] for e in entries)
    print("\n" + report.summary())
    print("\nauthors seen on the blog:")
    for a, n in authors.most_common(8):
        print(f"  {n:>4}  {a}")
    print(f"\nhis posts by year: {dict(sorted(years.items()))}")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(entries)} entries)")
    report.write()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
