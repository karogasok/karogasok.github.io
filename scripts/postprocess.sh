#!/usr/bin/env bash
#
# Put the model's themes and keywords onto a writing, and into the site.
#
#   scripts/postprocess.sh content/posts/2026-09-18-muslica.md
#   scripts/postprocess.sh 2026-09-18-muslica.md        # bare filename works too
#   scripts/postprocess.sh                              # everything not yet done
#
# Three steps have to happen in order and none of them is interesting: emtsv has
# to be running to lemmatise, infer.py places the piece on the existing themes,
# and export_temak.py writes the result into the front matter and the data files.
# Doing them by hand is how one gets forgotten.
#
# emtsv is started if it is not already up and is left running, because starting
# it costs about forty seconds and you will usually postprocess more than once.
# `make emtsv-down` stops it.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
analysis="$root/analysis"

if [ ! -f "$analysis/out/model.pkl" ]; then
  echo "nincs betanított modell: $analysis/out/model.pkl" >&2
  echo "  előbb: cd analysis && uv run python scripts/fit_topics.py" >&2
  exit 1
fi

# A removed video answers 200, and so does a half-started analyser; ask it
# something and see whether it answers.
if ! curl -fsS --max-time 5 -F "text=teszt." http://127.0.0.1:5000/tok/morph/pos \
     > /dev/null 2>&1; then
  echo "emtsv nem fut — indítom"
  make -C "$analysis" emtsv-up > /dev/null
  printf "  betöltés"
  for _ in $(seq 1 30); do
    if curl -fsS --max-time 30 -F "text=teszt." \
         http://127.0.0.1:5000/tok/morph/pos > /dev/null 2>&1; then
      echo " kész"
      break
    fi
    printf "."
    sleep 5
  done
fi

cd "$analysis"
uv run python scripts/infer.py "$@"
uv run python scripts/export_temak.py --allow-unchecked

echo
echo "kész. A címkék a bejegyzés front matterében vannak."
echo "  az emtsv fut még — 'make -C analysis emtsv-down' állítja le"
