#!/usr/bin/env bash
# Bootstrap docs/ tree from blueprints/docs/templates/ + blueprints/sdlc/templates/.
# Run from the REPOSITORY ROOT (where blueprints/ lives).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMPL_DIR="$SCRIPT_DIR/../templates"
SDLC_TMPL_DIR="$SCRIPT_DIR/../../sdlc/templates"

usage() {
  cat <<'USAGE'
Usage: ./blueprints/docs/scripts/init-docs-workspace.sh "Project Name" [OPTIONS]

Options:
  --force     Overwrite existing files (default: skip if exists)
  -h, --help  Show this help

Examples:
  ./blueprints/docs/scripts/init-docs-workspace.sh "My Product"
  ./blueprints/docs/scripts/init-docs-workspace.sh "My Product" --force
USAGE
}

# ── Parse arguments ──────────────────────────────────────────────────────────

PROJECT_NAME=""
FORCE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --force)   FORCE=true; shift ;;
    -h|--help) usage; exit 0 ;;
    -*)        echo "Unknown option: $1" >&2; usage >&2; exit 1 ;;
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
DATE="$(date +%Y-%m-%d)"

copy_template() {
  local src="$1"
  local dest="$2"

  if [[ -f "$dest" && "$FORCE" != true ]]; then
    echo "  SKIP  $dest (exists; use --force to overwrite)"
    SKIPPED=$((SKIPPED + 1))
    return
  fi

  mkdir -p "$(dirname "$dest")"
  sed -e "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" \
      -e "s/{{DATE}}/$DATE/g" \
      "$src" > "$dest"
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

strip_template_ext() {
  echo "$1" | sed 's/\.template\./\./'
}

echo "Bootstrapping docs/ tree for: $PROJECT_NAME"
echo ""

# ── Root docs files ──────────────────────────────────────────────────────────

echo "Root docs/:"
copy_template "$TMPL_DIR/INDEX.template.md" "docs/INDEX.md"
copy_template "$TMPL_DIR/PROJECT.template.md" "docs/PROJECT.md"

# ROADMAP from SDLC templates
if [[ -f "$SDLC_TMPL_DIR/ROADMAP.template.md" ]]; then
  copy_template "$SDLC_TMPL_DIR/ROADMAP.template.md" "docs/ROADMAP.md"
fi
echo ""

# ── Product functional docs ─────────────────────────────────────────────────

echo "Product functional docs/product/:"
for src in "$TMPL_DIR"/VISION.template.md "$TMPL_DIR"/PERSONAS.template.md \
           "$TMPL_DIR"/CAPABILITY.template.md "$TMPL_DIR"/JOURNEY.template.md \
           "$TMPL_DIR"/FEATURE-SPEC.template.md; do
  if [[ -f "$src" ]]; then
    name="$(strip_template_ext "$(basename "$src")")"
    copy_template "$src" "docs/product/$name"
  fi
done
echo ""

# ── Requirements ─────────────────────────────────────────────────────────────

echo "Requirements docs/requirements/:"
for src in "$TMPL_DIR"/requirements/*.template.md "$TMPL_DIR"/requirements/*.template.csv; do
  if [[ -f "$src" ]]; then
    name="$(strip_template_ext "$(basename "$src")")"
    copy_template "$src" "docs/requirements/$name"
  fi
done

# Risks
for src in "$TMPL_DIR"/requirements/risks/*.template.md; do
  if [[ -f "$src" ]]; then
    name="$(strip_template_ext "$(basename "$src")")"
    copy_template "$src" "docs/requirements/risks/$name"
  fi
done

# Traceability
for src in "$TMPL_DIR"/requirements/traceability/*.template.csv; do
  if [[ -f "$src" ]]; then
    name="$(strip_template_ext "$(basename "$src")")"
    copy_raw "$src" "docs/requirements/traceability/$name"
  fi
done

# Seed milestone scaffold
mkdir -p docs/requirements/milestones/M1/epics
mkdir -p docs/requirements/risks/items
echo ""

# ── ADR ──────────────────────────────────────────────────────────────────────

echo "ADR docs/adr/:"
copy_template "$TMPL_DIR/adr/README.template.md" "docs/adr/README.md"
echo ""

# ── Architecture ─────────────────────────────────────────────────────────────

echo "Architecture docs/architecture/:"
copy_template "$TMPL_DIR/architecture/README.template.md" "docs/architecture/README.md"
echo ""

# ── Development ──────────────────────────────────────────────────────────────

echo "Development docs/development/:"
copy_template "$TMPL_DIR/development/README.template.md" "docs/development/README.md"
copy_template "$TMPL_DIR/development/CI-CD.template.md" "docs/development/CI-CD.md"
echo ""

# ── Testing ──────────────────────────────────────────────────────────────────

echo "Testing docs/testing/:"
copy_template "$TMPL_DIR/testing/README.template.md" "docs/testing/README.md"
echo ""

# ── Release ──────────────────────────────────────────────────────────────────

echo "Release docs/release/:"
copy_template "$TMPL_DIR/release/README.template.md" "docs/release/README.md"
echo ""

# ── Security ─────────────────────────────────────────────────────────────────

echo "Security docs/security/:"
copy_template "$TMPL_DIR/security/README.template.md" "docs/security/README.md"
echo ""

# ── Operations ───────────────────────────────────────────────────────────────

echo "Operations docs/operations/:"
copy_template "$TMPL_DIR/operations/README.template.md" "docs/operations/README.md"
echo ""

# ── Summary ──────────────────────────────────────────────────────────────────

echo "Done. Created $CREATED file(s), skipped $SKIPPED."
if [[ $CREATED -gt 0 ]]; then
  echo ""
  echo "Next steps:"
  echo "  1. Edit docs/PROJECT.md — fill in stack & repo context"
  echo "  2. Edit docs/requirements/STRUCTURE-PROPOSAL.md — confirm ID scheme"
  echo "  3. Review docs/INDEX.md — remove links to areas you don't need yet"
  echo "  4. Commit the generated files to version control"
fi
