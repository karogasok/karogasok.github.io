"""Write the model's output onto the site.

Reads ``out/topics.json``, ``out/keywords.json`` and the names you approved in
``out/topic_names.json``, then:

* adds ``temak`` and ``kulcsszavak`` to the front matter of the pages the site
  owns, leaving every other line untouched;
* writes ``data/temak.yaml`` and ``data/kulcsszavak.yaml``, each carrying the
  hub's metadata **and** its external members — Kereső Világ leads, media and
  máshol entries — because those have no page of their own to hold front
  matter;
* writes ``data/temak_index.yaml``, the tags of every external item keyed by
  its URL, so the archive, máshol and média lists can show them;
* creates a ``content/temak/<term>/_index.md`` stub for each theme, ready for
  you to write the intro into.

Both taxonomies are multi-valued: a writing carries every theme that makes up at
least :data:`~karogasok_temak.topics.MULTI_LABEL_FLOOR` of its topic mixture,
and its strongest :data:`N_KEYWORDS` keywords.

Nothing here runs until a theme has ``checked_by_human: true``. A name invented
by a model is a draft, and drafts do not get to become site navigation.

Usage:
    uv run python scripts/export_temak.py [--dry-run] [--allow-unchecked]
"""

from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from collections import Counter, defaultdict
from collections.abc import Mapping
from pathlib import Path

from karogasok_temak.corpus import SITE, Document, load_corpus
from karogasok_temak.frontmatter import quote, update_front_matter

OUT = Path(__file__).resolve().parents[1] / "out"

