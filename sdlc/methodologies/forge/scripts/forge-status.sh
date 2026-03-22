#!/usr/bin/env bash
set -euo pipefail

CHARGE_FILE="forge/charge.md"
EMBER_DIR="ember-logs"
JOURNAL_DIR="forge/journal"
TODAY=$(date +%Y-%m-%d)

echo "=== Forge Status ==="
echo "Date: ${TODAY}"
echo ""

if [[ -f "$CHARGE_FILE" ]]; then
  echo "--- Current Charge ---"
  PLANNED=$(grep -c '| planned |' "$CHARGE_FILE" 2>/dev/null || echo 0)
  IN_PROGRESS=$(grep -c '| in-progress |' "$CHARGE_FILE" 2>/dev/null || echo 0)
  DONE=$(grep -c '| done |' "$CHARGE_FILE" 2>/dev/null || echo 0)
  BLOCKED=$(grep -c '| blocked |' "$CHARGE_FILE" 2>/dev/null || echo 0)
  BANKED=$(grep -c '| banked |' "$CHARGE_FILE" 2>/dev/null || echo 0)
  TOTAL=$((PLANNED + IN_PROGRESS + DONE + BLOCKED + BANKED))
  echo "  Planned:     ${PLANNED}"
  echo "  In progress: ${IN_PROGRESS}"
  echo "  Done:        ${DONE}"
  echo "  Blocked:     ${BLOCKED}"
  echo "  Banked:      ${BANKED}"
  echo "  Total:       ${TOTAL}"
  if [[ $TOTAL -gt 0 ]]; then
    PCT=$((DONE * 100 / TOTAL))
    echo "  Completion:  ${PCT}%"
  fi
else
  echo "No Charge file found."
fi

echo ""

if [[ -d "$EMBER_DIR" ]]; then
  EMBER_COUNT=$(find "$EMBER_DIR" -name '*.md' -type f | wc -l)
  TODAY_ENTRIES=0
  if [[ -f "${EMBER_DIR}/${TODAY}.md" ]]; then
    TODAY_ENTRIES=$(grep -c '^## Decision:' "${EMBER_DIR}/${TODAY}.md" 2>/dev/null || echo 0)
  fi
  echo "--- Ember Log ---"
  echo "  Total log files: ${EMBER_COUNT}"
  echo "  Today's entries: ${TODAY_ENTRIES}"
else
  echo "No Ember Log directory found."
fi

echo ""

if [[ -d "$JOURNAL_DIR" ]]; then
  JOURNAL_COUNT=$(find "$JOURNAL_DIR" -name '*.md' -type f | wc -l)
  echo "--- Journals ---"
  echo "  Total journals: ${JOURNAL_COUNT}"
  if [[ -f "${JOURNAL_DIR}/${TODAY}.md" ]]; then
    echo "  Today's journal: exists"
  else
    echo "  Today's journal: not yet created"
  fi
else
  echo "No journal directory found."
fi

echo ""
echo "=== End Forge Status ==="
