#!/usr/bin/env bash
# Assert the two things about this site that break silently.
#
# Both failures look exactly like success: the site builds, the pages render,
# and nothing complains. The only way to notice is to check, so the build
# checks.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
public="$root/public"
feed="$public/index.xml"
fail=0

[ -d "$public" ] || { echo "check_build: $public not found — build the site first" >&2; exit 1; }

# 1. The site feed carries the daily posts and nothing else.
#
# content/archivum/ holds several hundred imported files. Hugo's default home
# feed includes every regular page, so without the filter in
# layouts/index.rss.xml the whole archive would be published to subscribers in
# one burst — once, and irreversibly.
[ -f "$feed" ] || { echo "check_build: $feed not found" >&2; exit 1; }
items=$(grep -c '<item>' "$feed" || true)
archive_in_feed=$(grep -c '/archivum/' "$feed" || true)
posts=$(find "$root/content/posts" -name '*.md' ! -name '_index.md' | wc -l)

# The Kereső Világ entries are somebody else's writing, shown here as a lead and
# a link. They must never be syndicated as though they were this site's posts.
external_in_feed=$(grep -c 'kereses.blog.hu' "$feed" || true)

if [ "$archive_in_feed" -ne 0 ]; then
  echo "FAIL  feed: $archive_in_feed archive URLs in public/index.xml" >&2
  echo "      layouts/index.rss.xml must filter to the posts section only." >&2
  fail=1
elif [ "$external_in_feed" -ne 0 ]; then
  echo "FAIL  feed: $external_in_feed kereses.blog.hu URLs in public/index.xml" >&2
  echo "      Those posts are not ours to syndicate." >&2
  fail=1
else
  echo "OK    feed: $items items, no archive or external URLs (from $posts post files)"
fi

# Exactly two feeds, no more. The regi_cimke taxonomy was quietly publishing 94
# of them — every one full of archive posts, advertised nowhere, findable only by
# guessing a URL. Checking one file was why that went unseen for so long.
feeds=$(find "$public" -name '*.xml' ! -name 'sitemap*.xml' | sort)
feed_count=$(printf '%s\n' "$feeds" | grep -c . || true)
if [ "$feed_count" -ne 2 ]; then
  echo "FAIL  feeds: expected 2 (site + posts), found $feed_count" >&2
  printf '        %s\n' $feeds >&2
  fail=1
else
  echo "OK    feeds: exactly 2 — the site feed and the posts feed"
fi

# Those entries must also not have become pages of their own.
# `|| true` because grep exits 1 when it matches nothing, and pipefail would
# turn "no such pages exist" — the result we want — into a failed script.
ext_pages=$( { grep -rl 'rel=canonical href=https://kereses.blog.hu' "$public" --include='*.html' 2>/dev/null || true; } | wc -l)
if [ "$ext_pages" -ne 0 ]; then
  echo "FAIL  external: $ext_pages page(s) built for kereses.blog.hu content" >&2
  echo "      Those are link-only entries in data/kereses.yaml, not content." >&2
  fail=1
else
  echo "OK    external: no pages built for content the author does not own"
fi

# 2. A future publishDate stays out of the built site.
#
# This is the whole scheduling mechanism. Setting buildFuture, or Hugo changing
# its default, would publish every queued post at once with no other symptom.
future=$(grep -rl --include='*.md' -E '^publishDate: *(20[3-9][0-9]|2[1-9][0-9]{2})' "$root/content" 2>/dev/null | wc -l)
if [ "$future" -gt 0 ]; then
  leaked=0
  while IFS= read -r f; do
    title=$(grep -m1 '^title:' "$f" | sed -E 's/^title: *"?(.*[^"])"?$/\1/')
    if grep -rqF "$title" "$public" --include='*.html' 2>/dev/null; then
      echo "FAIL  scheduling: future-dated post is live — $f" >&2
      leaked=1; fail=1
    fi
  done < <(grep -rl --include='*.md' -E '^publishDate: *(20[3-9][0-9]|2[1-9][0-9]{2})' "$root/content")
  [ "$leaked" -eq 0 ] && echo "OK    scheduling: $future future-dated post(s) correctly withheld"
else
  echo "SKIP  scheduling: no future-dated posts to check"
fi

# 3. Every theme hub is attached to its own content file.
#
# Hugo derives a taxonomy term's directory from the term itself, accents and
# all, while the permalink strips them. Naming the directory after the ASCII
# slug builds a hub that looks fine but is a different page: an auto-generated
# title-cased heading, no external writings and no review notice, because the
# template joins the data file on the title. Twelve of nineteen hubs were in
# that state and the build was green throughout. Compare the rendered headings
# against the names in data/temak.yaml.
if [ -f "$root/data/temak.yaml" ] && [ -d "$public/tema" ]; then
  names=$(grep -E '^  nev: ' "$root/data/temak.yaml" | sed -E 's/^  nev: "?(.*[^"])"?$/\1/')
  bad=0; checked=0
  for page in "$public"/tema/*/index.html; do
    [ -f "$page" ] || continue
    # An alias redirect page has no heading, and pipefail would abort here.
    h1=$(grep -o '<h1>[^<]*</h1>' "$page" 2>/dev/null | head -1 | sed 's/<[^>]*>//g' || true)
    # Alias redirect pages carry no heading.
    [ -z "$h1" ] && continue
    checked=$((checked + 1))
    if ! printf '%s\n' "$names" | grep -qxF "$h1"; then
      echo "FAIL  temak: hub heading '$h1' is in no data/temak.yaml entry" >&2
      echo "      The term page is not attached to content/temak/<term>/." >&2
      bad=1; fail=1
    fi
  done
  [ "$bad" -eq 0 ] && echo "OK    temak: $checked theme hub(s) attached to their content files"
fi

# 4. Every theme and keyword tag leads somewhere.
#
# Tags are generated, and their URLs are derived twice — once by the exporter
# when it decides which hubs to create, once by Hugo when it turns a term into a
# path. The two agreeing is the whole design, and when they disagree the page
# still builds: the tag just 404s. Hugo strips accents and case for the URL, so
# `média` and `media` collide there while being distinct terms; that is how this
# check earned its place.
if [ -d "$public/tema" ] || [ -d "$public/kulcsszo" ]; then
  links=$(grep -rhoE 'href="/(tema|kulcsszo)/[^"]*"' "$public" --include='*.html' 2>/dev/null \
          | sed 's/^href="//;s/"$//' | sort -u)
  total=$(printf '%s\n' "$links" | grep -c . || true)
  broken=0
  while IFS= read -r href; do
    [ -z "$href" ] && continue
    target="$public${href}index.html"
    if [ ! -f "$target" ]; then
      [ "$broken" -lt 5 ] && echo "FAIL  tags: $href is linked but was never built" >&2
      broken=$((broken + 1)); fail=1
    fi
  done < <(printf '%s\n' "$links")
  if [ "$broken" -eq 0 ]; then
    echo "OK    tags: all $total theme and keyword links resolve"
  else
    echo "FAIL  tags: $broken of $total links are dead" >&2
  fi
fi

exit $fail
