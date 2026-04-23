---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Template recipe: `versona-kitchensink-diagram-export`

**Purpose:** **Execution-plane** stub for turning **`blueprint-diagram`** sources or session `diagrams/` inputs into **SVG** (or other Kitchen Sink outputs) via the consuming repo’s **generator** — e.g. `python3 generator/build-showcase.py` or site build. Keeps **diagram export** out of the IDE model when teams want **repeatable** CI.

**Cognition counterpart:** Skill **`export-versona-kitchensink-diagram`** ([`SKILL.md`](../../../../sdlc/templates/forge/cursor-skills/export-versona-kitchensink-diagram/SKILL.md)).

## Non-goals

- Not a general diagram editor — wire your **Kitchen Sink** or site toolchain.
- **Mermaid** is **not** the canonical Forge path for handbook/product docs; prefer **`blueprint-diagram`** + SVG per workspace policy.

## Adoption

1. Copy to **`agents/recipes/versona-kitchensink-diagram-export/`** ([`ORCHESTRATION.md`](../../ORCHESTRATION.md)).
2. Edit **`run.sh`**: set paths to your `forgesdlc-kitchensink` or consumer generator; mount repo at **`/work`** in Docker per [`STRUCTURE.md`](../../STRUCTURE.md).
3. Write exports to **`agents/workspaces/versona-kitchensink-diagram-export/`** or session `diagrams/exported/`; register in **`artifact-manifest.json`** when applicable.

## Environment

| Variable | Required | Description |
|----------|----------|-------------|
| `DIAGRAM_SOURCE_DIR` | Recommended | Host path or `/work/...` to IR or markdown sources |

## Usage

```bash
./run.sh
```

Stub exits `0` after printing **implementation hints**.

## See also

- [`VERSONA-OPERATING-MODEL.md`](../../../../sdlc/methodologies/forge/VERSONA-OPERATING-MODEL.md) §5 (diagram IR)
