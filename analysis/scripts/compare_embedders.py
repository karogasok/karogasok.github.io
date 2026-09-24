"""Which embedder puts writings the author labelled alike near each other?

Run once, to decide whether theme placement should keep huBERT or move to a
stronger multilingual model. Each candidate is judged by the share of a
writing's five nearest neighbours that carry one of the same cleaned labels —
the author's own labels, not a model's — separately for the archive pages and for
the tuning half of the Kereső Világ rows. The held-out half is not read.

Candidates are timed on 20 writings before any full encode, and every vector is
cached by the sha256 of the text it came from, so an interrupted run resumes.

Usage:
    uv run python scripts/compare_embedders.py [--only NAME ...]

Writes analysis/eval/embedder_comparison.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

from karogasok_temak.corpus import load_corpus
from karogasok_temak.embed import SPECS, encode_cached
from karogasok_temak.evaluate import (
    clean_labels,
    knn_shares,
    load_label_rules,
    paired_mean_delta,
    split_of,
)
from karogasok_temak.gold import archive_labels, kereses_labels

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "out"
EVAL = HERE / "eval"
CACHE = OUT / "embeddings"

#: Switch away from the current embedder only for at least this gain.
MIN_GAIN = 0.03


def main() -> int:
    """Encode with each candidate and compare them on the author's labels."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", nargs="*", default=None)
    args = parser.parse_args()

    rules = load_label_rules(EVAL / "cimke_normalizalas.yaml")
    documents = [d for d in load_corpus() if d.text.strip()]
    by_key = {d.key or d.doc_id: d for d in documents}

    pages_gold = clean_labels(archive_labels(), rules)
    rows_gold = {
        k: v
        for k, v in clean_labels(kereses_labels(), rules).items()
        if split_of(k) == "dev"
    }
    sources = {
        "oldalak": [k for k in sorted(pages_gold) if k in by_key],
        "sorok": [k for k in sorted(rows_gold) if k in by_key],
    }
    gold = {"oldalak": pages_gold, "sorok": rows_gold}

    specs = [s for s in SPECS if not args.only or s.name in args.only]
    results: dict[str, dict[str, object]] = {}
    shares: dict[tuple[str, str, str], np.ndarray] = {}
    for spec in specs:
        print(f"== {spec.name} ({spec.model})", flush=True)
        keys = sources["oldalak"] + sources["sorok"]
        vectors = encode_cached(spec, [by_key[k].text for k in keys])
        # Centre on the pages only, as placement will: adding blurbs must not
        # move the origin the author's own writing is measured from.
        centre = vectors[: len(sources["oldalak"])].mean(axis=0)
        for variant, space in (("raw", vectors), ("centred", vectors - centre)):
            row: dict[str, object] = {}
            offset = 0
            for source in ("oldalak", "sorok"):
                n = len(sources[source])
                s, _ = knn_shares(
                    space[offset : offset + n], sources[source], gold[source]
                )
                shares[(spec.name, variant, source)] = s
                row[source] = {"agreement": float(s.mean()), "n": int(len(s))}
                offset += n
            results[f"{spec.name}/{variant}"] = row
            print(
                f"   {variant:<8} pages {row['oldalak']['agreement']:.3f}   "
                f"rows {row['sorok']['agreement']:.3f}",
                flush=True,
            )

    baseline = ("hubert", "centred")
    comparisons: dict[str, dict[str, object]] = {}
    for (name, variant, source), s in shares.items():
        if (name, variant) == baseline or (
            baseline[0],
            baseline[1],
            source,
        ) not in shares:
            continue
        d = paired_mean_delta(shares[(baseline[0], baseline[1], source)], s)
        comparisons.setdefault(f"{name}/{variant}", {})[source] = {
            "delta": d.observed,
            "ci95": [d.low, d.high],
            "n": d.n,
            "clears_rule": d.observed >= MIN_GAIN and d.low > 0,
        }

    record = {
        "yardstick": "share of 5 nearest neighbours sharing a cleaned author label",
        "baseline": "/".join(baseline),
        "rule": f"switch only for a gain of at least {MIN_GAIN}, 95% CI above 0",
        "specs": {s.name: s.__dict__ for s in specs},
        "results": results,
        "vs_baseline": comparisons,
    }
    (EVAL / "embedder_comparison.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("\n  vs huBERT centred:")
    for name, per in comparisons.items():
        for source, c in per.items():
            flag = "CLEARS" if c["clears_rule"] else ""
            print(
                f"   {name:<18} {source:<8} Δ {c['delta']:+.3f}  "
                f"[{c['ci95'][0]:+.3f}, {c['ci95'][1]:+.3f}] {flag}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
