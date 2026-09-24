"""Validate analysis/temalista.yaml against the corpus and the site's history.

Every seed must be one of the author's own pages, dated no later than today and
at least MIN_FIT_WORDS long. Every theme name the site has ever published — read
from the git history of data/temak.yaml, not from memory — must still be
accounted for, because each one is a URL somebody may hold.

Usage:
    uv run python scripts/check_themes.py

Exits non-zero on any error.
"""

from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

from karogasok_temak import themes
from karogasok_temak.corpus import MIN_FIT_WORDS, SITE, load_corpus

HERE = Path(__file__).resolve().parents[1]


def published_names() -> set[str]:
    """Every ``nev`` that has ever appeared in data/temak.yaml, per git."""
    log = subprocess.run(
        ["git", "log", "-p", "--all", "--", "data/temak.yaml"],
        cwd=SITE,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    names = set(re.findall(r'^[+ ]  nev: "?(.+?)"?$', log, re.M))
    # Renamed before data/temak.yaml carried the current spelling; its alias
    # has been live since.
    names.add("A blog életéből")
    return names


def usable_pages() -> dict[str, int]:
    """The author's own pages that may seed a theme, with their word counts."""
    today = dt.date.today()
    out: dict[str, int] = {}
    for doc in load_corpus():
        if doc.source not in ("archivum", "posts"):
            continue
        if doc.year and doc.year > today.year:
            continue
        if doc.word_count >= MIN_FIT_WORDS:
            out[doc.doc_id] = doc.word_count
    return out


def main() -> int:
    """Print the report; fail on errors."""
    listed = themes.load(HERE / "temalista.yaml")
    names = published_names()
    report = themes.validate(listed, pages=usable_pages(), published_names=names)
    active = [t for t in listed if t.allapot == "aktiv"]
    print(
        f"  {len(active)} active, {len(listed) - len(active)} other; "
        f"{len(names)} names ever published"
    )
    for w in report.warnings:
        print(f"  warning: {w}")
    for e in report.errors:
        print(f"  ERROR: {e}")
    print("  OK" if report.ok else f"  {len(report.errors)} error(s)")
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
