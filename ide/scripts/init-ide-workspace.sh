#!/usr/bin/env bash
# Bootstrap IDE agent instruction files from blueprints/ide/templates/.
# Run from the REPOSITORY ROOT (where blueprints/ide/ lives).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TMPL_DIR="$SCRIPT_DIR/../templates"

usage() {
  cat <<'USAGE'
Usage: ./blueprints/ide/scripts/init-ide-workspace.sh "Project Name" [OPTIONS]

Options:
  --cursor-only   Skip Claude Code files (.claude/, CLAUDE.md)
  --claude-only   Skip Cursor files (.cursor/, AGENTS.md)
  --force         Overwrite existing files (default: skip if exists)
  -h, --help      Show this help

Examples:
  ./blueprints/ide/scripts/init-ide-workspace.sh "My Product"
  ./blueprints/ide/scripts/init-ide-workspace.sh "My Product" --cursor-only
  ./blueprints/ide/scripts/init-ide-workspace.sh "My Product" --force
USAGE
}

# ── Parse arguments ──────────────────────────────────────────────────────────

PROJECT_NAME=""
CURSOR=true
CLAUDE=true
FORCE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --cursor-only) CLAUDE=false; shift ;;
    --claude-only) CURSOR=false; shift ;;
    --force)       FORCE=true; shift ;;
    -h|--help)     usage; exit 0 ;;
    -*)            echo "Unknown option: $1" >&2; usage >&2; exit 1 ;;
    *)
      if [[ -z "$PROJECT_NAME" ]]; then
        PROJECT_NAME="$1"
      else
        echo "Unexpected argument: $1" >&2; usage >&2; exit 1
      fi
      shift
      ;;
  esac
done

if [[ -z "$PROJECT_NAME" ]]; then
  echo "Error: PROJECT_NAME is required." >&2
  usage >&2
  exit 1
fi

if [[ ! -d "$TMPL_DIR" ]]; then
  echo "Error: templates directory not found at $TMPL_DIR" >&2
  echo "Run this script from the repository root." >&2
  exit 1
fi

# ── Helpers ──────────────────────────────────────────────────────────────────

CREATED=0
SKIPPED=0

copy_template() {
  local src="$1"
  local dest="$2"

  if [[ -f "$dest" && "$FORCE" != true ]]; then
    echo "  SKIP  $dest (exists; use --force to overwrite)"
    SKIPPED=$((SKIPPED + 1))
    return
  fi

  mkdir -p "$(dirname "$dest")"
  sed "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" "$src" > "$dest"
  echo "  CREATE $dest"
  CREATED=$((CREATED + 1))
}

copy_raw() {
  local src="$1"
  local dest="$2"

  if [[ -f "$dest" && "$FORCE" != true ]]; then
    echo "  SKIP  $dest (exists; use --force to overwrite)"
    SKIPPED=$((SKIPPED + 1))
    return
  fi

  mkdir -p "$(dirname "$dest")"
  cp "$src" "$dest"
  echo "  CREATE $dest"
  CREATED=$((CREATED + 1))
}

echo "Bootstrapping IDE agent instructions for: $PROJECT_NAME"
echo ""

# ── Cursor files ─────────────────────────────────────────────────────────────

if [[ "$CURSOR" == true ]]; then
  echo "Cursor:"

  # Root AGENTS.md
  copy_template "$TMPL_DIR/AGENTS.template.md" "AGENTS.md"

  # Rules
  for src in "$TMPL_DIR"/cursor/rules/*.template.mdc; do
    name="$(basename "$src" | sed 's/\.template\./\./')"
    copy_template "$src" ".cursor/rules/$name"
  done

  # Commands
  for src in "$TMPL_DIR"/cursor/commands/*.template.md; do
    name="$(basename "$src" | sed 's/\.template\./\./')"
    copy_template "$src" ".cursor/commands/$name"
  done

  # Plans directory + template
  mkdir -p .cursor/plans
  copy_raw "$TMPL_DIR/plans/PLAN.template.md" ".cursor/plans/PLAN.template.md"

  echo ""
fi

# ── Claude Code files ────────────────────────────────────────────────────────

if [[ "$CLAUDE" == true ]]; then
  echo "Claude Code:"

  # Root CLAUDE.md
  copy_template "$TMPL_DIR/CLAUDE.template.md" "CLAUDE.md"

  # Skills
  for skill_dir in "$TMPL_DIR"/claude/skills/*/; do
    skill_name="$(basename "$skill_dir")"
    src="$skill_dir/SKILL.template.md"
    if [[ -f "$src" ]]; then
      copy_template "$src" ".claude/skills/$skill_name/SKILL.md"
    fi
  done

  # Agents (subagents)
  for src in "$TMPL_DIR"/claude/agents/*.template.md; do
    name="$(basename "$src" | sed 's/\.template\./\./')"
    copy_template "$src" ".claude/agents/$name"
  done

  echo ""
fi

# ── Summary ──────────────────────────────────────────────────────────────────

echo "Done. Created $CREATED file(s), skipped $SKIPPED."
if [[ $CREATED -gt 0 ]]; then
  echo ""
  echo "Next steps:"
  echo "  1. Fill in build/test/lint commands in AGENTS.md and/or CLAUDE.md"
  echo "  2. Review .cursor/rules/ and customize for your stack"
  echo "  3. Commit the generated files to version control"
  echo "  4. Add .cursor/plans/ to .gitignore if plans should stay local"
fi