#: Keywords written onto each item. Five is what fits a line of metadata under
#: a title without the tags outweighing the thing they describe.
N_KEYWORDS = 5

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

    Nothing but case and whitespace is touched. An earlier version replaced
    punctuation too, which is harmless for theme names but silently wrong for a
    keyword: ``nyest.hu`` became ``nyest-hu``, a directory Hugo would never look
    in.

    Args continued:
        The same rule serves both taxonomies, so there is one definition of
        "where does Hugo expect this term" rather than two that can drift.

    Example:
        >>> term_directory("Logika és matematika")
        'logika-és-matematika'
        >>> term_directory("A blog életéről")
        'a-blog-életéről'
        >>> term_directory("nyest.hu")
        'nyest.hu'
        >>> term_directory("gépi tanulás")
        'gépi-tanulás'
    """
    return "-".join(name.lower().split())


def _collect_orphans(
    approved_slugs: set[str], *, remove: bool, root: Path | None = None
) -> tuple[list[str], list[str]]:
    """Find hub directories no longer backed by an approved theme.

    Renaming a theme leaves its old directory behind, and a stale hub is a live
    URL listing nothing. Empty ones are deleted; **one carrying prose is never
    touched**, because that prose is the intro written by hand and losing it to
    a rename would be unforgivable. Those are reported instead.

    Args:
        approved_slugs: Term directory names that should exist.
        remove: Whether to delete the empty ones.
        root: Directory to scan. Defaults to the theme hubs.

    Returns:
        ``(removed, kept)`` slugs.
    """
    root = root or SITE / "content" / "temak"
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


def normalise_term(term: str) -> str:
    """Put a keyword into the composed form Hugo and the filesystem agree on.

    Typography that reaches the corpus from PDFs and old blog exports carries
    compatibility characters: the ligature in ``difﬁcult`` is a single
    codepoint, U+FB01. It is a letter, so it survives every word-like test, and
    it names a directory perfectly well — but Hugo percent-encodes it when it
    builds the term's URL, so the tag pointed at ``dif%EF%AC%81cult`` while the
    page sat at ``difﬁcult``. The tag 404'd and the build stayed green.

    NFKC folds those back to their plain equivalents, so the word joins the
    ordinary ``difficult`` rather than becoming a hub of its own.

    Args:
        term: The keyword as the analyser produced it.

    Returns:
        The normalised keyword.

    Example:
        >>> normalise_term("dif\ufb01cult")
        'difficult'
        >>> normalise_term("korpusz")
        'korpusz'
    """
    return unicodedata.normalize("NFKC", term)


def fold(term: str) -> str:
    """The accent-free lowercase form Hugo turns a term into for its URL.

    Args:
        term: The keyword.

    Returns:
        The folded form.

    Example:
        >>> fold("Médium"), fold("medium")
        ('medium', 'medium')
    """
    decomposed = unicodedata.normalize("NFKD", term.casefold())
    return "".join(c for c in decomposed if not unicodedata.combining(c))


def canonical_forms(counts: Mapping[str, int]) -> dict[str, str]:
    """Map every keyword variant onto the one spelling that gets the hub.

    Hugo strips case and accents when it builds a term's URL, so ``NLP`` and
    ``nlp``, or ``média`` and ``media``, resolve to the same address. Left
    alone, one of them silently wins the page and the other's writings vanish
    from it. Merging them here makes that explicit and keeps the counts true.

    The winner is the most frequent spelling; ties go to the one starting
    lowercase, which is usually the lemma rather than a sentence-initial
    accident, and then to alphabetical order so the result never depends on
    dictionary ordering.

    This merges by appearance, not by meaning. It is safe for the variants this
    corpus actually contains — every group is one word spelled two ways — but a
    Hungarian pair distinguished only by an accent would be merged wrongly, so
    the groups are printed when the export runs.

    Args:
        counts: How often each spelling occurs.

    Returns:
        Every spelling mapped to its canonical form.

    Example:
        >>> canonical_forms({"NLP": 13, "nlp": 1})
        {'NLP': 'NLP', 'nlp': 'NLP'}
        >>> canonical_forms({"Magyar": 2, "magyar": 13})["Magyar"]
        'magyar'
        >>> canonical_forms({"Media": 2, "média": 2})["Media"]
        'média'
    """
    groups: dict[str, list[str]] = defaultdict(list)
    for term in counts:
        groups[fold(term)].append(term)
    mapping: dict[str, str] = {}
    for members in groups.values():
        winner = min(
            members,
            key=lambda t: (-counts[t], not t[:1].islower(), t),
        )
        for term in members:
            mapping[term] = winner
    return mapping


def slugify(term: str) -> str:
    """The URL segment for a keyword hub.

    Accents are stripped and anything that is not a letter, digit or hyphen
    becomes one, so ``nyest.hu`` and ``C++`` survive as usable paths. Computed
    here and written into the data file rather than left to the template,
    because a slug this site does not control is a slug that changes under it.

    Args:
        term: The keyword.

    Returns:
        An ASCII slug, or ``""`` if nothing survives.

    Example:
        >>> slugify("korpusznyelvészet")
        'korpusznyelveszet'
        >>> slugify("nyest.hu")
        'nyest-hu'
        >>> slugify("gépi tanulás")
        'gepi-tanulas'
    """
    folded = unicodedata.normalize("NFKD", term.casefold())
    stripped = "".join(c for c in folded if not unicodedata.combining(c))
    cleaned = "".join(c if c.isalnum() else "-" for c in stripped)
    return "-".join(part for part in cleaned.split("-") if part)


def _external(document: Document) -> dict[str, object]:
    """One data-file row as a hub member."""
    return {
        "title": document.title,
        "year": document.year,
        "source": document.source,
        "url": document.url,
    }


def _member_lines(items: list[dict[str, object]], indent: str) -> list[str]:
    """Render external members as YAML, newest first."""
    lines: list[str] = []

    def newest_first(item: dict[str, object]) -> tuple[int, str]:
        year = item["year"]
        return (-int(year) if isinstance(year, int) else 0, str(item["title"]))

    for item in sorted(items, key=newest_first):
        lines.append(f"{indent}- cim: {quote(str(item['title']))}")
        lines.append(f"{indent}  ev: {item['year'] or 'null'}")
        lines.append(f"{indent}  forras: {quote(str(item['source']))}")
        if item["url"]:
            lines.append(f"{indent}  link: {quote(str(item['url']))}")
    return lines


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

    # Count every spelling first, so the canonical choice is made on the whole
    # corpus rather than on whichever document happened to come first.
    raw_counts: Counter[str] = Counter()
    for doc_id in assignments:
        raw_counts.update(
            normalise_term(k["term"]) for k in keywords.get(doc_id, [])[:N_KEYWORDS]
        )
    canonical = canonical_forms(raw_counts)
    merged = {
        winner: sorted(v for v, w in canonical.items() if w == winner and v != w)
        for winner in set(canonical.values())
    }
    merged = {w: v for w, v in merged.items() if v}
    if merged:
        print(f"  merged {len(merged)} keyword(s) that share a URL:")
        for winner, variants in sorted(merged.items())[:40]:
            print(f"    {winner} <- {', '.join(variants)}")

    pages = 0
    theme_members: dict[int, int] = dict.fromkeys(approved, 0)
    theme_externals: dict[int, list[dict[str, object]]] = {t: [] for t in approved}
    keyword_members: Counter[str] = Counter()
    page_terms: set[str] = set()
    keyword_externals: dict[str, list[dict[str, object]]] = defaultdict(list)
    index: dict[str, dict[str, list[str]]] = {}

    for doc_id, assignment in assignments.items():
        document = documents.get(doc_id)
        if document is None:
            continue
        theme_ids = [t for t in assignment["topics"] if int(t) in approved]
        themes = [approved[int(t)]["name"] for t in theme_ids]
        terms = list(
            dict.fromkeys(
                canonical[normalise_term(k["term"])]
                for k in keywords.get(doc_id, [])[:N_KEYWORDS]
            )
        )

        for topic_id in theme_ids:
            theme_members[int(topic_id)] += 1
        keyword_members.update(terms)

        if document.source in PAGE_SOURCES:
            page_terms.update(terms)
            path = SITE / doc_id
            text = path.read_text(encoding="utf-8")
            # The taxonomy front-matter keys are the plural forms, `temak` and
            # `kulcsszavak`. The empty `tema` entry clears an earlier singular
            # key that produced a clean build with no term pages at all.
            updated = update_front_matter(
                text, {"tema": [], "temak": themes, "kulcsszavak": terms}
            )
            if updated != text and not args.dry_run:
                path.write_text(updated, encoding="utf-8")
            pages += 1
        else:
            member = _external(document)
            for topic_id in theme_ids:
                theme_externals[int(topic_id)].append(member)
            for term in terms:
                keyword_externals[term].append(member)
            # Keyed by the row's own URL, falling back to the post that
            # announced it when the piece itself is gone. The doc_id would be
            # shorter, but it is the row's position in the file: it agrees with
            # the template's ordering today and would diverge silently the first
            # time the importer reorders a row, attaching tags to the wrong
            # writing with nothing to show for it.
            if document.key:
                index[document.key] = {"t": themes, "k": terms}

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
        # Every writing carrying the theme, not just the ones it leads. With
        # multi-label taxonomies these no longer partition the corpus, so the
        # counts across themes deliberately sum to more than the archive.
        lines.append(f"  darab: {theme_members[topic_id]}")
        lines.append("  kifejezesek:")
        lines.extend(f"    - {quote(term)}" for term in topic["terms"])
        first = topic["representative"][0] if topic["representative"] else None
        if first and first.get("quote"):
            lines.append("  idezet:")
            lines.append(f"    szoveg: {quote(first['quote'])}")
            lines.append(f"    forras: {quote(first['doc_id'])}")
        if theme_externals[topic_id]:
            lines.append("  kulsok:")
            lines.extend(_member_lines(theme_externals[topic_id], "    "))

    # A map rather than a list: with this many keywords a hub template that had
    # to scan a sequence would do it once per hub, which is quadratic.
    kw_lines = [
        "# Generated by analysis/scripts/export_temak.py — do not edit by hand.",
        "# Keyed by the keyword itself, so a hub is one lookup.",
    ]
    for term in sorted(keyword_members):
        kw_lines.append(f"{quote(term)}:")
        kw_lines.append(f"  slug: {quote(slugify(term))}")
        kw_lines.append(f"  darab: {keyword_members[term]}")
        if keyword_externals.get(term):
            kw_lines.append("  kulsok:")
            kw_lines.extend(_member_lines(keyword_externals[term], "    "))

    idx_lines = [
        "# Generated by analysis/scripts/export_temak.py — do not edit by hand.",
        "# The tags of every item that has no page of its own, keyed by its URL.",
    ]
    for url in sorted(index):
        idx_lines.append(f"{quote(url)}:")
        if index[url]["t"]:
            idx_lines.append("  t:")
            idx_lines.extend(f"    - {quote(name)}" for name in index[url]["t"])
        if index[url]["k"]:
            idx_lines.append("  k:")
            idx_lines.extend(f"    - {quote(term)}" for term in index[url]["k"])

    data_dir = SITE / "data"
    written = {
        data_dir / "temak.yaml": lines,
        data_dir / "kulcsszavak.yaml": kw_lines,
        data_dir / "temak_index.yaml": idx_lines,
    }
    stubs = 0
    keyword_stubs = 0
    removed: list[str] = []
    kept: list[str] = []
    if not args.dry_run:
        for path, content in written.items():
            path.write_text("\n".join(content) + "\n", encoding="utf-8")
        for entry in approved.values():
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
        theme_removed, theme_kept = _collect_orphans(
            {term_directory(entry["name"]) for entry in approved.values()},
            remove=True,
        )
        removed += [f"temak/{slug}" for slug in theme_removed]
        kept += [f"temak/{slug}" for slug in theme_kept]
        # A keyword carried only by items that have no page of their own would
        # otherwise have no term page either: Hugo builds taxonomy terms from
        # front matter, and a Kereső Világ link has none. Without these the tag
        # would render and lead nowhere, which is the one thing a tag must not
        # do.
        kw_root = SITE / "content" / "kulcsszavak"
        needed = {
            term_directory(term): term
            for term in keyword_members
            if term not in page_terms
        }
        for key, term in sorted(needed.items()):
            stub = kw_root / key / "_index.md"
            if stub.exists():
                continue
            stub.parent.mkdir(parents=True, exist_ok=True)
            stub.write_text(f"---\ntitle: {quote(term)}\n---\n\n", encoding="utf-8")
            keyword_stubs += 1
        kw_removed, kw_kept = _collect_orphans(set(needed), remove=True, root=kw_root)
        removed += [f"kulcsszavak/{slug}" for slug in kw_removed]
        kept += [f"kulcsszavak/{slug}" for slug in kw_kept]

    for slug in kept:
        print(f"  orphan hub kept, it has prose in it: content/{slug}/")
    for slug in removed:
        print(f"  removed empty orphan hub: content/{slug}/")

    verb = "would update" if args.dry_run else "updated"
    print(f"{verb} {pages} pages across {len(approved)} themes")
    print(f"  {len(keyword_members)} distinct keywords, {len(index)} external items")
    for path in written:
        size = len("\n".join(written[path])) / 1024
        print(f"  {verb} {path.relative_to(SITE)} ({size:.0f} KB)")
    print(f"  {stubs} new theme stubs, {keyword_stubs} new keyword stubs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
