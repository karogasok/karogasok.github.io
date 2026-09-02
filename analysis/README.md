# karogasok-temak

Topic model, keywords and themes over the Varjú Károgások corpus.

Separate from `../scripts/`, which is stdlib-only on purpose so the archive
importers still run years from now with a bare `python3`. This project has the
heavy ML stack; keeping them apart is what stops that stack leaking into the
importers.

## Run it

```sh
uv sync --all-extras
make emtsv-up                                   # docker; first request loads the analyser
uv run python scripts/lemmatise.py              # ~7 min, resumable, caches to out/
uv run python scripts/extract_keywords.py       # ~3 min
uv run python scripts/fit_topics.py             # ~7 min, embeddings cached
make emtsv-down
# then review out/topic_names.json and set checked_by_human: true
uv run python scripts/export_temak.py
```

Every step writes to `out/` and reads what the previous one left, so any of them
can be re-run alone. `lemmatise.py` skips documents already cached; `fit_topics.py`
re-uses cached embeddings unless the document texts themselves changed.

Docker's bridge networking does not work on this machine — `-p 5000:5000` fails
to create the veth pair — so `make emtsv-up` uses `--network host`.

## What it does

1. Reads the corpus out of `../content/` and `../data/`, keeping provenance.
2. Lemmatises through emtsv (`/tok/morph/pos`), keeping content words only.
3. Embeds with huBERT — chunked to 128 tokens, mean-pooled, L2-normalised.
4. Fits BERTopic on the full-text documents, then assigns the short ones.
5. Extracts per-document keywords with `keyflux` keyness.
6. Writes `../data/temak.yaml` and the front-matter tags — but only for themes
   you have marked `checked_by_human: true`. A name proposed by a model is a
   draft, and drafts do not become site navigation on their own.
