"""Propose a name for each topic and write ``out/topic_names.json``.

The names are a model's reading of the topic terms and its representative
documents. That is a judgement call, so each one ships with the evidence needed
to check it — the terms, the documents, and a verbatim quote — and with
``checked_by_human: false`` until you say otherwise. ``export_temak.py`` refuses
to publish a name that is still false.

Usage:
    uv run python scripts/propose_names.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from karogasok_temak.corpus import load_corpus

OUT = Path(__file__).resolve().parents[1] / "out"

#: Proposed names, keyed by topic id. Each entry is (name, slug, rationale).
#: Written by reading the terms and the representative titles of each topic;
#: the rationale says which of them the name is meant to cover.
PROPOSED: dict[int, tuple[str, str, str]] = {
    0: (
        "Lapszemle",
        "lapszemle",
        "A heti linkgyűjtemények és hírösszefoglalók. Műfaj, nem tárgy — de "
        "a modell külön csoportként találta meg, és a 29 dokumentum tényleg "
        "ugyanaz a rovat.",
    ),
    1: (
        "Statisztika és R",
        "statisztika-es-r",
        "Statisztikai kézikönyvek és R-es könyvismertetők.",
    ),
    2: (
        "NLP meetupok",
        "nlp-meetupok",
        "A budapesti NLP meetup meghívói, előadói és álláshirdetései.",
    ),
    3: (
        "A blog életéről",
        "a-blog-eleterol",
        "Évfordulók, tervek, köszönetek, szerkesztőségi bejelentések. "
        "A leggyengébben körülhatárolt csoport: a közös vonás a hangnem, "
        "nem a tárgy.",
    ),
    4: (
        "Logika és matematika",
        "logika-es-matematika",
        "Logikai és matematikai alapok, Neumanntól a jelentés geometriájáig.",
    ),
    5: (
        "Korpusznyelvészet",
        "korpusznyelveszet",
        "Korpuszok, korpusznyelvészeti elmélet, nyelvi relativizmus.",
    ),
    6: (
        "Adatújságírás és nyílt adat",
        "adatujsagiras-es-nyilt-adat",
        "API-k, adatújságírás, nyílt adat és a digitális bölcsészet határa.",
    ),
    7: (
        "Tudományfilozófia",
        "tudomanyfilozofia",
        "Elméletek, paradigmák, a Chomsky–Norvig vita és a gépi tanulás "
        "tudományelméleti helye.",
    ),
    8: (
        "A szakma",
        "a-szakma",
        "Mi az a számítógépes nyelvészet, és kik csinálják — interjúk és pályaképek.",
    ),
    9: (
        "Programozás nyelvészeknek",
        "programozas-nyelveszeknek",
        "Python, R, Ruby, Clojure, nltk — nyelvészeknek szóló bevezetők.",
    ),
    10: (
        "Nyelvelemző eszközök",
        "nyelvelemzo-eszkozok",
        "Szófajelemzők, értelmezők, NooJ, Unicode és a saját kezű "
        "korpuszkészítés gyakorlata.",
    ),
    11: (
        "Paradigmák és nyelvelméletek",
        "paradigmak-es-nyelvelmeletek",
        "Szintaxiselméletek, lexikai szemantika, Kuhn és a nyelvészeti paradigmák.",
    ),
    12: (
        "Kurzusok és önképzés",
        "kurzusok-es-onkepzes",
        "ESSLLI, nyári egyetemek, és hogyan tanuljon meg valaki programozni egyedül.",
    ),
    13: (
        "Korpuszépítés és annotáció",
        "korpuszepites-es-annotacio",
        "Annotációs szabványok, XML, korpuszkészítés lépésről lépésre.",
    ),
    14: (
        "Nyílt szoftver és tervezés",
        "nyilt-szoftver-es-tervezes",
        "Licencek, nyílt forráskód, keresőfelületek és információtervezés.",
    ),
    15: (
        "Mesterséges intelligencia",
        "mesterseges-intelligencia",
        "Watson, a kínai technológiai fejlődés, biopunk — az MI mint közügy.",
    ),
    16: (
        "Szövegvizualizáció",
        "szovegvizualizacio",
        "Szófelhők, térképek, demográfiai és névadási ábrák.",
    ),
    17: (
        "Hálózatok és eszközök",
        "halozatok-es-eszkozok",
        "Gephi, gráfok, telepítés és a hozzájuk tartozó kódrészletek.",
    ),
    18: (
        "Startup és termékfejlesztés",
        "startup-es-termekfejlesztes",
        "Lean startup, ügyfélfejlesztés, MVP — a technológia üzleti oldala.",
    ),
}


def main() -> int:
    """Write the proposal file, checking every quote against its source."""
    topics = json.loads((OUT / "topics.json").read_text(encoding="utf-8"))
    documents = {d.doc_id: d for d in load_corpus()}

    missing = {t["id"] for t in topics["topics"]} - set(PROPOSED)
    if missing:
        print(f"no name proposed for topics {sorted(missing)}; re-run after naming")
        return 1

    names: dict[str, dict[str, object]] = {}
    unverified = 0
    for topic in topics["topics"]:
        name, slug, rationale = PROPOSED[topic["id"]]
        evidence = None
        for representative in topic["representative"]:
            quote = representative.get("quote")
            if not quote:
                continue
            document = documents.get(representative["doc_id"])
            # The point of the quote is that it can be found in the source with
            # a string search. If it cannot, it is not evidence.
            if document is None or quote not in document.text:
                continue
            evidence = {
                "quote": quote,
                "doc_id": representative["doc_id"],
                "title": representative["title"],
                "year": representative["year"],
            }
            break
        if evidence is None:
            unverified += 1
        names[str(topic["id"])] = {
            "name": name,
            "slug": slug,
            "rationale": rationale,
            "terms": topic["terms"][:10],
            "documents": [r["title"] for r in topic["representative"][:5]],
            "size_fitted": topic["size_fitted"],
            "size_total": topic["size_total"],
            "evidence": evidence,
            "checked_by_human": False,
        }

    (OUT / "topic_names.json").write_text(
        json.dumps(names, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"wrote {OUT / 'topic_names.json'} — {len(names)} proposed names")
    print(f"  {len(names) - unverified} carry a quote verified verbatim in its source")
    if unverified:
        print(f"  {unverified} have no verifiable quote")
    return 0


if __name__ == "__main__":
    sys.exit(main())
