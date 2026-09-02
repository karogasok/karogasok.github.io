"""Read the site's writings into documents, keeping provenance.

The corpus is not uniform and pretending otherwise would wreck the topic model.
It has four sources with wildly different lengths:

===================================  =====  ==============
source                                docs  median words
===================================  =====  ==============
``content/archivum/`` (own posts)      364             414
``content/posts/``                       2             113
Kereső Világ leads                     399              37
Máshol / Média descriptions             47              15
===================================  =====  ==============

Only the first two are full text. The rest are blurbs an order of magnitude
shorter, and they belong to somebody else in the Kereső Világ case. So
:func:`load_corpus` marks each document ``fittable`` or not: the model is fitted
on full text and the blurbs are assigned to the resulting topics afterwards.
Fitting on a corpus where more than half the documents are 37-word summaries
would let the summaries decide what the themes are.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

SITE = Path(__file__).resolve().parents[3]

#: Below this, a document has no topic signal worth modelling. The archive holds
#: 28 such posts; "Nyelvi modellek" is two words long.
MIN_FIT_WORDS = 80

_FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
_CODE_FENCE = re.compile(r"```.*?```", re.S)
_IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_TAG = re.compile(r"<[^>]+>")
# Emphasis markers are punctuation, but emtsv tokenises "**Hírek" as one token
# and it then reaches the topic terms looking like a word. Link-roundup posts
# are full of them, so two whole topics came back named after bold markers.
_EMPHASIS = re.compile(r"[*]+")
# Markdown structure at the start of a line: headings, quotes, list bullets.
_LINE_MARKER = re.compile(r"(?m)^[ \t]{0,3}(?:[#>]+|[-+*])[ \t]+")
# Leftovers of a URL that survived link stripping — percent-encoded fragments
# and bare filenames. "%25255BUNSET%25255D.jpg" was a topic term.
_URL_JUNK = re.compile(
    r"\S*%[0-9A-Fa-f]{2}\S*|\S+\.(?:jpg|jpeg|png|gif|webp|svg|pdf)\b",
    re.I,
)


@dataclass(frozen=True)
class Document:
    """One item of writing, with enough provenance to write results back.

    Attributes:
        doc_id: Stable identifier. For a page this is its content path relative
            to the site root; for a data-file row it is ``<file>:<index>``.
        title: The headline.
        text: Plain text, markup stripped.
        source: ``archivum``, ``posts``, ``kereses``, ``mashol`` or ``media``.
        year: Publication year, or ``None`` where the source has no date.
        fittable: Whether this document is long enough and ours to fit on.
        url: Where the piece lives, for data-file rows that have no page on
            this site. ``None`` for pages, whose URL Hugo derives itself.
    """

    doc_id: str
    title: str
    text: str
    source: str
    year: int | None
    fittable: bool
    url: str | None = None

    @property
    def word_count(self) -> int:
        """Number of whitespace-separated tokens.

        Example:
            >>> Document("d", "t", "egy két három", "posts", 2026, True).word_count
            3
        """
        return len(self.text.split())


def strip_markup(markdown: str) -> str:
    r"""Reduce Markdown body text to plain prose.

    Code fences, images and raw HTML go; link text is kept and the URL dropped,
    because the anchor words are part of the sentence and the URL is not.

    Args:
        markdown: A post body, front matter already removed.

    Returns:
        Single-spaced plain text.

    Example:
        >>> strip_markup("Lásd [ezt](http://a.b) és <b>ezt</b>.")
        'Lásd ezt és ezt.'
        >>> strip_markup("Szöveg\n\n```\nkód\n```\n\nmég szöveg")
        'Szöveg még szöveg'
        >>> strip_markup("## **Hírek** a hétről")
        'Hírek a hétről'
        >>> strip_markup("Kép: %25255BUNSET%25255D.jpg itt.")
        'Kép: itt.'
    """
    text = _CODE_FENCE.sub(" ", markdown)
    text = _IMAGE.sub(" ", text)
    text = _LINK.sub(r"\1", text)
    text = _TAG.sub(" ", text)
    text = _URL_JUNK.sub(" ", text)
    text = _LINE_MARKER.sub("", text)
    text = _EMPHASIS.sub("", text)
    text = re.sub(r"\s+", " ", text)
    # Removing an inline tag leaves a space in front of whatever followed it,
    # so "<b>ezt</b>." becomes "ezt .". Harmless for the model, but it puts
    # stray tokens in front of the lemmatiser and looks like a bug in any
    # quote we later show the reader.
    text = re.sub(r"\s+([,.;:!?…])", r"\1", text)
    return text.strip()


def _front_matter_value(front: str, key: str) -> str | None:
    match = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', front, re.M)
    return match.group(1) if match else None


def _read_page(path: Path, source: str) -> Document | None:
    raw = path.read_text(encoding="utf-8")
    match = _FRONT_MATTER.match(raw)
    if match is None:
        return None
    front, body = match.group(1), raw[match.end() :]
    title = _front_matter_value(front, "title") or path.stem
    date = _front_matter_value(front, "date") or ""
    year = int(date[:4]) if date[:4].isdigit() else None
    text = strip_markup(body)
    return Document(
        doc_id=str(path.relative_to(SITE)),
        title=title,
        text=text,
        source=source,
        year=year,
        fittable=len(text.split()) >= MIN_FIT_WORDS,
    )


def _read_yaml_rows(path: Path, source: str, key: str) -> list[Document]:
    """Pull title/description rows out of a data file without a YAML parser.

    The data files are generated with a fixed two-space shape, so a regex is
    enough and keeps this module importable before ``uv sync`` has run.
    """
    if not path.exists():
        return []
    raw = path.read_text(encoding="utf-8")
    docs: list[Document] = []
    blocks = re.split(r"\n  - ", raw)[1:]
    for index, block in enumerate(blocks):
        title = re.search(r'cim: "(.*?)"', block)
        body = re.search(rf'{key}: "(.*?)"', block)
        if title is None:
            continue
        year = re.search(r"(?:ev|datum): (\d{4})", block)
        link = re.search(r'link: "(.*?)"', block)
        text = f"{title.group(1)}. {body.group(1) if body else ''}".strip()
        docs.append(
            Document(
                doc_id=f"{path.name}:{index}",
                title=title.group(1),
                text=text,
                source=source,
                year=int(year.group(1)) if year else None,
                # Blurbs are never fitted on: too short, and in the Kereső Világ
                # case not ours to let define a theme.
                fittable=False,
                url=link.group(1) if link else None,
            )
        )
    return docs


def load_corpus(site: Path | None = None) -> list[Document]:
    """Load every document on the site.

    Args:
        site: Site root. Defaults to the repository containing this package.

    Returns:
        Documents in a stable order: pages first, then data rows.

    Raises:
        FileNotFoundError: If the site has no ``content`` directory.
    """
    root = site or SITE
    if not (root / "content").is_dir():
        raise FileNotFoundError(f"no content/ under {root}")

    docs: list[Document] = []
    for source in ("archivum", "posts"):
        for path in sorted((root / "content" / source).glob("*.md")):
            if path.name == "_index.md":
                continue
            page = _read_page(path, source)
            if page is not None and page.text:
                docs.append(page)

    docs += _read_yaml_rows(root / "data" / "kereses.yaml", "kereses", "lead")
    docs += _read_yaml_rows(root / "data" / "mashol.yaml", "mashol", "leiras")
    docs += _read_yaml_rows(root / "data" / "media.yaml", "media", "leiras")
    return docs
