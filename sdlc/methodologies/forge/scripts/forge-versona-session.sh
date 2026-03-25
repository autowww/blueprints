#!/usr/bin/env bash
set -euo pipefail

# Creates forge-logs/versona/<actor>/<session-id>/ with SESSION.md from template.
# Run from consuming repository root (same convention as forge-ember.sh).

BASE_DIR="forge-logs/versona"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="${SCRIPT_DIR}/../../../templates/forge/versona-session.template.md"
MANIFEST_TEMPLATE="${SCRIPT_DIR}/../../../templates/forge/session.manifest.yaml.template"

usage() {
  echo "Usage: $0 <actor> [session-id] [--with-yaml-manifest]"
  echo ""
  echo "Creates:"
  echo "  ${BASE_DIR}/<actor>/<session-id>/SESSION.md"
  echo "  inputs/ and outputs/ subdirectories"
  echo ""
  echo "If session-id is omitted, generates: YYYYMMDD-HHMMSS-<random4>"
  echo ""
  echo "  --with-yaml-manifest  Also copy session.manifest.yaml.template → session.manifest.yaml"
  exit 1
}

if [[ $# -lt 1 ]] || [[ "$1" == "--help" ]]; then
  usage
fi

ACTOR="$1"
shift

WITH_YAML=false
SESSION_ID=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --with-yaml-manifest) WITH_YAML=true; shift ;;
    *)
      if [[ -z "$SESSION_ID" ]]; then
        SESSION_ID="$1"
        shift
      else
        usage
      fi
      ;;
  esac
done

if [[ -z "$SESSION_ID" ]]; then
  if command -v openssl >/dev/null 2>&1; then
    RAND=$(openssl rand -hex 2)
  else
    RAND=$(printf '%04x' "$RANDOM")
  fi
  SESSION_ID="$(date -u +%Y%m%d-%H%M%S)-${RAND}"
fi

# Sanitize actor and session id for single path segment (no slashes)
if [[ "$ACTOR" == *"/"* ]] || [[ "$SESSION_ID" == *"/"* ]]; then
  echo "Error: actor and session-id must not contain '/'."
  exit 1
fi

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TODAY_JOURNAL=$(date +%Y-%m-%d)

SESSION_DIR="${BASE_DIR}/${ACTOR}/${SESSION_ID}"

if [[ -e "$SESSION_DIR" ]]; then
  echo "Error: already exists: ${SESSION_DIR}"
  exit 1
fi

if [[ ! -f "$TEMPLATE" ]]; then
  echo "Error: template not found: ${TEMPLATE}"
  exit 1
fi

mkdir -p "${SESSION_DIR}/inputs" "${SESSION_DIR}/outputs"

sed -e "s/<session-id>/${SESSION_ID}/g" \
    -e "s/<actor>/${ACTOR}/g" \
    -e "s/YYYY-MM-DDTHH:MM:SSZ/${STARTED}/g" \
    "$TEMPLATE" > "${SESSION_DIR}/SESSION.md"

if [[ "$WITH_YAML" == true ]]; then
  if [[ ! -f "$MANIFEST_TEMPLATE" ]]; then
    echo "Error: manifest template not found: ${MANIFEST_TEMPLATE}"
    exit 1
  fi
  sed -e "s/<session-id>/${SESSION_ID}/g" \
      -e "s/YYYY-MM-DDTHH:MM:SSZ/${STARTED}/g" \
      "$MANIFEST_TEMPLATE" > "${SESSION_DIR}/session.manifest.yaml"
fi

echo "Created: ${SESSION_DIR}"
echo "Edit: ${SESSION_DIR}/SESSION.md"
echo ""
echo "Optional day journal row (${TODAY_JOURNAL}) — paste under 'Versona challenges invoked' or 'Versona sessions' columns:"
echo "| (discipline) | (work item) | (concern) | (action) | forge-logs/versona/${ACTOR}/${SESSION_ID} |  |  |  |"
