"""Propose new themes from the author's writings that no theme fits.

Reads where every writing was placed (``out/placement.json``) and groups the
candidates — the author's long archive pages that got no theme, plus every
post — by similarity, in the same centred space the placement uses. Each group
of at least three is written up with checkable evidence (see
:mod:`karogasok_temak.discover`). Nothing is published: a proposal becomes a
theme only when the author adds it to ``temalista.yaml`` with a name, and the
calibration is rebuilt.

The link roundups the placement leaves theme-less on purpose are not candidates:
they have no subject to discover.

Usage:
    uv run python scripts/discover.py [--threshold D] [--min-size N]

``--threshold`` defaults to the cohesion of the existing themes' seeds (one
minus their median pairwise similarity), measured on every run and recorded.

Writes out/javaslatok.md (to read), out/javaslatok.json (the record).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

from karogasok_temak import themes as theme_list
from karogasok_temak.assign import key_of, length_class
from karogasok_temak.corpus import load_corpus
from karogasok_temak.discover import (
    MIN_SIZE,
    central,
    clusters,
    cohesion_threshold,
    evidence_sentence,
    over_represented,
)
from karogasok_temak.embed import EncoderSpec, encode_cached
from karogasok_temak.gold import archive_labels
from karogasok_temak.keywords import corpus_counts, document_keywords, keyword_lemmas
from karogasok_temak.placement import load_calibration
from karogasok_temak.stopwords import hungarian_stopwords

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "out"

#: Keyness terms shown per group, and how many members must use one for it to
#: count — a term only one member uses describes that member, not the group.
N_TERMS, MIN_MEMBERS = 8, 2


def main() -> int:  # noqa: C901, PLR0915
    """Group the theme-less writings and write the proposals."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--threshold", type=float, default=None)
    parser.add_argument("--min-size", type=int, default=MIN_SIZE)
    args = parser.parse_args()

    cal, record = load_calibration(
        HERE / "temalista_kalibracio.json", HERE / "temalista.yaml"
    )
    spec = EncoderSpec(**record["encoder"])
    active = [
        t for t in theme_list.load(HERE / "temalista.yaml") if t.allapot == "aktiv"
    ]
    names = {t.kulcs: t.nev for t in active}
    placement = json.loads((OUT / "placement.json").read_text(encoding="utf-8"))[
        "placement"
    ]
    year = dt.date.today().year
    docs = [
        d for d in load_corpus() if d.text.strip() and not (d.year and d.year > year)
    ]
    by_key = {key_of(d): d for d in docs}

    candidates = [
        d
        for d in docs
        if d.source == "posts"
        or (
            d.source == "archivum"
            and length_class(d) == "long"
            and placement[key_of(d)]["role"] == "none"
        )
    ]
    if len(candidates) < 2:
        print(f"only {len(candidates)} candidate(s) — nothing to group.")
        return 0

    def centred(texts: list[str]) -> np.ndarray:
        return np.array(
            [cal.centre(v, "long") for v in encode_cached(spec, texts)], dtype=float
        )

    vectors = centred([d.text for d in candidates])
    seed_groups = [centred([by_key[s].text for s in t.magok]) for t in active]
    measured = cohesion_threshold(seed_groups)
    threshold = measured if args.threshold is None else args.threshold
    groups = clusters(vectors, threshold, min_size=args.min_size)

    lemmas: dict[str, list[str]] = json.loads(
        (OUT / "lemmas.json").read_text(encoding="utf-8")
    )
    stops = hungarian_stopwords()
    filtered = {k: keyword_lemmas(v, stops) for k, v in lemmas.items()}
    totals = corpus_counts(list(filtered.values()))
    labels = archive_labels()
    pool_labels = [labels.get(key_of(d), []) for d in docs if d.source == "archivum"]

    proposals: list[dict[str, Any]] = []
    for number, members in enumerate(groups, start=1):
        member_docs = [candidates[i] for i in members]
        focus = [w for d in member_docs for w in filtered.get(d.doc_id, [])]
        used_by = {
            k.term: sum(1 for d in member_docs if k.term in filtered.get(d.doc_id, []))
            for k in document_keywords(focus, totals, top_n=40)
        }
        terms = [t for t, n in used_by.items() if n >= MIN_MEMBERS][:N_TERMS]
        centroid = vectors[members].mean(axis=0)
        centroid /= np.linalg.norm(centroid) or 1.0
        near = cal.vectors @ centroid
        nearest = [
            {"tema": names[cal.theme_keys[i]], "hasonlosag": round(float(near[i]), 3)}
            for i in np.argsort(-near)[:3]
        ]
        seeds = [candidates[i] for i in central(vectors, members, n=3)]
        proposals.append(
            {
                "szam": number,
                "meret": len(members),
                "tagok": [
                    {"kulcs": key_of(d), "ev": d.year, "cim": d.title}
                    for d in member_docs
                ],
                "kulcsszavak": [{"szo": t, "tagok": used_by[t]} for t in terms],
                "cimkek": [
                    {
                        "cimke": c.label,
                        "a_csoportban": c.in_group,
                        "csoport_merete": c.group_size,
                        "osszesen": c.overall,
                        "archivum_merete": c.pool_size,
                        "arany": round(c.ratio, 2),
                    }
                    for c in over_represented(
                        [labels.get(key_of(d), []) for d in member_docs], pool_labels
                    )[:6]
                ],
                "legkozelebbi_temak": nearest,
                "magjeloltek": [
                    {
                        "kulcs": key_of(d),
                        "cim": d.title,
                        "idezet": evidence_sentence(d.text, terms),
                    }
                    for d in seeds
                ],
            }
        )

    clustered = sum(p["meret"] for p in proposals)
    payload = {
        "reproducibility": {
            "date": dt.date.today().isoformat(),
            "calibration_temalista_sha256": record["temalista_sha256"],
            "encoder": record["encoder"],
            "candidates": len(candidates),
            "candidate_rule": "posts, plus long archive pages placed on no theme "
            "(role 'none'; subject-less roundups excluded)",
            "threshold": threshold,
            "threshold_measured_from_seeds": measured,
            "threshold_overridden": args.threshold is not None,
            "linkage": "average, cosine distance, centred on the calibration mean",
            "min_size": args.min_size,
            "terms_min_members": MIN_MEMBERS,
            "left_ungrouped": len(candidates) - clustered,
        },
        "javaslatok": proposals,
    }
    (OUT / "javaslatok.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    lines = [
        "# Témajavaslatok",
        "",
        f"{len(candidates)} jelölt írás (a bejegyzések és a téma nélkül maradt hosszú "
        f"archívumoldalak), ebből {clustered} került {len(proposals)} csoportba, "
        f"{len(candidates) - clustered} egyedül maradt. Vágási távolság: "
        f"{threshold:.3f}"
        + (
            " (a meglévő témák magjainak összetartásából mérve)."
            if args.threshold is None
            else f" (kézzel megadva; a mért érték {measured:.3f})."
        ),
        "",
        "Egy csoport akkor lehet új téma, ha van közös tárgya. Ha a legközelebbi "
        "meglévő téma hasonlósága magas, inkább hiányzó mag, mint hiányzó téma.",
    ]
    for p in proposals:
        lines += ["", f"## {p['szam']}. javaslat — {p['meret']} írás", ""]
        lines += [f"- {m['ev']} — {m['cim']}" for m in p["tagok"]]
        kw = ", ".join(f"{k['szo']} ({k['tagok']})" for k in p["kulcsszavak"])
        lines += ["", f"**Kulcsszavak** (zárójelben: hány tag használja): {kw or '—'}"]
        lb = ", ".join(
            f"{c['cimke']} ({c['a_csoportban']}/{c['csoport_merete']} itt, "
            f"{c['osszesen']}/{c['archivum_merete']} összesen)"
            for c in p["cimkek"]
        )
        lines += [f"**A régi címkéid közül felülreprezentált:** {lb or '—'}"]
        nr = ", ".join(
            f"{n['tema']} {n['hasonlosag']:.2f}" for n in p["legkozelebbi_temak"]
        )
        lines += [f"**Legközelebbi meglévő témák:** {nr}", "", "**Magjelöltek:**"]
        for s in p["magjeloltek"]:
            quote = (
                f"„{s['idezet']}”"
                if s["idezet"]
                else "(nincs rövid, kulcsszavas mondat)"
            )
            lines.append(f"- {s['cim']} — {quote}")
    lines += [
        "",
        "## Beillesztésre kész vázlat",
        "",
        "A nevet és a leírást neked kell megadnod; `allapot: javaslat` nem jelenik "
        "meg az oldalon.",
        "",
        "```yaml",
    ]
    for p in proposals:
        lines += [
            f"  - kulcs: javaslat-{p['szam']}",
            f'    nev: "Javaslat {p["szam"]}"',
            '    leiras: ""',
            "    allapot: javaslat",
            "    magok:",
        ]
        lines += [f"      - {s['kulcs']}" for s in p["magjeloltek"]]
        lines += [
            "    eredet:",
            f"      discover: {dt.date.today().isoformat()}",
            f"      meret: {p['meret']}",
        ]
    lines.append("```")
    (OUT / "javaslatok.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"  {len(candidates)} candidates, threshold {threshold:.3f} "
        f"(measured {measured:.3f}): {len(proposals)} group(s), "
        f"{len(candidates) - clustered} left alone"
    )
    print(f"  wrote {OUT / 'javaslatok.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
