#!/usr/bin/env bash
set -euo pipefail

CHARGE_DIR="forge"
CHARGE_FILE="${CHARGE_DIR}/charge.md"
TODAY=$(date +%Y-%m-%d)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="${SCRIPT_DIR}/../daily/charge.template.md"

usage() {
  echo "Usage: $0 [show|new|done SPARK_ID|block SPARK_ID|bank SPARK_ID]"
  echo ""
  echo "Commands:"
  echo "  show              Show today's Charge (default)"
  echo "  new               Create a new Charge file for today from template"
  echo "  done SPARK_ID     Mark a Spark as done in the Charge"
  echo "  block SPARK_ID    Mark a Spark as blocked"
  echo "  bank SPARK_ID     Mark a Spark as banked"
  exit 1
}

ensure_dir() {
  if [[ ! -d "$CHARGE_DIR" ]]; then
    echo "Error: ${CHARGE_DIR}/ directory not found. Run the Forge setup wizard first."
    exit 1
  fi
}

cmd="${1:-show}"

case "$cmd" in
  show)
    ensure_dir
    if [[ -f "$CHARGE_FILE" ]]; then
      cat "$CHARGE_FILE"
    else
      echo "No Charge file found. Run: $0 new"
    fi
    ;;
  new)
    ensure_dir
    if [[ -f "$CHARGE_FILE" ]]; then
      ARCHIVE="${CHARGE_DIR}/charge-archive"
      mkdir -p "$ARCHIVE"
      PREV_DATE=$(head -5 "$CHARGE_FILE" | grep '^date:' | sed 's/date: //' || echo "unknown")
      mv "$CHARGE_FILE" "${ARCHIVE}/charge-${PREV_DATE}.md"
      echo "Archived previous Charge to ${ARCHIVE}/charge-${PREV_DATE}.md"
    fi
    if [[ -f "$TEMPLATE" ]]; then
      sed "s/YYYY-MM-DD/${TODAY}/g" "$TEMPLATE" > "$CHARGE_FILE"
    else
      cat > "$CHARGE_FILE" <<EOF
---
date: ${TODAY}
iteration:
hat:
---

# Charge — ${TODAY}

## Active Sparks

| # | Spark ID | Phase | Intent | Status |
|---|----------|-------|--------|--------|
| 1 | | | | planned |

## Blockers

| Spark | Blocker | Action |
|-------|---------|--------|

## Banking decisions

| Spark | Reason banked | Restart context |
|-------|---------------|-----------------|

## Notes

EOF
    fi
    echo "Created Charge for ${TODAY}: ${CHARGE_FILE}"
    ;;
  done|block|bank)
    ensure_dir
    SPARK_ID="${2:-}"
    if [[ -z "$SPARK_ID" ]]; then
      echo "Error: SPARK_ID required. Usage: $0 $cmd SPARK_ID"
      exit 1
    fi
    if [[ ! -f "$CHARGE_FILE" ]]; then
      echo "Error: No Charge file. Run: $0 new"
      exit 1
    fi
    STATUS="$cmd"
    [[ "$STATUS" == "block" ]] && STATUS="blocked"
    [[ "$STATUS" == "bank" ]] && STATUS="banked"
    if grep -q "$SPARK_ID" "$CHARGE_FILE"; then
      sed -i "s/\(.*${SPARK_ID}.*\)| [a-z-]* |/\1| ${STATUS} |/" "$CHARGE_FILE"
      echo "Marked ${SPARK_ID} as ${STATUS}"
    else
      echo "Warning: ${SPARK_ID} not found in Charge. Add it manually."
    fi
    ;;
  *)
    usage
    ;;
esac
