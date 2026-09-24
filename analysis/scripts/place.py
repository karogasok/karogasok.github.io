"""Tune theme placement on the tuning data, and report what it would do.

For each candidate encoder, a small grid is searched on the author's labelled
pages (seeds held out) and then on the tuning half of the Kereső Világ rows.
The held-out half is never read here — that is the gate's job, run once.

Grid, declared before any result was seen:

* centring on the mean of the author's pages, or of the whole corpus;
* δ (the margin a secondary theme must be within) ∈ {0.05, 0.10, 0.15};
* τ_long over the similarity levels that place 60–98% of the long pages;
* then, with everything else fixed and on the Kereső Világ tuning half, the
  short writings' centring (the long pages' mean, or the mean of the short
  writings themselves, held-out rows excluded) and τ_short.

Added after the first run, before the gate: the one-sided seed-count correction
and the short writings' own mean. The first run's review showed both 3-seed
themes and then *Vizualizáció* acting as catch-alls; see placement.py.

A configuration is admissible only if it meets the gate's G2 limits on the
tuning data: at least 70% of long pages and 40% of rows get a theme, the mean
number of themes per writing is no higher than today's, and no theme covers more
than 25% of a class. Among admissible configurations the best BCubed F wins.

Between encoders, the one with the higher mean of its best page-F and row-F is
chosen — also declared in advance.

Usage:
    uv run python scripts/place.py e5-large bge-m3

Writes out/placement_tuning.json, out/kalibracio_jelolt.npz (the winner's
frozen values, not yet committed) and out/besorolas_jelentes.md (the review).
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np

from karogasok_temak import themes as theme_list
from karogasok_temak.corpus import MIN_FIT_WORDS, Document, load_corpus
from karogasok_temak.embed import encode_cached, spec_named
from karogasok_temak.evaluate import bcubed, clean_labels, load_label_rules, split_of
from karogasok_temak.gold import archive_labels, kereses_labels
from karogasok_temak.placement import (
    Calibration,
    place,
    seed_count_curve,
    theme_vectors,
    unit,
)

HERE = Path(__file__).resolve().parents[1]
OUT, EVAL = HERE / "out", HERE / "eval"

COVER_LONG, COVER_SHORT, MAX_SHARE = 0.70, 0.40, 0.25
DELTAS = (0.05, 0.10, 0.15)
KS = (3, 4, 5, 6, 8)
GENRE_THEMES = {"Lapszemle", "NLP meetupok", "A blog életéről", "Kurzusok és önképzés"}


def key_of(doc: Document) -> str:
    """Pages by path, data rows by their URL — never by position."""
    return (
        doc.doc_id if doc.source in ("archivum", "posts") else (doc.key or doc.doc_id)
    )


def usable(docs: list[Document]) -> list[Document]:
    """Drop empty and future-dated writings."""
    year = dt.date.today().year
    return [d for d in docs if d.text.strip() and not (d.year and d.year > year)]


def evaluate(
    placed: dict[str, tuple[str, ...]],
    keys: list[str],
    gold: dict[str, frozenset[str]],
    baseline_mean: float,
    cover_min: float,
) -> dict[str, Any]:
    """Score one class of writings and check the G2 limits."""
    n = len(keys)
    counts = Counter(t for k in keys for t in placed[k])
    coverage = sum(1 for k in keys if placed[k]) / n
    mean = sum(len(placed[k]) for k in keys) / n
    largest = max(counts.values()) / n if counts else 0.0
    scored = [k for k in keys if k in gold]
    s = bcubed({k: placed[k] for k in scored}, gold, scored)
    ok = coverage >= cover_min and mean <= baseline_mean and largest <= MAX_SHARE
    return {
        "F": s.f,
        "P": s.precision,
        "R": s.recall,
        "n_scored": s.n,
        "coverage": coverage,
        "mean_themes": mean,
        "largest_share": largest,
        "admissible": ok,
    }


def main() -> int:  # noqa: C901, PLR0915
    """Tune every named encoder, choose one, write the review."""
    names = sys.argv[1:] or ["e5-large"]
    active = [
        t for t in theme_list.load(HERE / "temalista.yaml") if t.allapot == "aktiv"
    ]
    keys_t = tuple(t.kulcs for t in active)
    label = {t.kulcs: t.nev for t in active}
    seed_of: dict[str, list[str]] = {}
    for t in active:
        for s in t.magok:
            seed_of.setdefault(s, []).append(t.kulcs)

    docs = usable(load_corpus())
    keys = [key_of(d) for d in docs]
    by_key = dict(zip(keys, docs, strict=True))
    klass = {
        k: "long" if d.word_count >= MIN_FIT_WORDS else "short"
        for k, d in by_key.items()
    }
    pages = [k for k in keys if by_key[k].source in ("archivum", "posts")]
    long_pages = [k for k in pages if klass[k] == "long"]
    rows_dev = [
        k for k in keys if by_key[k].source == "kereses" and split_of(k) == "dev"
    ]

    rules = load_label_rules(EVAL / "cimke_normalizalas.yaml")
    gold_pages = clean_labels(archive_labels(), rules)
    gold_rows = clean_labels(kereses_labels(), rules)
    base = json.loads((EVAL / "baseline_2026-09.json").read_text(encoding="utf-8"))
    base_pages = {k: tuple(base["oldalak"].get(k, [])) for k in long_pages}
    base_rows = {k: tuple(base["sorok"].get(k, [])) for k in rows_dev}
    dev_pages = [k for k in long_pages if k not in seed_of]
    mean_a_pages = sum(len(base_pages[k]) for k in dev_pages) / len(dev_pages)
    mean_a_rows = sum(len(base_rows[k]) for k in rows_dev) / len(rows_dev)

    # The old clusters, for the seed-count curve: the only multi-member groups
    # we have that the curated list was not tuned on.
    topics = json.loads((OUT / "topics.json").read_text(encoding="utf-8"))
    clusters: dict[int, list[str]] = {}
    for doc_id, a in topics["assignments"].items():
        if a.get("role") == "fitted" and a["topic_reduced"] >= 0 and doc_id in by_key:
            clusters.setdefault(a["topic_reduced"], []).append(doc_id)

    report: dict[str, Any] = {"encoders": {}}
    best_overall: tuple[float, str, dict, Calibration] | None = None
    for name in names:
        raw = encode_cached(spec_named(name), [by_key[k].text for k in keys])
        row = {k: i for i, k in enumerate(keys)}
        results: list[dict[str, Any]] = []
        for centring in ("pages", "corpus"):
            ref = long_pages if centring == "pages" else keys
            mean = raw[[row[k] for k in ref]].mean(axis=0)
            centred = unit(raw - mean)
            vecs = theme_vectors(
                {k: centred[row[k]] for k in keys}, [t.magok for t in active]
            )
            groups = [[row[k] for k in m] for m in clusters.values()]
            g = seed_count_curve(centred, groups, KS)
            best_long = np.array(
                [float(np.max(vecs @ centred[row[k]])) for k in long_pages]
            )
            taus = np.unique(
                np.round(np.quantile(best_long, np.linspace(0.02, 0.40, 20)), 3)
            )
            for delta in DELTAS:
                for tau in taus:
                    cal = Calibration(
                        mean,
                        keys_t,
                        vecs,
                        tuple(len(t.magok) for t in active),
                        {"long": float(tau), "short": float(tau)},
                        g,
                        delta,
                    )
                    placed = {
                        k: place(
                            raw[row[k]], "long", cal, seed_of=seed_of.get(k, ())
                        ).themes
                        for k in long_pages
                    }
                    ev = evaluate(
                        placed, dev_pages, gold_pages, mean_a_pages, COVER_LONG
                    )
                    results.append(
                        {
                            "centring": centring,
                            "delta": delta,
                            "tau_long": float(tau),
                            "pages": ev,
                            "_cal": cal,
                        }
                    )
        admissible = [r for r in results if r["pages"]["admissible"]]
        pool = admissible or results
        top = max(pool, key=lambda r: (r["pages"]["F"], r["tau_long"]))
        cal: Calibration = top["_cal"]
        short_ref = [
            k
            for k in keys
            if klass[k] == "short"
            and not (by_key[k].source == "kereses" and split_of(k) == "test")
        ]
        short_means = {
            "long": None,
            "own": raw[[row[k] for k in short_ref]].mean(axis=0),
        }
        short_results: list[dict[str, Any]] = []
        for short_centring, mean_short in short_means.items():
            base_s = Calibration(
                cal.mean,
                cal.theme_keys,
                cal.vectors,
                cal.seed_counts,
                dict(cal.tau),
                cal.g,
                cal.delta,
                mean_short=mean_short,
            )
            sims_rows = np.array(
                [
                    float(np.max(cal.vectors @ base_s.centre(raw[row[k]], klass[k])))
                    for k in rows_dev
                ]
            )
            for tau_s in np.unique(
                np.round(np.quantile(sims_rows, np.linspace(0.05, 0.60, 24)), 3)
            ):
                cal_s = Calibration(
                    cal.mean,
                    cal.theme_keys,
                    cal.vectors,
                    cal.seed_counts,
                    {"long": cal.tau["long"], "short": float(tau_s)},
                    cal.g,
                    cal.delta,
                    mean_short=mean_short,
                )
                placed = {
                    k: place(raw[row[k]], klass[k], cal_s).themes for k in rows_dev
                }
                short_results.append(
                    {
                        "short_centring": short_centring,
                        "tau_short": float(tau_s),
                        "rows": evaluate(
                            placed, rows_dev, gold_rows, mean_a_rows, COVER_SHORT
                        ),
                        "_cal": cal_s,
                    }
                )
        pool_s = [r for r in short_results if r["rows"]["admissible"]] or short_results
        top_s = max(pool_s, key=lambda r: (r["rows"]["F"], r["tau_short"]))
        final: Calibration = top_s["_cal"]
        score = (top["pages"]["F"] + top_s["rows"]["F"]) / 2
        report["encoders"][name] = {
            "centring": top["centring"],
            "short_centring": top_s["short_centring"],
            "delta": top["delta"],
            "one_sided": final.one_sided,
            "tau": dict(final.tau),
            "g": {str(k): v for k, v in final.g.items()},
            "pages": top["pages"],
            "rows": top_s["rows"],
            "admissible_long_configs": len(admissible),
            "tried_long_configs": len(results),
            "choice_score": score,
        }
        print(
            f"== {name}: centring={top['centring']}/{top_s['short_centring']} "
            f"δ={top['delta']} "
            f"τ_long={final.tau['long']:.3f} τ_short={final.tau['short']:.3f}"
        )
        for cls, ev in (("pages", top["pages"]), ("rows ", top_s["rows"])):
            verdict = "ok" if ev["admissible"] else "NOT ADMISSIBLE"
            print(
                f"   {cls} F={ev['F']:.3f} (P {ev['P']:.3f} R {ev['R']:.3f})  "
                f"coverage {ev['coverage']:.0%}  "
                f"themes/writing {ev['mean_themes']:.2f}  "
                f"largest {ev['largest_share']:.0%}  {verdict}"
            )
        if best_overall is None or score > best_overall[0]:
            best_overall = (score, name, top, final)

    # Baselines on exactly the same items, for comparison.
    no_genre = {
        k: tuple(t for t in v if t not in GENRE_THEMES)
        for k, v in {**base_pages, **base_rows}.items()
    }
    for cls, items, gold in (
        ("pages", dev_pages, gold_pages),
        ("rows", rows_dev, gold_rows),
    ):
        a = bcubed(
            {k: (base_pages | base_rows)[k] for k in items if k in gold},
            gold,
            [k for k in items if k in gold],
        )
        b = bcubed(
            {k: no_genre[k] for k in items if k in gold},
            gold,
            [k for k in items if k in gold],
        )
        report[f"baseline_{cls}"] = {"A": a.f, "B": b.f, "n": a.n}
        print(f"   baseline {cls}: A F={a.f:.3f}  B F={b.f:.3f}  (n={a.n})")

    assert best_overall is not None
    _, winner, _, cal = best_overall
    report["winner"] = winner
    print(f"\n  chosen encoder: {winner}")
    np.savez(
        OUT / "kalibracio_jelolt.npz",
        encoder=np.array(winner),
        mean=cal.mean,
        mean_short=cal.mean_short if cal.mean_short is not None else np.array(0.0),
        theme_keys=np.array(cal.theme_keys),
        vectors=cal.vectors,
        seed_counts=np.array(cal.seed_counts),
        tau=np.array([cal.tau["long"], cal.tau["short"]]),
        g_k=np.array(list(cal.g)),
        g_v=np.array(list(cal.g.values())),
        delta=np.array(cal.delta),
        one_sided=np.array(cal.one_sided),
    )
    (OUT / "placement_tuning.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
    )

    # The review: the four 2026 posts, the unplaced pages, theme sizes, candidate seeds.
    raw = encode_cached(spec_named(winner), [by_key[k].text for k in keys])
    row = {k: i for i, k in enumerate(keys)}
    placed_all = {
        k: place(raw[row[k]], klass[k], cal, seed_of=seed_of.get(k, ())) for k in keys
    }
    lines = [f"# Besorolás — áttekintés ({winner})", ""]
    lines += ["## A négy 2026-os bejegyzés", ""]
    for k in [k for k in pages if k.startswith("content/posts/2026")]:
        p = placed_all[k]
        cal_sims = cal.vectors @ cal.centre(raw[row[k]], klass[k])
        near = ", ".join(
            f"{label[cal.theme_keys[i]]} {cal_sims[i]:.2f}"
            for i in np.argsort(-cal_sims)[:3]
        )
        got = ", ".join(label[t] for t in p.themes) or "— (nincs téma)"
        lines.append(f"- **{by_key[k].title}** → {got}  \n  legközelebbi: {near}")
    sizes = Counter(t for k in keys for t in placed_all[k].themes)
    lines += ["", "## Témák mérete (összes írás)", ""]
    lines += [f"- {label[t]}: {sizes.get(t, 0)}" for t in keys_t]
    unplaced = [k for k in long_pages if not placed_all[k].themes]
    lines += ["", f"## Téma nélkül maradt saját írások ({len(unplaced)})", ""]
    lines += [
        f"- {by_key[k].year} — {by_key[k].title} (legjobb: {placed_all[k].best:.2f})"
        for k in sorted(unplaced)
    ]
    lines += ["", "## Magjelöltek (a legközelebbi nem-mag tagok)", ""]
    for i, t in enumerate(keys_t):
        members = [
            k for k in long_pages if t in placed_all[k].themes and k not in seed_of
        ]
        ranked = sorted(
            members,
            key=lambda k: -float(cal.vectors[i] @ cal.centre(raw[row[k]], klass[k])),
        )
        lines.append(
            f"- **{label[t]}**: " + "; ".join(by_key[k].title[:50] for k in ranked[:4])
        )
    (OUT / "besorolas_jelentes.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print(f"  wrote {OUT / 'besorolas_jelentes.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
