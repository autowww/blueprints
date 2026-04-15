#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(pwd)"
HOOK_MARKER="FORGE_VERSION_RELEASE_HOOK"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_HOOK="${SCRIPT_DIR}/hooks/version-release-post-commit.py"

if [[ ! -f "${PY_HOOK}" ]]; then
  echo "Error: missing ${PY_HOOK}" >&2
  exit 1
fi

if [[ ! -d "${REPO_ROOT}/.git" ]]; then
  echo "Error: run from a git repository root (no .git here: ${REPO_ROOT})" >&2
  exit 1
fi

if [[ ! -f "${REPO_ROOT}/blueprints/sdlc/methodologies/forge/setup/hooks/version-release-post-commit.py" ]]; then
  echo "Warning: blueprints hook path not found under repo root — post-commit will use:" >&2
  echo "  ${PY_HOOK}" >&2
fi

HOOK_PATH="${REPO_ROOT}/.git/hooks/post-commit"

if [[ -f "${HOOK_PATH}" ]] && ! grep -q "${HOOK_MARKER}" "${HOOK_PATH}" 2>/dev/null; then
  echo "Error: ${HOOK_PATH} exists and does not contain ${HOOK_MARKER} — merge manually or remove the file." >&2
  exit 1
fi

cat > "${HOOK_PATH}" <<EOF
#!/usr/bin/env sh
# ${HOOK_MARKER} — installed by blueprints install-version-release-hook.sh
REPO_ROOT="\$(git rev-parse --show-toplevel)"
cd "\${REPO_ROOT}" || exit 0
PY="\${REPO_ROOT}/blueprints/sdlc/methodologies/forge/setup/hooks/version-release-post-commit.py"
if test -f "\${PY}"; then
  python3 "\${PY}" || true
elif test -f "${PY_HOOK}"; then
  python3 "${PY_HOOK}" || true
fi
EOF
chmod +x "${HOOK_PATH}"
echo "Installed ${HOOK_PATH}"
echo "Add ${REPO_ROOT}/.forge/version-release.json (see blueprints/sdlc/methodologies/forge/setup/templates/version-release.manifest.example.json)."
