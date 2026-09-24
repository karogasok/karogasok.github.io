"""Freeze the tuned calibration and the gate's criteria, before the gate runs.

Committing the file this writes is the pre-registration: the thresholds, the
encoder, the theme vectors and exactly what the held-out test must show are all
fixed before a single held-out writing is placed. Nothing about them may change
afterwards without running the whole tuning again.

Usage:
    uv run python scripts/freeze.py

Reads out/kalibracio_jelolt.npz (from place.py); writes
analysis/temalista_kalibracio.json.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

from karogasok_temak.embed import spec_named

HERE = Path(__file__).resolve().parents[1]

#: What the held-out half must show, written down before it is looked at.
GATE = {
    "G1": {
        "what": "BCubed F on the held-out Kereső Világ rows beats the stronger of "
        "baseline A (as published) and B (genre themes removed)",
        "min_delta": 0.03,
        "bootstrap": {"resamples": 2000, "seed": 42, "lower_bound_above": 0.0},
    },
    "G2": {
        "min_coverage_long_pages": 0.70,
        "min_coverage_rows": 0.40,
        "mean_themes_at_most": "baseline A on the same writings",
        "max_theme_share": 0.25,
    },
    "G3": {
        "note": "The author approved the theme list without naming expected themes "
        "for the four 2026 posts, so these expectations are the assistant's, "
        "written here before the gate ran. The hard criterion stands: none of "
        "the four may be placed in Logika és matematika.",
        "forbidden_for_all": ["logika-es-matematika"],
        "expected_any_of": {
            "content/posts/2026-09-18-muslica.md": [
                "megismeres",
                "mesterseges-intelligencia",
            ],
            "content/posts/2026-09-18-cognitive-debt.md": ["programozas", "megismeres"],
            "content/posts/2026-09-23-llm-emotions.md": ["nyelvmodellek", "megismeres"],
            "content/posts/2026-09-24-jev-system-1.md": [
                "megismeres",
                "mesterseges-intelligencia",
                "nyelvmodellek",
            ],
        },
        "no_theme_counts_as": "flagged, not failed",
    },
    "if_it_fails": "The archive keeps its current placement, carried through the "
    "renames; the new method places new writing only.",
}


#: How the method changed between the first dev run and freezing — all on the
#: tuning data, none after the held-out half was touched.
CHANGES = [
    "Seed-count correction made one-sided: the first run lowered the bar for the "
    "two 3-seed themes, and Nyelvmodellek (134) and Megismerés (73) became "
    "catch-alls, taking in 2011 press reviews and Kanban book reviews.",
    "Short writings may be centred on their own mean (held-out rows excluded): "
    "with page centring, the Kereső Világ blurbs as a group leaned +0.09 towards "
    "Vizualizáció, which grew to 151. Chosen by the declared rule on dev rows.",
    "Known, left for the author: ten 2011–12 Lapszemle link roundups land in "
    "Nyelvmodellek. Affects pages only, not the gate.",
]


def main() -> int:
    """Write the frozen calibration."""
    npz = np.load(HERE / "out" / "kalibracio_jelolt.npz", allow_pickle=True)
    tuning = json.loads((HERE / "out" / "placement_tuning.json").read_text("utf-8"))
    encoder = str(npz["encoder"])
    spec = spec_named(encoder)
    themes_file = (HERE / "temalista.yaml").read_bytes()
    record = {
        "temalista_sha256": hashlib.sha256(themes_file).hexdigest(),
        "encoder": {k: getattr(spec, k) for k in spec.__dataclass_fields__},
        "theme_keys": [str(k) for k in npz["theme_keys"]],
        "seed_counts": [int(k) for k in npz["seed_counts"]],
        "tau": {"long": float(npz["tau"][0]), "short": float(npz["tau"][1])},
        "delta": float(npz["delta"]),
        "one_sided": bool(npz["one_sided"]),
        "g": {
            str(int(k)): float(v) for k, v in zip(npz["g_k"], npz["g_v"], strict=True)
        },
        "mean": [round(float(x), 6) for x in npz["mean"]],
        "mean_short": (
            [round(float(x), 6) for x in npz["mean_short"]]
            if npz["mean_short"].size > 1
            else None
        ),
        "vectors": [[round(float(x), 6) for x in row] for row in npz["vectors"]],
        "gate": GATE,
        "dev_results": tuning["encoders"][encoder],
        "baselines_dev": {
            "pages": tuning["baseline_pages"],
            "rows": tuning["baseline_rows"],
        },
        "changes_before_freezing": CHANGES,
    }
    out = HERE / "temalista_kalibracio.json"
    out.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    print(
        f"  wrote {out.name}: encoder {encoder}, τ_long {record['tau']['long']:.3f}, "
        f"τ_short {record['tau']['short']:.3f}, δ {record['delta']}"
    )
    print(
        "  commit it before running scripts/gate.py: "
        "that commit is the pre-registration"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
