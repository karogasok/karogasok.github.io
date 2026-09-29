"""Add new themes to the frozen calibration without re-tuning it.

A new theme needs a vector — the mean of its seeds, centred like everything
else — and nothing more: the centring, the thresholds, δ and the seed-count
curve were tuned on the whole list and stay frozen. So adding a theme moves only
the writings that now fit it better; every other placement stays where it was.

This is deliberately narrow. It refuses if a theme was removed, and — unless
``--reseed`` is given — if an existing theme's seeds changed, because its vector
would move and with it every writing near it. ``--reseed`` is for replacing a
seed that should never have been one (a guest post, say) with another of the
author's writings: the vector moves, the thresholds do not. The gate result
was measured on the list as it was frozen; each extension is recorded in the
calibration file under ``changes_after_gate``, so nobody mistakes the gate's
numbers for a measurement of the extended list.

Usage:
    uv run python scripts/extend_themes.py [--reseed]
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

from karogasok_temak import themes as theme_list
from karogasok_temak.assign import key_of
from karogasok_temak.corpus import load_corpus
from karogasok_temak.embed import EncoderSpec, encode_cached
from karogasok_temak.placement import theme_vectors, unit

HERE = Path(__file__).resolve().parents[1]
FROZEN = HERE / "temalista_kalibracio.json"
THEMES = HERE / "temalista.yaml"

#: How far a recomputed vector of an existing theme may drift from the frozen
#: one — the frozen file stores six decimals, so anything beyond rounding means
#: its seeds changed.
TOLERANCE = 1e-4


def main() -> int:
    """Append vectors for new themes, and with --reseed recompute changed ones."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reseed",
        action="store_true",
        help="allow existing themes whose seeds changed to get new vectors",
    )
    args = parser.parse_args()
    record = json.loads(FROZEN.read_text(encoding="utf-8"))
    active = [t for t in theme_list.load(THEMES) if t.allapot == "aktiv"]
    frozen_keys = list(record["theme_keys"])
    keys = [t.kulcs for t in active]
    missing = [k for k in frozen_keys if k not in keys]
    if missing:
        print(
            f"  theme(s) removed or deactivated: {missing} — run place.py + freeze.py"
        )
        return 1
    new = [t for t in active if t.kulcs not in frozen_keys]

    spec = EncoderSpec(**record["encoder"])
    mean = np.array(record["mean"])
    by_key = {key_of(d): d for d in load_corpus() if d.text.strip()}
    seeds = sorted({s for t in active for s in t.magok})
    raw = encode_cached(spec, [by_key[s].text for s in seeds])
    centred = dict(zip(seeds, unit(raw - mean), strict=True))
    vectors = theme_vectors(centred, [t.magok for t in active])

    frozen = np.array(record["vectors"])
    reseeded: dict[str, float] = {}
    for i, key in enumerate(frozen_keys):
        drift = float(np.abs(vectors[keys.index(key)] - frozen[i]).max())
        if drift > TOLERANCE and args.reseed:
            reseeded[key] = round(float(vectors[keys.index(key)] @ frozen[i]), 4)
        elif drift > TOLERANCE:
            print(
                f"  {key}: seeds changed (vector drift {drift:.2e}) — "
                "run place.py + freeze.py"
            )
            return 1

    if not new and not reseeded:
        print("  no new or re-seeded theme — nothing to do.")
        return 0

    order = frozen_keys + [t.kulcs for t in new]
    record["theme_keys"] = order
    record["vectors"] = [
        [round(float(x), 6) for x in vectors[keys.index(k)]] for k in order
    ]
    record["seed_counts"] = [
        len(next(t for t in active if t.kulcs == k).magok) for k in order
    ]
    record["temalista_sha256"] = hashlib.sha256(THEMES.read_bytes()).hexdigest()
    record.setdefault("changes_after_gate", []).append(
        {
            "date": dt.date.today().isoformat(),
            "added": [t.kulcs for t in new],
            "reseeded": {
                k: {
                    "seeds": list(next(t for t in active if t.kulcs == k).magok),
                    "cosine_to_previous_vector": c,
                }
                for k, c in reseeded.items()
            },
            "seeds": {t.kulcs: list(t.magok) for t in new},
            "note": "Theme vectors appended or recomputed from their seeds; "
            "centring, thresholds, delta and the seed-count curve unchanged. The "
            "gate result was measured on the list before this change.",
        }
    )
    FROZEN.write_text(
        json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    for key, c in reseeded.items():
        print(f"  re-seeded {key}: cosine to its previous vector {c:.3f}")
    if new:
        print(f"  added {', '.join(t.kulcs for t in new)}")
    print(f"  {len(order)} themes frozen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
