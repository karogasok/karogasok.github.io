#!/usr/bin/env bash
# The site feed must carry the daily posts and nothing else.
#
# content/archivum/ holds several hundred imported files. Hugo's default home
# feed includes every regular page, so without a filtered layouts/index.rss.xml
# the whole archive would be published to subscribers in one burst. That failure
# is silent — the site looks fine and the feed is wrong — so it is asserted here
# rather than left to be noticed.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
feed="$root/public/index.xml"

[ -f "$feed" ] || { echo "check_feed: $feed not found — build the site first" >&2; exit 1; }

in_feed=$(grep -c '<item>' "$feed" || true)
archive_in_feed=$(grep -c '/archivum/' "$feed" || true)

echo "check_feed: $in_feed items in the site feed"

if [ "$archive_in_feed" -ne 0 ]; then
  echo "check_feed: FAIL — $archive_in_feed archive URLs found in public/index.xml" >&2
  echo "  layouts/index.rss.xml must filter to the posts section only." >&2
  exit 1
fi

echo "check_feed: OK — no archive URLs in the site feed"
