"""Grounding a proposed topic name in something a human can check.

A topic name is a judgement call, and judgement calls need evidence attached.
Every name this pipeline proposes ships with the topic's top terms and a
**verbatim sentence** from a real document in that topic, so verifying it is a
string match against the source rather than a reread of the whole corpus.

The awkward part is Hungarian morphology. Topic terms are lemmas, and a lemma
usually does not appear in running text in that form: the topic term is
``metafora`` while the post says *metaforákról*. Matching on equality would
find almost nothing, so matching is done on a prefix — long enough that
``nyelv`` does not swallow ``nyelvész``, short enough that case endings do not
break it.
"""

from __future__ import annotations

import re
from collections.abc import Iterable, Sequence

#: Shortest prefix used when matching a surface form against a lemma. Below
#: four characters, common Hungarian stems collide badly.
MIN_PREFIX = 5

#: Longest quote to keep, in characters.
MAX_QUOTE_CHARS = 260

_SENTENCE_END = re.compile(r"(?<=[.!?…])\s+")
_WORD = re.compile(r"\w+", re.UNICODE)


def matches_lemma(surface: str, lemma: str, *, min_prefix: int = MIN_PREFIX) -> bool:
    """Whether an inflected surface form plausibly realises ``lemma``.

    The comparison is case-insensitive and prefix-based: the surface form must
    begin with the lemma, or — for lemmas longer than ``min_prefix`` — with the
    lemma's first ``min_prefix`` characters.

    Compounds therefore match their parts, so ``adat`` finds *adatbázisról*.
    That is wanted here: a sentence about databases really is evidence for a
    topic about data. The cost is that a lemma of one or two characters would
    match almost anything, which is tolerable only because topic terms come
    from a stopword-filtered content-word vocabulary where such lemmas do not
    survive.

    Args:
        surface: A word as it appears in the text.
        lemma: The lemma to match.
        min_prefix: Prefix length for long lemmas. Defaults to
            :data:`MIN_PREFIX`.

    Returns:
        Whether they plausibly match.

    Example:
        >>> matches_lemma("metaforákról", "metafora")
        True
        >>> matches_lemma("nyelvészetben", "nyelv")
        True
        >>> matches_lemma("adatbázisról", "adat")
        True
        >>> matches_lemma("nyelvtan", "gép")
        False
        >>> matches_lemma("Gépi", "gépi")
        True
    """
    surface = surface.casefold()
    lemma = lemma.casefold()
    if not lemma or not surface:
        return False
    if len(lemma) <= min_prefix:
        return surface.startswith(lemma)
    return surface.startswith(lemma[:min_prefix])


def split_sentences(text: str) -> list[str]:
    """Split prose into sentences on terminal punctuation.

    Deliberately naive — it is choosing a quote, not parsing. Hungarian
    abbreviations and ordinals ("1848. évi") will occasionally split early,
    which costs a shorter quote and nothing else.

    Args:
        text: Plain prose.

    Returns:
        Non-empty, stripped sentences.

    Example:
        >>> split_sentences("Első mondat. Második! Harmadik?")
        ['Első mondat.', 'Második!', 'Harmadik?']
        >>> split_sentences("   ")
        []
    """
    return [part.strip() for part in _SENTENCE_END.split(text) if part.strip()]


def score_sentence(sentence: str, terms: Iterable[str]) -> int:
    """Count how many distinct topic terms a sentence realises.

    Args:
        sentence: The candidate.
        terms: Topic terms, as lemmas.

    Returns:
        The number of distinct terms found.

    Example:
        >>> score_sentence("A metaforák a nyelvben élnek.", ["metafora", "nyelv"])
        2
        >>> score_sentence("Semmi köze hozzá.", ["metafora"])
        0
    """
    surfaces = _WORD.findall(sentence)
    return sum(
        1 for term in set(terms) if any(matches_lemma(s, term) for s in surfaces)
    )


def evidence_quote(
    text: str,
    terms: Sequence[str],
    *,
    max_chars: int = MAX_QUOTE_CHARS,
) -> str | None:
    """Pick the sentence that best shows why a document sits in a topic.

    Ties are broken towards the earlier sentence, which tends to be the more
    expository one. Sentences longer than ``max_chars`` are skipped rather than
    truncated, because a truncated quote is no longer verbatim and the whole
    point is that it can be found in the source with a string search.

    Args:
        text: The document's plain text.
        terms: Topic terms, as lemmas.
        max_chars: Longest acceptable quote. Defaults to
            :data:`MAX_QUOTE_CHARS`.

    Returns:
        The best sentence, or ``None`` if no sentence of usable length
        contains any topic term.

    Example:
        >>> text = "Bevezető mondat. A metafora a nyelv szerkezetét mutatja."
        >>> evidence_quote(text, ["metafora", "nyelv"])
        'A metafora a nyelv szerkezetét mutatja.'
        >>> evidence_quote("Nincs itt semmi.", ["metafora"]) is None
        True
    """
    best: tuple[int, str] | None = None
    for sentence in split_sentences(text):
        if len(sentence) > max_chars:
            continue
        score = score_sentence(sentence, terms)
        if score and (best is None or score > best[0]):
            best = (score, sentence)
    return None if best is None else best[1]
