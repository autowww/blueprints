#!/usr/bin/env bash
set -euo pipefail

EMBER_DIR="ember-logs"
TODAY=$(date +%Y-%m-%d)
EMBER_FILE="${EMBER_DIR}/${TODAY}.md"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="${SCRIPT_DIR}/../daily/ember-log-entry.template.md"

usage() {
  echo "Usage: $0 \"Decision summary\" [--type TYPE] [--refs SPARK_REFS]"
  echo ""
  echo "Appends an Ember Log entry to ${EMBER_DIR}/${TODAY}.md"
  echo ""
  echo "Options:"
  echo "  --type TYPE     Decision type: trade-off, assumption, risk-acceptance,"
  echo "                  scope-change, bank, technical (default: trade-off)"
  echo "  --refs REFS     Comma-separated Spark references (e.g. M1E1S1,M1E1S2)"
  exit 1
}

if [[ $# -lt 1 ]] || [[ "$1" == "--help" ]]; then
  usage
fi

SUMMARY="$1"
shift

DECISION_TYPE="trade-off"
SPARK_REFS=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --type) DECISION_TYPE="$2"; shift 2 ;;
    --refs) SPARK_REFS="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; usage ;;
  esac
done

mkdir -p "$EMBER_DIR"

if [[ ! -f "$EMBER_FILE" ]]; then
  cat > "$EMBER_FILE" <<EOF
---
date: ${TODAY}
---

# Ember Log — ${TODAY}

EOF
  echo "Created Ember Log for ${TODAY}"
fi

REFS_YAML="[]"
if [[ -n "$SPARK_REFS" ]]; then
  REFS_YAML="[$(echo "$SPARK_REFS" | sed 's/,/, /g')]"
fi

cat >> "$EMBER_FILE" <<EOF

---
<!-- spark_refs: ${REFS_YAML} | decision_type: ${DECISION_TYPE} -->

## Decision: ${SUMMARY}

**Context:** <!-- what prompted this decision -->

**Alternatives considered:**

1. <!-- option A — pros/cons -->
2. <!-- option B — pros/cons -->

**Decision:** <!-- what was chosen and why -->

**Assumptions at risk:**

- <!-- assumption that could invalidate this decision -->

**Evidence still needed:**

- <!-- what would confirm or refute the decision -->

**Revisit trigger:** <!-- when to revisit -->

EOF

echo "Appended Ember Log entry: ${SUMMARY}"
echo "Edit: ${EMBER_FILE}"
