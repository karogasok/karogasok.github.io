#!/usr/bin/env bash
# Install the same Hugo the deploy workflow uses, into ~/.local/bin.
#
# The version is read out of .github/workflows/deploy.yml rather than repeated
# here, so there is exactly one number to bump and a local build cannot quietly
# differ from CI.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
version=$(grep -oP 'HUGO_VERSION:\s*\K[0-9.]+' "$root/.github/workflows/deploy.yml")
[ -n "$version" ] || { echo "install_hugo: could not read HUGO_VERSION from the workflow" >&2; exit 1; }

if command -v hugo >/dev/null && hugo version | grep -q "v${version}"; then
  echo "install_hugo: hugo ${version} already installed"; exit 0
fi

mkdir -p "$HOME/.local/bin"
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
curl -sSL -o "$tmp/hugo.tar.gz" \
  "https://github.com/gohugoio/hugo/releases/download/v${version}/hugo_${version}_linux-amd64.tar.gz"
tar xzf "$tmp/hugo.tar.gz" -C "$tmp" hugo
install -m755 "$tmp/hugo" "$HOME/.local/bin/hugo"
echo "install_hugo: installed hugo ${version} to ~/.local/bin"
