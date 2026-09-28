"""Write themes and keywords onto the site.

Reads the curated theme list (``temalista.yaml``), where every writing was
placed (``out/placement.json``, written by ``infer.py``) and ``out/keywords.json``,
then:

* adds ``temak`` and ``kulcsszavak`` to the front matter of the pages the site
  owns, leaving every other line untouched;
* writes ``data/temak.yaml`` and ``data/kulcsszavak.yaml``, each carrying the
  hub's metadata **and** its external members — Kereső Világ leads, media and
  máshol entries — because those have no page of their own to hold front
  matter;
* writes ``data/temak_index.yaml``, the tags of every external item keyed by
  its URL, so the archive, máshol and média lists can show them;
* keeps a ``content/temak/<term>/_index.md`` for each active theme, whose
  ``aliases`` redirect every former name's URL to it;
* redirects each retired theme's URL to the page named in its ``atiranyitas``,
  through an alias on that page's term file;
* appends every theme URL it publishes to ``data/tema_slugok.txt``, the
  registry ``check_build.sh`` uses to make sure no theme URL ever dies.

Every writing carries the themes it was placed on (at most three, strongest
first) and its strongest :data:`N_KEYWORDS` keywords.

Usage:
    uv run python scripts/export_temak.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from collections import Counter, defaultdict
from collections.abc import Mapping
from pathlib import Path

from karogasok_temak import themes as theme_list
from karogasok_temak.assign import key_of
from karogasok_temak.corpus import SITE, Document, load_corpus
from karogasok_temak.frontmatter import quote, update_front_matter
from karogasok_temak.themes import Theme

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "out"
REGISTRY = SITE / "data" / "tema_slugok.txt"

#: Keywords written onto each item. Five is what fits a line of metadata under
#: a title without the tags outweighing the thing they describe.
N_KEYWORDS = 5

#: Sources whose items are pages on this site; everything else is external.
PAGE_SOURCES = frozenset({"archivum", "posts"})


def _load(name: str) -> dict:
    """Read a JSON artefact, failing with a usable message."""
    path = OUT / name
    if not path.exists():
        msg = f"{path} missing — run scripts/infer.py first"
        raise SystemExit(msg)
    return json.loads(path.read_text(encoding="utf-8"))


def _stub(path: Path, fields: dict[str, str | list[str]]) -> bool:
    """Write a term page's front matter, keeping any prose below it.

    A hub's intro is written by hand, so it must survive every export: only the
    front matter is rewritten. Returns whether the file changed.
    """
    body = ""
    if path.exists():
        text = path.read_text(encoding="utf-8")
        body = text.partition("---\n")[2].partition("---\n")[2]
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            if value:
                lines.append(f"{key}:")
                lines.extend(f"  - {quote(v)}" for v in value)
        else:
            lines.append(f"{key}: {quote(value)}")
    lines.append("---")
    text_new = "\n".join(lines) + "\n" + (body or "\n")
    if path.exists() and path.read_text(encoding="utf-8") == text_new:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text_new, encoding="utf-8")
    return True


def theme_aliases(theme: Theme) -> list[str]:
    """The URLs of a theme's former names, which must now lead to it.

    Example:
        >>> theme_aliases(Theme("s", "Statisztika és valószínűség",
        ...                     korabbi_nevek=("Statisztika és R",)))
        ['/tema/statisztika-es-r/']
    """
    own = slugify(theme.nev)
    return sorted(
        {f"/tema/{slugify(n)}/" for n in theme.korabbi_nevek if slugify(n) != own}
    )


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


def _is_acronym(term: str) -> bool:
    """Two or more letters, all of them capitals: ``LLM``, ``API``, ``NLTK``."""
    letters = [c for c in term if c.isalpha()]
    return len(letters) >= 2 and all(c.isupper() for c in letters)


def canonical_forms(counts: Mapping[str, int]) -> dict[str, str]:
    """Map every keyword variant onto the one spelling that gets the hub.

    Hugo strips case and accents when it builds a term's URL, so ``NLP`` and
    ``nlp``, or ``média`` and ``media``, resolve to the same address. Left
    alone, one of them silently wins the page and the other's writings vanish
    from it. Merging them here makes that explicit and keeps the counts true.

    An all-capitals acronym wins whenever it is among the spellings: ``LLM`` is
    how the word is written, even where the author once typed ``llm``. Otherwise
    the most frequent spelling wins; ties go to the one starting lowercase, which
    is usually the lemma rather than a sentence-initial accident, and then to
    alphabetical order so the result never depends on dictionary ordering.

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
        >>> canonical_forms({"llm": 5, "LLM": 1})["llm"]
        'LLM'
    """
    groups: dict[str, list[str]] = defaultdict(list)
    for term in counts:
        groups[fold(term)].append(term)
    mapping: dict[str, str] = {}
    for members in groups.values():
        winner = min(
            members,
            key=lambda t: (not _is_acronym(t), -counts[t], not t[:1].islower(), t),
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


def main() -> int:  # noqa: C901, PLR0912, PLR0915
    """Write themes and keywords onto the site."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    all_themes = theme_list.load(HERE / "temalista.yaml")
    active = [t for t in all_themes if t.allapot == "aktiv"]
    retired = [t for t in all_themes if t.allapot == "megszunt"]
    by_key = {t.kulcs: t for t in active}
    placement = _load("placement.json")["placement"]
    keywords = _load("keywords.json")
    documents = [d for d in load_corpus() if d.text.strip()]

    # Count every spelling first, so the canonical choice is made on the whole
    # corpus rather than on whichever document happened to come first.
    raw_counts: Counter[str] = Counter()
    for document in documents:
        raw_counts.update(
            normalise_term(k["term"]) for k in keywords.get(document.doc_id, [])
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
    theme_members: Counter[str] = Counter()
    theme_externals: dict[str, list[dict[str, object]]] = {t.kulcs: [] for t in active}
    keyword_members: Counter[str] = Counter()
    page_terms: set[str] = set()
    keyword_externals: dict[str, list[dict[str, object]]] = defaultdict(list)
    index: dict[str, dict[str, list[str]]] = {}

    for document in documents:
        placed = placement.get(key_of(document), {}).get("temak", [])
        unknown = [k for k in placed if k not in by_key]
        if unknown:
            msg = f"{document.doc_id}: placed on unknown theme(s) {unknown}"
            raise SystemExit(msg + " — re-run scripts/infer.py")
        themes = [by_key[k].nev for k in placed]
        # Merge spellings first, then cut: two spellings of one word must not use
        # up two of the five places.
        terms = list(
            dict.fromkeys(
                canonical[normalise_term(k["term"])]
                for k in keywords.get(document.doc_id, [])
            )
        )[:N_KEYWORDS]

        theme_members.update(placed)
        keyword_members.update(terms)

        if document.source in PAGE_SOURCES:
            page_terms.update(terms)
            path = SITE / document.doc_id
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
            for kulcs in placed:
                theme_externals[kulcs].append(member)
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
        "# The curated themes (analysis/temalista.yaml), with the writings that",
        "# have no page of their own. Placement: see /modszer/.",
    ]
    for theme in active:
        lines.append(f"- kulcs: {quote(theme.kulcs)}")
        lines.append(f"  nev: {quote(theme.nev)}")
        lines.append(f"  slug: {quote(slugify(theme.nev))}")
        if theme.leiras:
            lines.append(f"  leiras: {quote(theme.leiras)}")
        # Every writing carrying the theme, not just the ones it leads. With
        # multi-label taxonomies these no longer partition the corpus, so the
        # counts across themes deliberately sum to more than the archive.
        lines.append(f"  darab: {theme_members[theme.kulcs]}")
        if theme_externals[theme.kulcs]:
            lines.append("  kulsok:")
            lines.extend(_member_lines(theme_externals[theme.kulcs], "    "))

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

    # Every theme URL this export makes live — hubs and redirects alike. The
    # registry only ever grows, so a URL published once stays checked forever.
    published = {slugify(t.nev) for t in active}
    for theme in active:
        published.update(a.strip("/").split("/")[-1] for a in theme_aliases(theme))
    for theme in retired:
        published.update(slugify(n) for n in (theme.nev, *theme.korabbi_nevek))
    registry = (
        set(REGISTRY.read_text(encoding="utf-8").split())
        if REGISTRY.exists()
        else set()
    )

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
        REGISTRY.write_text(
            "# Every /tema/<slug>/ URL ever published. check_build.sh requires each\n"
            "# to build, as a hub or as a redirect. Append only.\n"
            + "\n".join(sorted(registry | published))
            + "\n",
            encoding="utf-8",
        )
        for theme in active:
            # Term pages live under the plural name, in the directory Hugo
            # derives from the term itself — accents and all. The slug is
            # explicit for the same reason every archive post's is: Hugo derives
            # it from the title, which here would keep the accents.
            stub = SITE / "content" / "temak" / term_directory(theme.nev) / "_index.md"
            stubs += _stub(
                stub,
                {
                    "title": theme.nev,
                    "slug": slugify(theme.nev),
                    "aliases": theme_aliases(theme),
                },
            )
        for theme in retired:
            # The destination is an old-label hub, a term page of its own. An
            # alias on its term file turns the retired theme's URL into a
            # redirect; the file sets nothing else, so the hub keeps its title.
            if not theme.atiranyitas:
                continue
            segment = theme.atiranyitas.strip("/").split("/")[-1]
            target = SITE / "content" / "regi_cimkek" / segment / "_index.md"
            aliases = sorted(
                {f"/tema/{slugify(n)}/" for n in (theme.nev, *theme.korabbi_nevek)}
            )
            stubs += _stub(target, {"aliases": aliases})
        theme_removed, theme_kept = _collect_orphans(
            {term_directory(t.nev) for t in active}, remove=True
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
    print(f"{verb} {pages} pages across {len(active)} themes")
    print(f"  {len(keyword_members)} distinct keywords, {len(index)} external items")
    for path in written:
        size = len("\n".join(written[path])) / 1024
        print(f"  {verb} {path.relative_to(SITE)} ({size:.0f} KB)")
    print(
        f"  {stubs} theme/redirect stub(s) written, {keyword_stubs} new keyword stubs"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
