"""Write the model's output onto the site.

Reads ``out/topics.json``, ``out/keywords.json`` and the names you approved in
``out/topic_names.json``, then:

* adds ``tema`` and ``kulcsszavak`` to the front matter of the pages the site
  owns, leaving every other line untouched;
* writes ``data/temak.yaml``, which carries the theme metadata **and** the
  external members — Kereső Világ leads, media and máshol entries — because
  those have no page of their own to hold front matter;
* creates a ``content/tema/<slug>/_index.md`` stub for each theme, ready for
  you to write the intro into.

Nothing here runs until a theme has ``checked_by_human: true``. A name invented
by a model is a draft, and drafts do not get to become site navigation.

Usage:
    uv run python scripts/export_temak.py [--dry-run] [--allow-unchecked]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from karogasok_temak.corpus import SITE, load_corpus
from karogasok_temak.frontmatter import quote, update_front_matter

OUT = Path(__file__).resolve().parents[1] / "out"

#: Keywords written into a page's front matter.
N_KEYWORDS = 6

#: Sources whose items are pages on this site; everything else is external.
PAGE_SOURCES = frozenset({"archivum", "posts"})


def _load(name: str) -> dict:
    """Read a JSON artefact, failing with a usable message."""
    path = OUT / name
    if not path.exists():
        msg = f"{path} missing — run the earlier scripts first"
        raise SystemExit(msg)
    return json.loads(path.read_text(encoding="utf-8"))


def term_directory(name: str) -> str:
    """The directory Hugo expects a taxonomy term's page to live in.

    Hugo derives a term's key from the term as written, lowercased with spaces
    turned into hyphens, and **keeps the accents** — ``removePathAccents``
    defaults to false. The permalink is a different string: ``/tema/:slug/``
    strips them. Naming the directory after the ASCII slug therefore produces a
    page Hugo never attaches to the term, and the symptom is quiet: the hub
    still builds, but with an auto-generated title-cased name, no external rows
    and no review notice, because the template joins on the title.

    Args:
        name: The theme name.

    Returns:
        The directory name.

    Example:
        >>> term_directory("Logika és matematika")
        'logika-és-matematika'
        >>> term_directory("NLP meetupok")
        'nlp-meetupok'
        >>> term_directory("A blog életéről")
        'a-blog-életéről'
    """
    cleaned = "".join(
        character if character.isalnum() or character in " -" else " "
        for character in name.lower()
    )
    return "-".join(cleaned.split())


def _collect_orphans(
    approved_slugs: set[str], *, remove: bool
) -> tuple[list[str], list[str]]:
    """Find hub directories no longer backed by an approved theme.

    Renaming a theme leaves its old directory behind, and a stale hub is a live
    URL listing nothing. Empty ones are deleted; **one carrying prose is never
    touched**, because that prose is the intro written by hand and losing it to
    a rename would be unforgivable. Those are reported instead.

    Args:
        approved_slugs: Term directory names that should exist.
        remove: Whether to delete the empty ones.

    Returns:
        ``(removed, kept)`` slugs.
    """
    root = SITE / "content" / "temak"
    if not root.is_dir():
        return [], []
    removed: list[str] = []
    kept: list[str] = []
    for directory in sorted(root.iterdir()):
        if not directory.is_dir() or directory.name in approved_slugs:
            continue
        index = directory / "_index.md"
        body = ""
        if index.exists():
            text = index.read_text(encoding="utf-8")
            # Everything after the closing fence of the front matter.
            body = text.partition("---\n")[2].partition("---\n")[2]
        if body.strip():
            kept.append(directory.name)
            continue
        if remove:
            for child in sorted(directory.rglob("*"), reverse=True):
                child.unlink() if child.is_file() else child.rmdir()
            directory.rmdir()
        removed.append(directory.name)
    return removed, kept


def main() -> int:
    """Write themes and keywords onto the site."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--allow-unchecked",
        action="store_true",
        help="export names you have not yet reviewed (for inspection only)",
    )
    args = parser.parse_args()

    topics = _load("topics.json")
    keywords = _load("keywords.json")
    names = _load("topic_names.json")

    approved = {
        int(topic_id): entry
        for topic_id, entry in names.items()
        if entry.get("checked_by_human") or args.allow_unchecked
    }
    if not approved:
        print("no theme has checked_by_human: true — nothing exported.")
        print("review out/topic_names.json first, or pass --allow-unchecked.")
        return 1
    unchecked = len(names) - sum(
        1 for entry in names.values() if entry.get("checked_by_human")
    )
    if unchecked:
        print(f"note: {unchecked} of {len(names)} names are still unreviewed")

    assignments = topics["assignments"]
    documents = {d.doc_id: d for d in load_corpus()}

    pages = 0
    externals: dict[int, list[dict[str, object]]] = {tid: [] for tid in approved}
    for doc_id, assignment in assignments.items():
        topic_id = int(assignment["topic_reduced"])
        if topic_id not in approved:
            continue
        document = documents.get(doc_id)
        if document is None:
            continue
        theme = approved[topic_id]["name"]
        terms = [k["term"] for k in keywords.get(doc_id, [])][:N_KEYWORDS]

        if document.source in PAGE_SOURCES:
            path = SITE / doc_id
            text = path.read_text(encoding="utf-8")
            updated = update_front_matter(
                text,
                # The taxonomy front-matter key is the *plural* — `temak`, as
                # `tags` is for the pillar taxonomy. Writing the singular gives
                # a clean build with no term pages at all, which is exactly
                # what it did the first time. The empty `tema` entry deletes
                # that earlier mistake where it has already been written.
                {"tema": [], "temak": [theme], "kulcsszavak": terms},
            )
            if updated != text and not args.dry_run:
                path.write_text(updated, encoding="utf-8")
            pages += 1
        else:
            externals[topic_id].append(
                {
                    "title": document.title,
                    "year": document.year,
                    "source": document.source,
                    "url": document.url,
                }
            )

    lines = [
        "# Generated by analysis/scripts/export_temak.py — do not edit by hand.",
        "# Each theme carries the model's evidence so a name can be checked",
        "# against the corpus rather than taken on trust.",
    ]
    for topic in topics["topics"]:
        topic_id = int(topic["id"])
        if topic_id not in approved:
            continue
        entry = approved[topic_id]
        lines.append(f"- id: {topic_id}")
        lines.append(f"  nev: {quote(entry['name'])}")
        lines.append(f"  slug: {quote(entry['slug'])}")
        lines.append(
            f"  ellenorizve: {str(bool(entry.get('checked_by_human'))).lower()}"
        )
        lines.append(f"  darab: {topic['size_total']}")
        lines.append("  kifejezesek:")
        lines.extend(f"    - {quote(term)}" for term in topic["terms"])
        first = topic["representative"][0] if topic["representative"] else None
        if first and first.get("quote"):
            lines.append("  idezet:")
            lines.append(f"    szoveg: {quote(first['quote'])}")
            lines.append(f"    forras: {quote(first['doc_id'])}")
        if externals[topic_id]:
            lines.append("  kulsok:")
            for item in sorted(
                externals[topic_id], key=lambda i: (-(i["year"] or 0), i["title"])
            ):
                lines.append(f"    - cim: {quote(str(item['title']))}")
                lines.append(f"      ev: {item['year'] or 'null'}")
                lines.append(f"      forras: {quote(str(item['source']))}")
                if item["url"]:
                    lines.append(f"      link: {quote(str(item['url']))}")

    data_path = SITE / "data" / "temak.yaml"
    stubs = 0
    removed: list[str] = []
    kept: list[str] = []
    if not args.dry_run:
        data_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        for topic_id, entry in approved.items():
            # Term pages live under the plural name, in the directory Hugo
            # derives from the term itself — accents and all.
            stub = (
                SITE / "content" / "temak" / term_directory(entry["name"]) / "_index.md"
            )
            if stub.exists():
                continue
            stub.parent.mkdir(parents=True, exist_ok=True)
            # The slug is explicit for the same reason every archive post's is:
            # Hugo derives it from the title, which here would keep the accents.
            stub.write_text(
                f"---\ntitle: {quote(entry['name'])}\n"
                f"slug: {quote(entry['slug'])}\n---\n\n",
                encoding="utf-8",
            )
            stubs += 1
        removed, kept = _collect_orphans(
            {term_directory(entry["name"]) for entry in approved.values()}, remove=True
        )

    for slug in kept:
        print(f"  orphan hub kept, it has prose in it: content/temak/{slug}/")
    for slug in removed:
        print(f"  removed empty orphan hub: content/temak/{slug}/")

    verb = "would update" if args.dry_run else "updated"
    print(f"{verb} {pages} pages across {len(approved)} themes")
    print(f"{verb} {data_path.relative_to(SITE)}, {stubs} new hub stubs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
