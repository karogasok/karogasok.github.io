"""Run the pre-registered gate on the held-out half, once.

The new placement may replace the archive's only if it passes the criteria
frozen in analysis/temalista_kalibracio.json — committed before this script is
ever run. It places the held-out half of the Kereső Világ rows, which no step of
the tuning has read, and checks:

* **G1** — BCubed F beats the stronger of the two baselines by the frozen
  margin, and the paired bootstrap's 95% lower bound is above zero;
* **G2** — coverage, themes per writing and the largest theme's share stay
  within the frozen limits;
* **G3** — none of the four 2026 posts lands in a forbidden theme, and each gets
  one of its expected themes or none at all.

The result is written to analysis/eval/gate_result.json. If that file already
exists the script refuses to run: a held-out set looked at twice is no longer
held out.

Usage:
    uv run python scripts/gate.py
"""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

from karogasok_temak import themes as theme_list
from karogasok_temak.corpus import MIN_FIT_WORDS, Document, load_corpus
from karogasok_temak.embed import EncoderSpec, encode_cached
from karogasok_temak.evaluate import (
    bcubed,
    clean_labels,
    load_label_rules,
    paired_bootstrap,
    split_of,
)
from karogasok_temak.gold import kereses_labels
from karogasok_temak.placement import load_calibration, place

HERE = Path(__file__).resolve().parents[1]
EVAL = HERE / "eval"
RESULT = EVAL / "gate_result.json"
GENRE_THEMES = {"Lapszemle", "NLP meetupok", "A blog életéről", "Kurzusok és önképzés"}


def key_of(doc: Document) -> str:
    """Pages by path, data rows by their URL — the same keys place.py uses."""
    return (
        doc.doc_id if doc.source in ("archivum", "posts") else (doc.key or doc.doc_id)
    )


