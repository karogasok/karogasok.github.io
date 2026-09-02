"""The ISO-8859-1 trap, made into a test.

``requests`` guesses ISO-8859-1 for a ``text/plain`` response that does not
name its charset, which is exactly what emtsv returns. Decoding the body with
that guess turns every long vowel into mojibake and silently corrupts the whole
lemma stream, so this asserts the accented characters survive a real round trip.
"""

from __future__ import annotations

import pytest

from karogasok_temak.emtsv import analyse, lemmatize

from .conftest import needs_emtsv

#: Every Hungarian accent, including the two double acutes that only Hungarian
#: uses, in a sentence whose lemmas are unambiguous.
ACCENTED = "A hűtőgépben őrzött szőlőt tegnap megettük a fűtött kertben."


@needs_emtsv
def test_accents_survive_the_round_trip() -> None:
    tokens = analyse(ACCENTED)
    forms = [token.form for token in tokens]
    assert "hűtőgépben" in forms
    assert "szőlőt" in forms
    lemmas = [token.lemma for token in tokens]
    assert "hűtőgép" in lemmas
    assert "szőlő" in lemmas


@needs_emtsv
def test_no_mojibake_anywhere() -> None:
    """No token may contain a replacement char or a Latin-1 misread."""
    tokens = analyse(ACCENTED)
    blob = "".join(token.form + token.lemma for token in tokens)
    assert "�" not in blob
    for suspect in ("Å", "Ã", "±", "»"):
        assert suspect not in blob, f"{suspect!r} suggests a Latin-1 misread"


@needs_emtsv
def test_lemmatize_drops_function_words_and_normalises_morphology() -> None:
    lemmas = lemmatize(ACCENTED)
    assert "megeszik" in lemmas, "irregular past tense should lemmatise"
    assert "kert" in lemmas
    assert "a" not in lemmas, "the definite article is not a content word"


@needs_emtsv
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Nyelvi modellekről írtam.", "nyelvi"),
        ("A gépi tanulás mindent visz.", "tanulás"),
    ],
)
def test_known_lemmas(text: str, expected: str) -> None:
    assert expected in lemmatize(text)
