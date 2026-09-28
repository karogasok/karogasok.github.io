"""Contracts for corpus-level placement: seeds and subject-less writings."""

from __future__ import annotations

import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st

from karogasok_temak.assign import assign_corpus
from karogasok_temak.corpus import Document
from karogasok_temak.placement import Calibration
from karogasok_temak.themes import Theme

from .test_placement import DIM, calibrations, vectors


def _doc(i: int, words: int) -> Document:
    return Document(
        f"content/archivum/{i}.md", "t", "szó " * words, "archivum", 2012, True
    )


@given(
    cal=calibrations(),
    raw=st.lists(vectors, min_size=3, max_size=3),
    words=st.integers(0, 300),
)
def test_seed_keeps_its_theme_and_roundup_gets_none(
    cal: Calibration, raw: list[np.ndarray], words: int
) -> None:
    docs = [_doc(i, words) for i in range(3)]
    seed = docs[0].doc_id
    themes = [Theme(cal.theme_keys[0], "Alfa", magok=(seed, "x", "y"))]
    labels = {docs[1].doc_id: ["Lapszemle"], seed: ["lapszemle"]}
    out = assign_corpus(docs, np.array(raw), cal, themes, author_labels=labels)
    # A seed carries its theme even if it is also labelled as a roundup.
    assert cal.theme_keys[0] in out[seed].themes
    assert out[seed].role == "seed"
    # A roundup that is not a seed gets nothing, however close it sits.
    assert out[docs[1].doc_id].themes == ()
    assert out[docs[1].doc_id].role == "subjectless"
    # Never more themes than the cap, never a repeated theme.
    for a in out.values():
        assert len(a.themes) <= cal.cap
        assert len(set(a.themes)) == len(a.themes)


def test_mismatched_lengths_fail_loudly() -> None:
    cal = Calibration(
        np.zeros(DIM),
        ("a",),
        np.eye(1, DIM),
        (5,),
        {"long": 0.2, "short": 0.1},
        {5: 0.3},
        0.1,
    )
    with pytest.raises(ValueError, match="2 documents but 1 vectors"):
        assign_corpus(
            [_doc(0, 5), _doc(1, 5)], np.zeros((1, DIM)), cal, [], author_labels={}
        )
