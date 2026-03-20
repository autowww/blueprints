#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_URL="https://github.com/autowww/blueprints.wiki.git"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

git clone "$WIKI_URL" "$TMP/wiki"
cd "$TMP/wiki"

cp "$ROOT/wiki-source/Home.md" "$ROOT/wiki-source/_Sidebar.md" .

git add Home.md _Sidebar.md
if git diff --staged --quiet; then
  echo "Wiki already matches wiki-source/ (nothing to commit)."
  exit 0
fi

git commit -m "Sync wiki from blueprints wiki-source"
git push
