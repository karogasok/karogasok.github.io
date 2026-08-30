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

if [ "$archive_in_feed" -ne 0 ]; then
  echo "FAIL  feed: $archive_in_feed archive URLs in public/index.xml" >&2
  echo "      layouts/index.rss.xml must filter to the posts section only." >&2
  fail=1
else
  echo "OK    feed: $items items, no archive URLs (from $posts post files)"
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

exit $fail
