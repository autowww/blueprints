#!/usr/bin/env bash
# Install Forge example tasklets (+ optional Sampling Versona) into a project's .cursor/rules/
# Run from repo root: bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VERSONA_DIR="$(cd "${SCRIPT_DIR}/../versona" && pwd)"

usage() {
  sed -n '1,80p' <<'EOF'
Usage: install-tasklets.sh [options] [REPO_ROOT]

  REPO_ROOT    Target repository root (default: current directory)
  --dry-run    Print actions only
  --force      Overwrite existing rule files
  --no-sampling  Skip versona-sampling.mdc (tasklets only)

Examples:
  bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh
  bash blueprints/sdlc/methodologies/forge/tasklets/install-tasklets.sh --force ../my-app
EOF
}

DEST_ROOT="."
DRY_RUN=0
FORCE=0
NO_SAMPLING=0

for arg in "$@"; do
  case "$arg" in
    -h|--help) usage; exit 0 ;;
  esac
done

positional=()
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --force) FORCE=1 ;;
    --no-sampling) NO_SAMPLING=1 ;;
    -h|--help) ;;
    *) positional+=("$arg") ;;
  esac
done

if ((${#positional[@]} > 0)); then
  DEST_ROOT="${positional[-1]}"
fi

RULES_DIR="${DEST_ROOT%/}/.cursor/rules"
SAMPLING_SRC="${VERSONA_DIR}/catalog/meta/versona-sampling.mdc.template"

echo "=== Forge tasklets install ==="
echo "Target root: ${DEST_ROOT}"
echo "Rules dir:   ${RULES_DIR}"
echo ""

install_one() {
  local src="$1"
  local dest="$2"
  if [[ ! -f "$src" ]]; then
    echo "  Warning: missing source: $src"
    return 0
  fi
  if [[ -f "$dest" && "$FORCE" -eq 0 ]]; then
    echo "  skip (exists): $dest"
    return 0
  fi
  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "  would copy: $src -> $dest"
    return 0
  fi
  mkdir -p "$(dirname "$dest")"
  cp "$src" "$dest"
  echo "  installed: $dest"
}

shopt -s nullglob
count=0
for f in "${SCRIPT_DIR}"/tasklet-*.mdc.template; do
  base="$(basename "$f" .mdc.template)"
  install_one "$f" "${RULES_DIR}/forge-${base}.mdc"
  count=$((count + 1))
done

if [[ "$count" -eq 0 ]]; then
  echo "Error: no tasklet-*.mdc.template files in ${SCRIPT_DIR}"
  exit 1
fi

if [[ "$NO_SAMPLING" -eq 0 ]]; then
  install_one "$SAMPLING_SRC" "${RULES_DIR}/versona-sampling.mdc"
else
  echo "  (--no-sampling: skipped versona-sampling.mdc)"
fi

echo ""
echo "Done. Tune globs: in each installed .mdc, set globs for your tree if you want auto-attach."
echo "Invoke Sampling Versona from the rule picker or @versona-sampling."
