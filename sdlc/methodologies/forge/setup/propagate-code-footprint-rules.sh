#!/usr/bin/env bash
# Copy code-footprint.mdc from blueprints templates into .cursor/rules/ for sibling repos.
# Usage: from blueprints repo root or any path:
#   bash blueprints/sdlc/methodologies/forge/setup/propagate-code-footprint-rules.sh [workspace_root]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BP_ROOT="$(cd "${SCRIPT_DIR}/../../../.." && pwd)"
SRC="${BP_ROOT}/sdlc/templates/forge/cursor-rules/code-footprint.mdc"

if [[ ! -f "${SRC}" ]]; then
  echo "Error: template not found: ${SRC}" >&2
  exit 1
fi

WORKSPACE="${1:-$(cd "${BP_ROOT}/.." 2>/dev/null && pwd || echo "$HOME/Code")}"

install_one() {
  local dest_dir="$1"
  mkdir -p "${dest_dir}"
  cp "${SRC}" "${dest_dir}/code-footprint.mdc"
  echo "  ${dest_dir}/code-footprint.mdc"
}

echo "=== Propagate code-footprint.mdc ==="
echo "Source: ${SRC}"
echo "Workspace: ${WORKSPACE}"
echo

# Workspace hub rule
if [[ -d "${WORKSPACE}/.cursor/rules" ]] || [[ -d "${WORKSPACE}/.cursor" ]]; then
  echo "Workspace hub:"
  install_one "${WORKSPACE}/.cursor/rules"
fi

echo
echo "Git repos under workspace (maxdepth 2):"
count=0
while IFS= read -r gitdir; do
  repo="$(dirname "${gitdir}")"
  name="$(basename "${repo}")"
  [[ "${name}" == "blueprints" ]] && continue
  echo "${name}:"
  install_one "${repo}/.cursor/rules"
  count=$((count + 1))
done < <(find "${WORKSPACE}" -maxdepth 2 -type d -name .git 2>/dev/null | sort)

echo
echo "Done. Installed/updated in ${count} repo(s) under ${WORKSPACE}."
echo "Optional clones:"
for extra in \
  "${HOME}/forge-fleet" \
  "${HOME}/LCDL/forge-lenses" \
  "${HOME}/Code/forge-accessibility-leo" \
  "${HOME}/Code/forge-accessibility-vika4ka"; do
  if [[ -d "${extra}/.git" ]]; then
    echo "$(basename "$(dirname "${extra}")")/$(basename "${extra}"):"
    install_one "${extra}/.cursor/rules"
  fi
done