def main() -> int:  # noqa: C901, PLR0915
    """Place the held-out half and judge it against the frozen criteria."""
    if RESULT.exists():
        print(
            f"  {RESULT.name} exists — the gate has already run. Not running it again."
        )
        return 1
    frozen = HERE / "temalista_kalibracio.json"
    dirty = subprocess.run(
        [
            "git",
            "status",
            "--porcelain",
            "--",
            str(frozen),
            str(HERE / "temalista.yaml"),
        ],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    if dirty:
        print("  calibration or theme list differs from the commit; not running")
        return 1
    commit = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--", str(frozen)],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    cal, record = load_calibration(
        HERE / "temalista_kalibracio.json", HERE / "temalista.yaml"
    )
    gate = record["gate"]
    spec = EncoderSpec(**record["encoder"])
    active = [
        t for t in theme_list.load(HERE / "temalista.yaml") if t.allapot == "aktiv"
    ]
    seed_of: dict[str, list[str]] = {}
    for t in active:
        for s in t.magok:
            seed_of.setdefault(s, []).append(t.kulcs)

    year = dt.date.today().year
    docs = [
        d for d in load_corpus() if d.text.strip() and not (d.year and d.year > year)
    ]
    rows = [d for d in docs if d.source == "kereses" and split_of(key_of(d)) == "test"]
    long_pages = [
        d
        for d in docs
        if d.source in ("archivum", "posts") and d.word_count >= MIN_FIT_WORDS
    ]
    posts_2026 = [d for d in docs if d.doc_id in gate["G3"]["expected_any_of"]]

    everything = rows + long_pages + posts_2026
    vectors = encode_cached(spec, [d.text for d in everything])
    vec = {id(d): v for d, v in zip(everything, vectors, strict=True)}

    placed_rows = {
        key_of(d): place(
            vec[id(d)], "long" if d.word_count >= MIN_FIT_WORDS else "short", cal
        ).themes
        for d in rows
    }
    placed_pages = {
        d.doc_id: place(
            vec[id(d)], "long", cal, seed_of=seed_of.get(d.doc_id, ())
        ).themes
        for d in long_pages
    }

    rules = load_label_rules(EVAL / "cimke_normalizalas.yaml")
    gold = {
        k: v
        for k, v in clean_labels(kereses_labels(), rules).items()
        if split_of(k) == "test"
    }
    base = json.loads((EVAL / "baseline_2026-09.json").read_text(encoding="utf-8"))
    base_a = {key_of(d): tuple(base["sorok"].get(key_of(d), [])) for d in rows}
    base_b = {
        k: tuple(t for t in v if t not in GENRE_THEMES) for k, v in base_a.items()
    }
    scored = [k for k in placed_rows if k in gold]

    f_new = bcubed(placed_rows, gold, scored)
    f_a, f_b = bcubed(base_a, gold, scored), bcubed(base_b, gold, scored)
    stronger, stronger_name = (base_a, "A") if f_a.f >= f_b.f else (base_b, "B")
    delta = paired_bootstrap(
        stronger,
        placed_rows,
        gold,
        scored,
        n=gate["G1"]["bootstrap"]["resamples"],
        seed=gate["G1"]["bootstrap"]["seed"],
    )
    g1 = (
        delta.observed >= gate["G1"]["min_delta"]
        and delta.low > gate["G1"]["bootstrap"]["lower_bound_above"]
    )

    def shares(placed: dict[str, tuple[str, ...]]) -> tuple[float, float, float]:
        n = len(placed)
        cover = sum(1 for v in placed.values() if v) / n
        mean = sum(len(v) for v in placed.values()) / n
        counts: dict[str, int] = {}
        for v in placed.values():
            for t in v:
                counts[t] = counts.get(t, 0) + 1
        return cover, mean, (max(counts.values()) / n if counts else 0.0)

    cov_r, mean_r, big_r = shares(placed_rows)
    cov_p, _, big_p = shares(placed_pages)
    mean_base_r = sum(len(v) for v in base_a.values()) / len(base_a)
    lim = gate["G2"]
    g2 = (
        cov_p >= lim["min_coverage_long_pages"]
        and cov_r >= lim["min_coverage_rows"]
        and mean_r <= mean_base_r
        and max(big_r, big_p) <= lim["max_theme_share"]
    )

    g3_detail, g3 = {}, True
    for d in posts_2026:
        got = place(vec[id(d)], "long", cal).themes
        forbidden = set(got) & set(gate["G3"]["forbidden_for_all"])
        expected = set(gate["G3"]["expected_any_of"][d.doc_id])
        ok = not forbidden and (not got or bool(set(got) & expected))
        g3 = g3 and ok
        g3_detail[d.doc_id] = {
            "got": list(got),
            "expected_any_of": sorted(expected),
            "flagged_no_theme": not got,
            "ok": ok,
        }

    passed = g1 and g2 and g3
    result = {
        "passed": passed,
        "preregistration_commit": commit,
        "G1": {
            "passed": g1,
            "new_F": f_new.f,
            "baseline_A_F": f_a.f,
            "baseline_B_F": f_b.f,
            "stronger": stronger_name,
            "delta": delta.observed,
            "ci95": [delta.low, delta.high],
            "n": delta.n,
        },
        "G2": {
            "passed": g2,
            "coverage_rows": cov_r,
            "coverage_long_pages": cov_p,
            "mean_themes_rows": mean_r,
            "mean_themes_rows_baseline": mean_base_r,
            "largest_share_rows": big_r,
            "largest_share_pages": big_p,
        },
        "G3": {"passed": g3, "posts": g3_detail},
    }
    RESULT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(
        f"  G1 {'PASS' if g1 else 'FAIL'}: F {f_new.f:.3f} vs {stronger_name} "
        f"{max(f_a.f, f_b.f):.3f}  Δ {delta.observed:+.3f} "
        f"[{delta.low:+.3f}, {delta.high:+.3f}]  n={delta.n}"
    )
    print(
        f"  G2 {'PASS' if g2 else 'FAIL'}: rows covered {cov_r:.0%}, "
        f"pages covered {cov_p:.0%}, "
        f"themes/row {mean_r:.2f} (baseline {mean_base_r:.2f}), "
        f"largest {max(big_r, big_p):.0%}"
    )
    for doc_id, r in g3_detail.items():
        mark = "ok " if r["ok"] else "BAD"
        print(f"  G3 {mark} {doc_id.split('/')[-1]}: {r['got'] or '—'}")
    print(
        f"\n  GATE {'PASSED' if passed else 'FAILED'} — "
        f"result in {RESULT.relative_to(HERE)}"
    )
    return 0 if passed else 2


if __name__ == "__main__":
    sys.exit(main())
