#!/usr/bin/env bash
# Mirror blueprint Markdown into GitHub Wiki (autowww/blueprints.wiki).
# Prerequisite: Wiki tab → create first page "Home" once so the wiki git repo exists.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_URL="${WIKI_URL:-https://github.com/autowww/blueprints.wiki.git}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

export BLUEPRINTS_ROOT="$ROOT"
export WIKI_STAGE="$TMP/stage"
python3 "$ROOT/wiki-source/sync_markdown.py"

cp "$ROOT/wiki-source/Home.md" "$TMP/stage/Home.md"

git clone "$WIKI_URL" "$TMP/wiki"
cd "$TMP/wiki"

# Drop previous mirror (keep only git metadata); re-add everything from stage
shopt -s dotglob nullglob
for p in *; do
  [[ "$p" == ".git" ]] && continue
  rm -rf "$p"
done
shopt -u dotglob

cp -a "$TMP/stage/"* .

git add -A
if git diff --staged --quiet; then
  echo "Wiki already up to date (nothing to commit)."
  exit 0
fi

git commit -m "Sync wiki from blueprints (markdown mirror + sidebar)"
git push

echo "Done. Open https://github.com/autowww/blueprints/wiki"
