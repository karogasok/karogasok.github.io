"""The author's own historical labels, read from the site as the yardstick.

Two sources, never mixed, because they were labelled in different places with
different habits:

* **archive pages** — `regi_cimkek_mind` in the front matter: every label the
  post carried on Blogspot or WordPress, keyed by the page's path;
* **Kereső Világ rows** — `cimkek` in data/kereses.yaml: the blog.hu tags,
  keyed by the row's URL.

Keys are paths and URLs, never the corpus's positional ``kereses.yaml:17`` ids:
those shift when the importer reorders a file, and a yardstick keyed by them
would silently start judging the wrong writing.
"""

from __future__ import annotations

import re
from pathlib import Path

from karogasok_temak.corpus import SITE

_LIST_KEY = r"^{key}:\n((?:  - .*\n)+)"
_ITEM = re.compile(r"^  - (.*)$", re.M)


def _front_matter(text: str) -> str:
    return text.split("---", 2)[1] if text.startswith("---") else ""


def _yaml_list(front: str, key: str) -> list[str]:
    match = re.search(_LIST_KEY.format(key=re.escape(key)), front, re.M)
    if not match:
        return []
    return [m.strip().strip('"') for m in _ITEM.findall(match.group(1))]


def archive_labels(site: Path | None = None) -> dict[str, list[str]]:
    """Raw labels of every archive page that has any.

    Args:
        site: Site root. Defaults to the repository.

    Returns:
        Page path (``content/archivum/….md``) mapped to its labels as written.
    """
    root = site or SITE
    out: dict[str, list[str]] = {}
    for path in sorted((root / "content" / "archivum").glob("*.md")):
        if path.name == "_index.md":
            continue
        labels = _yaml_list(
            _front_matter(path.read_text(encoding="utf-8")), "regi_cimkek_mind"
        )
        if labels:
            out[str(path.relative_to(root))] = labels
    return out


def kereses_labels(site: Path | None = None) -> dict[str, list[str]]:
    """Raw blog.hu tags of every Kereső Világ row that has any.

    Args:
        site: Site root. Defaults to the repository.

    Returns:
        Row URL mapped to its tags as written.
    """
    root = site or SITE
    raw = (root / "data" / "kereses.yaml").read_text(encoding="utf-8")
    out: dict[str, list[str]] = {}
    for block in re.split(r"\n  - ", raw)[1:]:
        link = re.search(r'\n\s+link: "(.*?)"', "\n" + block)
        tags = re.search(r"\n    cimkek:\n((?:      - .*\n?)+)", "\n" + block)
        if not link or not tags:
            continue
        values = [
            t.strip().strip('"')
            for t in re.findall(r"^      - (.*)$", tags.group(1), re.M)
        ]
        if values:
            out[link.group(1)] = values
    return out
