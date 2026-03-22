#!/usr/bin/env bash
set -euo pipefail

JOURNAL_DIR="forge/journal"
TODAY=$(date +%Y-%m-%d)
JOURNAL_FILE="${JOURNAL_DIR}/${TODAY}.md"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="${SCRIPT_DIR}/../daily/day-journal.template.md"

usage() {
  echo "Usage: $0 [new|commit]"
  echo ""
  echo "Commands:"
  echo "  new       Create today's journal from template (default)"
  echo "  commit    Stage and commit today's journal + Charge + Ember Log"
  exit 1
}

cmd="${1:-new}"

case "$cmd" in
  new)
    mkdir -p "$JOURNAL_DIR"
    if [[ -f "$JOURNAL_FILE" ]]; then
      echo "Journal already exists: ${JOURNAL_FILE}"
      exit 0
    fi
    if [[ -f "$TEMPLATE" ]]; then
      sed "s/YYYY-MM-DD/${TODAY}/g" "$TEMPLATE" > "$JOURNAL_FILE"
    else
      cat > "$JOURNAL_FILE" <<EOF
---
date: ${TODAY}
iteration:
---

# Journal — ${TODAY}

## Hat transitions

| Time | Hat | Activity |
|------|-----|----------|

## Sparks completed

| Spark ID | Phase | Outcome |
|----------|-------|---------|

## Bellows challenges invoked

| Discipline | Work item | Key concern | Action taken |
|------------|-----------|-------------|--------------|

## Learnings

## Tomorrow's focus

EOF
    fi
    echo "Created journal: ${JOURNAL_FILE}"
    ;;
  commit)
    FILES_TO_STAGE=""
    [[ -f "$JOURNAL_FILE" ]] && FILES_TO_STAGE="$JOURNAL_FILE"
    [[ -f "forge/charge.md" ]] && FILES_TO_STAGE="${FILES_TO_STAGE} forge/charge.md"
    [[ -f "ember-logs/${TODAY}.md" ]] && FILES_TO_STAGE="${FILES_TO_STAGE} ember-logs/${TODAY}.md"

    if [[ -z "$FILES_TO_STAGE" ]]; then
      echo "No Forge files to commit for ${TODAY}."
      exit 0
    fi

    git add $FILES_TO_STAGE
    git commit -m "forge: daily journal ${TODAY}" || echo "Nothing to commit."
    echo "Committed Forge daily artifacts for ${TODAY}"
    ;;
  *)
    usage
    ;;
esac
