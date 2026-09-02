"""Per-document keywords, as keyness against the rest of the corpus.

There is no separate keyword-extraction model here. A keyword is simply a lemma
this document uses far more than the other documents do, which is exactly what
:mod:`keyflux` measures. The focus counts are one document; the reference counts
are the whole corpus minus that document.

Working on emtsv lemmas rather than surface forms matters more in Hungarian than
it would in English: *metaforát*, *metaforák*, *metaforáról* are one keyword,
and only lemmatisation makes them count as three occurrences of one thing
instead of one occurrence of three.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass

#: Keyness measure. Simple Maths is frequency-aware and, unlike log-likelihood,
#: does not reward a term purely for being common.
MEASURE = "simple_maths"

#: How often a lemma must occur *in the document* to be eligible.
#:
#: keyflux defaults to 5, which suits corpus-against-corpus comparison. Against
#: a single blog post of a few hundred words a lemma used five times is already
#: the title subject, so the floor drops to 2 — appearing twice is the weakest
#: evidence that a word is not a typo or an aside. This changes the output and
#: is recorded in ``CHANGES_SUMMARY.md``.
#:
#: It is applied in this module rather than passed to keyflux. keyflux's
#: documented contract is that a type is scored if
#: ``focus_count >= min_focus_freq`` **or**
#: ``reference_count >= min_reference_freq`` — an OR, so the usual
#: ``min_reference_freq=0`` makes the focus floor vacuous: every type
#: trivially has a reference count of at least zero.
MIN_FOCUS_FREQ = 2

#: Keywords kept per document.
TOP_N = 8


@dataclass(frozen=True)
class Keyword:
    """One keyword with the numbers that produced it.

    Attributes:
        term: The lemma.
        score: Simple Maths keyness score.
        effect_size: Log ratio against the reference.
        count: Occurrences in this document.
    """

    term: str
    score: float
    effect_size: float
    count: int


def corpus_counts(lemma_docs: Sequence[Sequence[str]]) -> Counter[str]:
    """Total lemma counts across every document.

    Args:
        lemma_docs: One lemma list per document.

    Returns:
        The summed counts.

    Example:
        >>> dict(corpus_counts([["nyelv", "nyelv"], ["gép", "nyelv"]]))
        {'nyelv': 3, 'gép': 1}
    """
    totals: Counter[str] = Counter()
    for lemmas in lemma_docs:
        totals.update(lemmas)
    return totals


def document_keywords(
    lemmas: Sequence[str],
    totals: Counter[str],
    *,
    top_n: int = TOP_N,
    min_focus_freq: int = MIN_FOCUS_FREQ,
) -> list[Keyword]:
    """Rank one document's lemmas against the rest of the corpus.

    The reference is ``totals`` minus this document, so a document is never
    compared against itself — with a few hundred documents, leaving itself in
    the reference measurably flattens its own keywords.

    Args:
        lemmas: This document's lemmas.
        totals: Corpus-wide counts from :func:`corpus_counts`, *including* this
            document.
        top_n: How many keywords to keep. Defaults to :data:`TOP_N`.
        min_focus_freq: Occurrence floor. Defaults to :data:`MIN_FOCUS_FREQ`.

    Returns:
        Keywords, strongest first. Empty if the document is too short for any
        lemma to clear the floor — which is the honest answer for a 20-word
        blurb, not a failure.

    Example:
        >>> totals = corpus_counts([
        ...     ["metafora"] * 4 + ["nyelv"] * 3,
        ...     ["kutya"] * 30 + ["nyelv"] * 20,
        ...     ["ház"] * 30 + ["nyelv"] * 20,
        ... ])
        >>> kws = document_keywords(["metafora"] * 4 + ["nyelv"] * 3, totals)
        >>> kws[0].term, kws[0].count
        ('metafora', 4)
        >>> document_keywords(["egy", "rövid", "szöveg"], totals)
        []
    """
    from keyflux import Keyness

    focus = Counter(lemmas)
    if not focus:
        return []
    reference = totals - focus
    rows = (
        Keyness(
            focus,
            reference,
            measure=MEASURE,
            min_focus_freq=min_focus_freq,
            min_reference_freq=0,
        )
        .keywords(top=None)
        .positive()
    )
    rows = sorted(
        (row for row in rows if row.focus_count >= min_focus_freq),
        key=lambda row: row.score,
        reverse=True,
    )
    return [
        Keyword(
            term=row.type,
            score=float(row.score),
            effect_size=float(row.effect_size),
            count=int(row.focus_count),
        )
        for row in rows[:top_n]
    ]
