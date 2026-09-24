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
from collections.abc import Collection, Iterable, Sequence
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


#: Hungarian case, plural and possessive endings that the analyser leaves attached
#: behind a hyphen when the stem is an acronym, a name or a foreign word:
#: ``LLM-ek``, ``API-hoz``, ``Facebook-on``. A closed list, so a real compound
#: such as ``Turing-teszt`` or ``e-könyv`` is never mistaken for one.
HYPHEN_SUFFIXES: frozenset[str] = frozenset(
    {
        "t",
        "et",
        "at",
        "ot",
        "öt",
        "k",
        "ek",
        "ak",
        "ok",
        "ök",
        "ben",
        "ban",
        "ről",
        "ról",
        "nak",
        "nek",
        "val",
        "vel",
        "hoz",
        "hez",
        "höz",
        "ra",
        "re",
        "ba",
        "be",
        "ból",
        "ből",
        "tól",
        "től",
        "on",
        "en",
        "ön",
        "n",
        "nál",
        "nél",
        "ig",
        "ként",
        "é",
        "ja",
        "je",
    }
)

#: Short lowercase ASCII lemmas that are Hungarian words rather than debris.
#: Everything else of two letters or fewer — English function words the
#: analyser does not know (``to``, ``it``, ``or``; ``bu`` from *but*, ``vi`` from
#: *vibe*), stray letters, abbreviation fragments — carries no subject.
SHORT_WORDS: frozenset[str] = frozenset({"ad", "fa", "ma", "ok"})


def _is_ending(ending: str) -> bool:
    """Whether ``ending`` is one closed-list ending, or two stacked."""
    if ending in HYPHEN_SUFFIXES:
        return True
    return any(
        ending[:i] in HYPHEN_SUFFIXES and ending[i:] in HYPHEN_SUFFIXES
        for i in range(1, len(ending))
    )


def normalise_lemma(lemma: str) -> str | None:
    """Clean one lemma before it can become a keyword.

    Two repairs, applied until nothing changes:

    1. A Hungarian ending attached with a hyphen — one from
       :data:`HYPHEN_SUFFIXES`, or two of them stacked, as in *-eket* — is
       removed when the stem is an
       acronym, contains a digit, or is plain ASCII: ``LLM-ek`` → ``LLM``. For
       an all-lowercase stem the ending ``-on`` is left alone, because English
       compounds end that way (*hands-on*, *add-on*).
    2. A lowercase ASCII lemma of two characters or fewer is dropped unless it
       is in :data:`SHORT_WORDS`. Uppercase ones such as ``R`` or ``AI`` stay;
       accented Hungarian words such as *év* or *nő* are not ASCII and stay too.

    Args:
        lemma: A lemma as the analyser produced it.

    Returns:
        The cleaned lemma, or ``None`` if it should not be a keyword.

    Example:
        >>> [normalise_lemma(x) for x in ("LLM-ek", "Facebook-on", "API-hoz")]
        ['LLM', 'Facebook', 'API']

        Endings stack — a plural and then a case:

        >>> [normalise_lemma(x) for x in ("LLM-eket", "API-kban", "GPU-knak")]
        ['LLM', 'API', 'GPU']
        >>> [normalise_lemma(x) for x in ("Turing-teszt", "hands-on", "e-könyv")]
        ['Turing-teszt', 'hands-on', 'e-könyv']
        >>> [normalise_lemma(x) for x in ("bu", "vi", "to", "ad", "R", "év")]
        [None, None, None, 'ad', 'R', 'év']
    """
    current = lemma
    while True:
        stem, dash, ending = current.rpartition("-")
        if not dash or not stem or not _is_ending(ending):
            break
        foreign = any(c.isupper() or c.isdigit() for c in stem) or stem.isascii()
        english_particle = ending == "on" and stem.isascii() and stem.islower()
        if not foreign or english_particle:
            break
        current = stem
    if current.isascii() and current.islower() and len(current) <= 2:
        return current if current in SHORT_WORDS else None
    return current or None


def keyword_lemmas(words: Iterable[str], stopwords: Collection[str]) -> list[str]:
    """The lemmas of one writing that are allowed to become keywords.

    Each lemma is cleaned by :func:`normalise_lemma` first, and only then tested
    against the stopword list and :func:`~karogasok_temak.topics.is_wordlike`, so
    ``LLM-ek`` counts as ``LLM`` rather than as a word of its own. The corpus
    counts and every single writing's counts go through here, so a keyword and
    the reference it is measured against are always cleaned the same way.

    Args:
        words: The writing's lemmas, as the analyser produced them.
        stopwords: Lemmas never to use, lowercased.

    Returns:
        The kept lemmas, in order, duplicates included.

    Example:
        >>> keyword_lemmas(["LLM-ek", "a", "bu", "nyelv", "LLM"], {"a"})
        ['LLM', 'nyelv', 'LLM']
    """
    from karogasok_temak.topics import is_wordlike

    kept: list[str] = []
    for word in words:
        clean = normalise_lemma(word)
        if clean and clean.casefold() not in stopwords and is_wordlike(clean):
            kept.append(clean)
    return kept


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
