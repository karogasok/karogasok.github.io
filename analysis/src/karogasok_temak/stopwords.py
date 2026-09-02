"""Hungarian stopwords for parliamentary text, in three auditable groups.

The groups are kept separate rather than merged into one opaque blob so that
each can be inspected, edited and argued with on its own. Only
:func:`hungarian_stopwords` unions them.

Everything here is a **lemma**, because the list is applied after
:func:`parlamonitor.emtsv.lemmatize`. Inflected forms in :data:`SPACY_HU` are
harmless -- they simply never match.

This whole module changes the numbers. Every topic label depends on it.
"""

from __future__ import annotations

from collections.abc import Iterable

from spacy.lang.en.stop_words import STOP_WORDS as _SPACY_EN
from spacy.lang.hu.stop_words import STOP_WORDS as _SPACY_HU

SPACY_HU: frozenset[str] = frozenset(_SPACY_HU)
"""spaCy's Hungarian stopword list -- 219 entries, no model download needed.

Covers the closed classes and a few light verbs (``van``, ``kell``, ``lesz``)
but **not** ``tud``, ``mond``, ``beszél`` or ``gondol``, which is exactly why
:data:`LIGHT_VERBS` exists.
"""

LIGHT_VERBS: frozenset[str] = frozenset(
    {
        # Existential, modal and auxiliary
        "van",
        "volt",
        "lesz",
        "kell",
        "lehet",
        "szabad",
        "fog",
        "akar",
        "szeret",
        "kíván",
        # Saying and thinking -- the verbs a parliament uses to frame anything
        "mond",
        "elmond",
        "beszél",
        "szól",
        "gondol",
        "hisz",
        "vél",
        "ért",
        "érez",
        "tud",
        "ismer",
        "lát",
        "néz",
        "említ",
        "jelent",
        "tekint",
        "kérdez",
        "válaszol",
        "köszön",
        # Support verbs: carry almost no meaning without their object
        "tesz",
        "vesz",
        "ad",
        "kap",
        "kér",
        "hoz",
        "visz",
        "jön",
        "megy",
        "áll",
        "tart",
        "marad",
        "kerül",
        "csinál",
        "hagy",
        "kezd",
        "folytat",
        "próbál",
        "történik",
        # Procedural verbs the user asked to drop: frequent in every speech
        # regardless of subject, so they distinguish nothing.
    }
)
"""Light, modal and support verbs, as lemmas.

Nouns and adjectives survive the part-of-speech filter on their own merits;
verbs mostly do not. These are the ones that appear across every topic and so
separate none of them. Deliberately *not* included: ``szavaz``, ``elfogad``,
``elutasít``, ``módosít``, ``támogat`` -- speech-act verbs that genuinely mark
what a speech is doing.
"""

ENGLISH: frozenset[str] = frozenset(_SPACY_EN)
"""English function words.

Part of the archive is written in English, and emtsv analyses it as though it
were Hungarian — so ``in``, ``to``, ``which`` and ``I`` arrive as content-word
lemmas and two topics came back with English function words among their top
terms. This is not language detection, just a floor under the damage.
"""

BLOG: frozenset[str] = frozenset(
    {
        "poszt",
        "bejegyzés",
        "blog",
        "blogol",
        "lapszemle",
        "olvasó",
        "link",
        "hét",
        "cikk",
        "ajánl",
        "ajánló",
        "olvas",
        "ír",
    }
)
"""Blog furniture.

The residue of running a weekly reading blog for a decade: a "Lapszemle" is a
press review, and its 23 instalments would otherwise form a topic whose subject
is the format rather than anything written about. ``ír`` and ``olvas`` are here
for the same reason -- they are what every post is doing.

Deliberately *not* included: ``nyelv``, ``modell``, ``adat``, ``gép`` -- these
look generic in a corpus about computational linguistics and are in fact the
distinctions the topics are made of.
"""


def hungarian_stopwords(
    *,
    spacy: bool = True,
    light_verbs: bool = True,
    blog: bool = True,
    english: bool = True,
    extra: Iterable[str] = (),
) -> frozenset[str]:
    """Union the stopword groups, each switchable.

    Args:
        spacy: Include :data:`SPACY_HU`. Defaults to ``True``.
        light_verbs: Include :data:`LIGHT_VERBS`. Defaults to ``True``.
        blog: Include :data:`BLOG`. Defaults to ``True``.
        english: Include :data:`ENGLISH`, for the English-language
            posts in the archive. Defaults to ``True``.
        extra: Any further lemmas to drop.

    Returns:
        The union, as a frozenset of lemmas.

    Example:
        >>> stops = hungarian_stopwords()
        >>> {"tud", "tesz", "van", "lapszemle"} <= stops
        True
        >>> "költségvetés" in stops
        False

        Speech-act verbs are kept on purpose:

        >>> any(v in stops for v in ("szavaz", "elutasít", "módosít"))
        False

        English function words go too, because part of the archive is in
        English and the analyser treats it as Hungarian:

        >>> all(w in stops for w in ("which", "to", "or"))
        True

        Groups can be switched off individually:

        >>> "tud" in hungarian_stopwords(light_verbs=False)
        False
        >>> "which" in hungarian_stopwords(english=False)
        False
    """
    result: set[str] = set(extra)
    if spacy:
        result |= SPACY_HU
    if light_verbs:
        result |= LIGHT_VERBS
    if blog:
        result |= BLOG
    if english:
        result |= ENGLISH
    return frozenset(result)
