"""List every theme move the new placement would make, for the author to review.

Nothing is exported until the author has read this list and approved it. The
old placement is the committed snapshot (eval/baseline_2026-09.json); its theme
names are carried through the renames in temalista.yaml, so a theme that was
only renamed does not count as a move. The new placement is the frozen
calibration, the one that passed the gate, as written to ``out/placement.json``
by ``infer.py`` — so the list shows exactly what the export will publish,
including the writings the subject-less rule leaves without a theme.

Usage:
    uv run python scripts/moves.py

Writes out/athelyezesek.md (to read) and out/athelyezesek.json (the machine
version), and prints the JSON's sha256. The export will refuse to run unless
that hash is recorded as approved.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

from karogasok_temak import themes as theme_list
from karogasok_temak.assign import key_of, length_class
from karogasok_temak.corpus import load_corpus
from karogasok_temak.placement import load_calibration

HERE = Path(__file__).resolve().parents[1]
OUT, EVAL = HERE / "out", HERE / "eval"
NONE = "—"
SOURCE_NAMES = {
    "archivum": "Archívum",
    "posts": "Bejegyzések",
    "kereses": "Kereső Világ",
    "media": "Média",
    "mashol": "Máshol",
}


def main() -> int:  # noqa: C901, PLR0915
    """Compare the old and new placement of every writing."""
    all_themes = theme_list.load(HERE / "temalista.yaml")
    _, record = load_calibration(
        HERE / "temalista_kalibracio.json", HERE / "temalista.yaml"
    )
    name_of = {t.kulcs: t.nev for t in all_themes}
    old_to_key: dict[str, str] = {}
    for t in all_themes:
        for n in (t.nev, *t.korabbi_nevek):
            old_to_key[n] = t.kulcs
    retired = {t.kulcs for t in all_themes if t.allapot == "megszunt"}
    placement = json.loads((OUT / "placement.json").read_text(encoding="utf-8"))[
        "placement"
    ]

    base = json.loads((EVAL / "baseline_2026-09.json").read_text(encoding="utf-8"))
    old_all = {**base["oldalak"], **base["sorok"]}
    unknown = sorted({n for v in old_all.values() for n in v} - set(old_to_key))
    if unknown:
        print(f"  old theme names missing from temalista.yaml: {unknown}")
        return 1

    docs = [d for d in load_corpus() if d.text.strip()]
    entries = []
    for d in docs:
        k = key_of(d)
        klass = length_class(d)
        p = placement[k]
        old = [old_to_key[n] for n in old_all.get(k, [])]
        old = list(dict.fromkeys(old))
        new = list(p["temak"])
        entries.append(
            {
                "key": k,
                "source": d.source,
                "year": d.year,
                "title": d.title,
                "class": klass,
                "old": old,
                "new": new,
                "scores": p["scores"],
                "best": p["best"],
                "role": p["role"],
                "in_baseline": k in old_all,
            }
        )

    def kind(e: dict) -> str:
        old, new = set(e["old"]), set(e["new"])
        if old == new:
            return "változatlan" if old else "továbbra is téma nélkül"
        if not new:
            return "téma nélkül marad"
        if not old:
            return "témát kap"
        if old < new:
            return "bővül"
        if new < old:
            return "szűkül"
        return "módosul"

    for e in entries:
        e["kind"] = kind(e)

    payload = json.dumps(
        {"calibration_sha256": record["temalista_sha256"], "moves": entries},
        ensure_ascii=False,
        indent=1,
        sort_keys=True,
    )
    (OUT / "athelyezesek.json").write_text(payload, encoding="utf-8")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()

    label = {**name_of, NONE: "(nincs téma)"}

    def names(keys: list[str]) -> str:
        return (
            ", ".join(f"~~{label[k]}~~" if k in retired else label[k] for k in keys)
            or NONE
        )

    lines = [
        "# Áthelyezések — régi és új témabesorolás",
        "",
        "A régi besorolás a `baseline_2026-09.json` pillanatképe, a témaneveket "
        "átvezetve az átnevezéseken; az új a befagyasztott kalibráció, amely "
        "átment a kapun. ~~Áthúzva~~: megszűnt műfaji téma.",
        "",
        f"Ellenőrzőösszeg (sha256): `{digest}`",
        "",
        "## Összesítés",
        "",
        "| forrás | "
        + " | ".join(
            k
            for k in (
                "változatlan",
                "bővül",
                "szűkül",
                "módosul",
                "témát kap",
                "téma nélkül marad",
                "továbbra is téma nélkül",
            )
        )
        + " | összes |",
        "|---|" + "---:|" * 8,
    ]
    kinds = (
        "változatlan",
        "bővül",
        "szűkül",
        "módosul",
        "témát kap",
        "téma nélkül marad",
        "továbbra is téma nélkül",
    )
    for src, title in SOURCE_NAMES.items():
        c = Counter(e["kind"] for e in entries if e["source"] == src)
        n = sum(c.values())
        if n:
            lines.append(
                f"| {title} | "
                + " | ".join(str(c.get(k, 0)) for k in kinds)
                + f" | {n} |"
            )
    c = Counter(e["kind"] for e in entries)
    lines.append(
        "| **összes** | "
        + " | ".join(str(c.get(k, 0)) for k in kinds)
        + f" | {len(entries)} |"
    )

    # Flow: of the writings that carried an old theme, where do they go?
    lines += [
        "",
        "## Hová kerülnek a régi témák írásai",
        "",
        "Soronként: a régi téma írásai, és hogy az új besorolásban mely témákat "
        "kapják (egy írás több helyen is számít).",
        "",
    ]
    olds = [t.kulcs for t in all_themes]
    for o in olds:
        members = [e for e in entries if o in e["old"]]
        if not members:
            continue
        flow = Counter(t for e in members for t in (e["new"] or [NONE]))
        stay = sum(1 for e in members if o in e["new"])
        top = ", ".join(f"{label[t]} {n}" for t, n in flow.most_common(6))
        lines.append(f"- **{names([o])}** ({len(members)} írás, {stay} marad): {top}")

    sizes_old = Counter(t for e in entries for t in e["old"])
    sizes_new = Counter(t for e in entries for t in e["new"])
    lines += ["", "## Témák mérete", "", "| téma | régi | új |", "|---|---:|---:|"]
    for o in olds:
        if sizes_old[o] or sizes_new[o]:
            lines.append(f"| {names([o])} | {sizes_old[o]} | {sizes_new[o]} |")

    for src, title in SOURCE_NAMES.items():
        changed = [
            e
            for e in entries
            if e["source"] == src
            and e["kind"] not in ("változatlan", "továbbra is téma nélkül")
        ]
        if not changed:
            continue
        lines += ["", f"## {title}: változó besorolások ({len(changed)})", ""]
        for e in sorted(changed, key=lambda e: (e["kind"], str(e["year"]), e["title"])):
            lines.append(
                f"- *{e['kind']}* — {e['year'] or ''} {e['title'][:80]}: "
                f"{names(e['old'])} → **{names(e['new'])}**"
            )
    (OUT / "athelyezesek.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"  {len(entries)} writings: " + ", ".join(f"{k} {c.get(k, 0)}" for k in kinds)
    )
    print(f"  wrote {OUT / 'athelyezesek.md'}")
    print(f"  sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
