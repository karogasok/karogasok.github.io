# Varjú Károgások.
#
# `make new t="a cím"` starts a post. Everything else is build and check.

HUGO ?= hugo
DATE := $(shell date +%Y-%m-%d)

.PHONY: help new serve build check clean fonts og import-blogspot import-wordpress import-kereses prune-media

help:
	@echo "make new t=\"a bejegyzés címe\"   új bejegyzés a mai dátummal"
	@echo "make serve                       helyi szerver, piszkozatokkal együtt"
	@echo "make build                       éles build a public/ könyvtárba"
	@echo "make check                       build + a feed és az ütemezés ellenőrzése"
	@echo "make fonts                       betűkészletek újratöltése"
	@echo "make og                          OG-kártyák generálása"
	@echo "make import-blogspot             Blogspot archívum importálása"
	@echo "make import-wordpress            WordPress archívum importálása"
	@echo "make import-kereses              Kereső Világ bejegyzések listája"
	@echo "make prune-media                 hivatkozatlan archív képek törlése"

# One command to start a post. The filename carries the date so the directory
# sorts chronologically; the URL does not use it.
new:
	@test -n "$(t)" || { echo 'kell egy cím: make new t="a cím"'; exit 1; }
	@slug=$$(printf '%s' "$(t)" | iconv -f utf8 -t ascii//TRANSLIT 2>/dev/null | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$$//g'); \
	  $(HUGO) new "posts/$(DATE)-$$slug.md" && \
	  sed -i "s|^title: \"\"|title: \"$(t)\"|" "content/posts/$(DATE)-$$slug.md" && \
	  echo "content/posts/$(DATE)-$$slug.md"

serve:
	$(HUGO) server --buildDrafts --disableFastRender

build:
	$(HUGO) --gc --minify

check: build
	./scripts/check_build.sh

fonts:
	python3 scripts/fetch_fonts.py

og:
	python3 scripts/make_og.py

import-blogspot:
	python3 scripts/import_blogspot.py

import-wordpress:
	python3 scripts/import_wordpress.py

# Nem importál, csak listáz: a Kereső Világ tartalma nem a szerzőé, ezért
# ebből csak lead + hivatkozás kerül a data/kereses.yaml fájlba.
import-kereses:
	python3 scripts/import_kereses.py

# An import only ever adds files. This is the other half: anything in
# static/archivum/img/ that no post mentions any more gets removed.
prune-media:
	python3 scripts/prune_media.py

clean:
	rm -rf public resources/_gen
