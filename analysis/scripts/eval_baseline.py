"""Score the current theme placement against the author's labels.

Writes nothing but analysis/eval/baseline_scores.json.

Two baselines, because the new method has to beat the stronger of them:

* **A** — the placement as published;
* **B** — the same with the four genre themes removed. Dropping genre labels from
  the yardstick already tilts the field towards a subject-only method, so the
  new method must also beat a baseline that has had the same courtesy.

Scored on the tuning half only. The held-out half of the Kereső Világ rows is not
touched here.

Usage:
    uv run python scripts/eval_baseline.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from karogasok_temak.evaluate import (
    bcubed,
    clean_labels,
    load_label_rules,
    split_of,
)
from karogasok_temak.gold import archive_labels, kereses_labels

HERE = Path(__file__).resolve().parents[1]
EVAL = HERE / "eval"

#: The themes that name a kind of post rather than a subject.
GENRE_THEMES = frozenset(
    {"Lapszemle", "NLP meetupok", "A blog életéről", "Kurzusok és önképzés"}
)


def main() -> int:
    """Compute and record the baseline scores."""
    rules = load_label_rules(EVAL / "cimke_normalizalas.yaml")
    base = json.loads((EVAL / "baseline_2026-09.json").read_text(encoding="utf-8"))

    gold = {
        "oldalak": clean_labels(archive_labels(), rules),
        "sorok": clean_labels(kereses_labels(), rules),
    }
    dev = {
        "oldalak": sorted(gold["oldalak"]),
        "sorok": sorted(k for k in gold["sorok"] if split_of(k) == "dev"),
    }
    held_out = sum(1 for k in gold["sorok"] if split_of(k) == "test")

    record: dict[str, object] = {"held_out_rows_untouched": held_out}
    for source in ("oldalak", "sorok"):
        placed = base[source]
        without_genre = {
            k: [t for t in v if t not in GENRE_THEMES] for k, v in placed.items()
        }
        items = dev[source]
        a = bcubed(placed, gold[source], items)
        b = bcubed(without_genre, gold[source], items)
        labels_per = sum(len(placed.get(k, [])) for k in items) / len(items)
        record[source] = {
            "n_scored": a.n,
            "distinct_labels": len({x for k in items for x in gold[source][k]}),
            "A_current": {
                "P": a.precision,
                "R": a.recall,
                "F": a.f,
                "unplaced": a.unplaced,
            },
            "B_no_genre_themes": {
                "P": b.precision,
                "R": b.recall,
                "F": b.f,
                "unplaced": b.unplaced,
            },
            "mean_themes_per_writing": labels_per,
        }
        print(
            f"  {source:<8} n={a.n:<4} labels={record[source]['distinct_labels']:<4} "
            f"A: F={a.f:.3f} (P {a.precision:.3f} R {a.recall:.3f}) "
            f"B: F={b.f:.3f} (P {b.precision:.3f} R {b.recall:.3f}) "
            f"themes/writing {labels_per:.2f}"
        )
    (EVAL / "baseline_scores.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  held-out rows, not scored: {held_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
