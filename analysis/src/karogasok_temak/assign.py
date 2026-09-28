"""Place every writing in the corpus on the curated themes, the way the site shows it.

:mod:`placement` places one vector. This is the corpus-level step around it that
the export, the move list and ``infer.py`` all share, so that the three can
never disagree about where a writing belongs:

* a writing's length class decides which threshold it faces (``long`` from
  :data:`~karogasok_temak.corpus.MIN_FIT_WORDS` words up);
* a seed always carries the theme it defines;
* a writing the author labelled as a genre with no single subject — by default
  only ``lapszemle``, the link roundups — gets no theme at all, however close it
  happens to sit to one. A roundup of ten unrelated links has no subject; the
  similarity would only reflect which links dominate its text.

Nothing here decides a threshold: those are frozen in
``analysis/temalista_kalibracio.json``.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass

import numpy as np

from karogasok_temak.corpus import MIN_FIT_WORDS, Document
from karogasok_temak.placement import Calibration, place
from karogasok_temak.themes import Theme

#: Author labels that mark a writing as having no single subject. Changing this
#: changes which writings get a theme, so it is a parameter, not a constant
#: buried in a function. Compared case-insensitively.
SUBJECTLESS_LABELS: frozenset[str] = frozenset({"lapszemle"})


@dataclass(frozen=True)
class Assignment:
    """Where one writing landed, and why.

    Attributes:
        themes: Theme keys, strongest first; empty if none.
        scores: Similarity to each of those themes.
        best: The best similarity over all themes.
        role: ``"seed"``, ``"placed"``, ``"none"`` or ``"subjectless"``.
    """

    themes: tuple[str, ...]
    scores: tuple[float, ...]
    best: float
    role: str


def key_of(doc: Document) -> str:
    """The stable key of a writing: pages by path, data rows by their URL.

    Example:
        >>> key_of(Document("content/posts/a.md", "t", "x", "posts", 2026, True))
        'content/posts/a.md'
        >>> key_of(Document("kereses#3", "t", "x", "kereses", 2012, False,
        ...                 key="https://kereses.blog.hu/x"))
        'https://kereses.blog.hu/x'
    """
    if doc.source in ("archivum", "posts"):
        return doc.doc_id
    return doc.key or doc.doc_id


def length_class(doc: Document) -> str:
    """``"long"`` from :data:`MIN_FIT_WORDS` words up, else ``"short"``."""
    return "long" if doc.word_count >= MIN_FIT_WORDS else "short"


def seeds_by_writing(themes: Iterable[Theme]) -> dict[str, list[str]]:
    """Map each seed page to the active themes it defines.

    Example:
        >>> seeds_by_writing([Theme("a", "Alfa", magok=("p1", "p2")),
        ...                   Theme("b", "Béta", allapot="megszunt", magok=("p1",))])
        {'p1': ['a'], 'p2': ['a']}
    """
    out: dict[str, list[str]] = {}
    for theme in themes:
        if theme.allapot == "aktiv":
            for seed in theme.magok:
                out.setdefault(seed, []).append(theme.kulcs)
    return out


def is_subjectless(
    labels: Iterable[str], subjectless: frozenset[str] = SUBJECTLESS_LABELS
) -> bool:
    """Whether the author's own labels mark a writing as having no subject.

    Example:
        >>> is_subjectless(["Lapszemle", "nyelvészet"])
        True
        >>> is_subjectless(["nyelvészet"])
        False
    """
    wanted = {s.casefold() for s in subjectless}
    return any(label.casefold() in wanted for label in labels)


def assign_corpus(
    documents: Sequence[Document],
    vectors: np.ndarray,
    cal: Calibration,
    themes: Iterable[Theme],
    *,
    author_labels: Mapping[str, Iterable[str]],
    subjectless: frozenset[str] = SUBJECTLESS_LABELS,
) -> dict[str, Assignment]:
    """Place every writing.

    Args:
        documents: The writings, in the same order as ``vectors``.
        vectors: Their raw embeddings from the calibration's encoder.
        cal: The frozen calibration.
        themes: The whole theme list (retired entries are ignored).
        author_labels: The author's own labels, by :func:`key_of` key.
        subjectless: Labels that mean "no theme". Defaults to
            :data:`SUBJECTLESS_LABELS`.

    Returns:
        Each writing's :func:`key_of` key mapped to its assignment.

    Raises:
        ValueError: If ``documents`` and ``vectors`` differ in length.
    """
    if len(documents) != len(vectors):
        msg = f"{len(documents)} documents but {len(vectors)} vectors"
        raise ValueError(msg)
    seed_of = seeds_by_writing(themes)
    out: dict[str, Assignment] = {}
    for doc, vector in zip(documents, vectors, strict=True):
        key = key_of(doc)
        p = place(vector, length_class(doc), cal, seed_of=seed_of.get(key, ()))
        if p.role != "seed" and is_subjectless(author_labels.get(key, ()), subjectless):
            out[key] = Assignment((), (), p.best, "subjectless")
        else:
            out[key] = Assignment(p.themes, p.scores, p.best, p.role)
    return out
