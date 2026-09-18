"""Show how multi-labelling behaves at different floors. Writes nothing.

This is a gate, not a step. The floor decides how many themes each writing
carries, which decides what the archive filter and the theme network are made
of — so it gets looked at before anything downstream is generated, and the
number that is chosen gets recorded rather than defaulted.

Usage:
    uv run python scripts/report_multilabel.py [--floors 0.05,0.10,0.15,0.20]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

from karogasok_temak.topics import (
    MULTI_LABEL_CAP,
    MULTI_LABEL_FLOOR,
    MULTI_LABEL_RATIO,
    OUTLIER,
    as_mixture,
    label_set,
    label_spread,
    labels_above,
)

OUT = Path(__file__).resolve().parents[1] / "out"

#: How many of the most-labelled documents to name.
N_EXAMPLES = 10


def main() -> int:
    """Print the label-spread table."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--floors", default="0.05,0.10,0.15,0.20,0.25")
    args = parser.parse_args()
    floors = [float(value) for value in args.floors.split(",")]

    topics_path = OUT / "topics.json"
    matrix_path = OUT / "probabilities.npz"
    if not topics_path.exists() or not matrix_path.exists():
        print("run scripts/fit_topics.py first")
        return 1
    topics = json.loads(topics_path.read_text(encoding="utf-8"))
    stored = np.load(matrix_path, allow_pickle=True)
    doc_ids = [str(d) for d in stored["doc_ids"]]
    columns = [int(c) for c in stored["columns"]]
    # Reported in mixture shares, which is what the floor is expressed in.
    matrix = [as_mixture(row) for row in stored["matrix"]]
    primaries = [
        int(topics["assignments"][doc_id]["topic_reduced"]) for doc_id in doc_ids
    ]

    print(f"{len(doc_ids)} documents, {len(columns)} topics\n")
    header = "floor  cap  ratio |" + "".join(f"{n:>6}" for n in range(6))
    print(header)
    print("-" * len(header))

    for floor in floors:
        # Uncapped and ungated: what the floor alone does.
        raw = [labels_above(row, columns, floor=floor) for row in matrix]
        spread = label_spread([[t for t, _ in labels] for labels in raw])
        counts = "".join(f"{spread.counts.get(n, 0):>6}" for n in range(6))
        over = sum(1 for labels in raw if len(labels) > MULTI_LABEL_CAP)
        print(
            f"{floor:>5.2f}   -     -   |{counts}"
            f"   mean {spread.mean:.2f}  cover {spread.coverage:.1%}"
            f"  max {spread.largest}  over-cap {over}"
        )

    print()
    for floor in floors:
        gated = [
            label_set(row, columns, primary, floor=floor)[0]
            for row, primary in zip(matrix, primaries, strict=True)
        ]
        spread = label_spread(gated)
        counts = "".join(f"{spread.counts.get(n, 0):>6}" for n in range(6))
        print(
            f"{floor:>5.2f} {MULTI_LABEL_CAP:>4} {MULTI_LABEL_RATIO:>5} |{counts}"
            f"   mean {spread.mean:.2f}  cover {spread.coverage:.1%}"
            f"  max {spread.largest}"
        )

    print(f"\nmost-labelled documents at floor {MULTI_LABEL_FLOOR}:")
    names = {}
    names_path = OUT / "topic_names.json"
    if names_path.exists():
        names = {
            int(k): v["name"]
            for k, v in json.loads(names_path.read_text(encoding="utf-8")).items()
        }
    ranked = sorted(
        zip(doc_ids, matrix, primaries, strict=True),
        key=lambda triple: (
            -len(label_set(triple[1], columns, triple[2], floor=MULTI_LABEL_FLOOR)[0])
        ),
    )
    for doc_id, row, primary in ranked[:N_EXAMPLES]:
        ids, scores = label_set(row, columns, primary, floor=MULTI_LABEL_FLOOR)
        if len(ids) < 2:
            continue
        labelled = ", ".join(
            f"{names.get(t, t)} {s:.2f}" for t, s in zip(ids, scores, strict=True)
        )
        marker = " (outlier promoted)" if primary == OUTLIER else ""
        print(f"  {doc_id.split('/')[-1][:44]:<44} {labelled}{marker}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
