---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Tasklet taxonomy

**Tasklets** are small, **single-operation** units (typically Cursor `.mdc` rules). A **Versona** supplies **discipline overlay**: phase intensity, scope boundaries, severity, and merge into [`VERSONA-CONTRACT.md`](../versona/VERSONA-CONTRACT.md) output.

## 1. Execution plane (where work runs)

| Plane | Mechanism | Examples |
|-------|-----------|----------|
| **Cognition** | In-IDE LLM (rules, Skills, chat) | Extract assumptions, triage table |
| **Local tool** | Approved host scripts | Lint, codegen, format |
| **Container / recipe** | `agents/recipes/*/run.sh` + Docker | Headless browser, batch export |
| **Remote API** | Script or MCP wrapper | Tickets, analytics, vendor UI |

Cognition tasklets live in **`.cursor/rules/`** after install. **Execution-plane** steps are **not** the same process as the LLM: they exchange **manifests and artifacts** (stdin/JSON → files + logs) that the Versona or human reviews.

## 2. Operation class (what the step does)

| Class | Typical output |
|-------|----------------|
| **Extract** | Lists (assumptions, entities, risks) |
| **Transform** | Spec → test cases, outline → deck spec |
| **Verify** | Pass/fail, rubric scores, diff commentary |
| **Act** | Commit, PR, run recipe — usually **human-gated** |

## 3. Lifecycle / Forge alignment (filters)

Tag or invoke tasklets by **Ore / Ingot / Spark**, SDLC **A–F**, or Spark prefix (`discover:`, `build:`, …). Aligns with [`forge-versona.mdc`](../../../templates/forge/cursor-rules/forge-versona.mdc) routing.

## 4. Artifact binding (optional `globs`)

Use Cursor **`globs:`** so rules attach when relevant paths are open (e.g. `docs/product/**/*`). See [`../versona/RECOMMENDED-GLOBS.md`](../versona/RECOMMENDED-GLOBS.md) for Product Versonas.

## 5. Discipline overlay (required for “neutral” tasklets)

| Layer | Responsibility |
|-------|----------------|
| **Tasklet** | Mechanical I/O schema; minimal normative text |
| **Versona** | Chooses tasklets, adds constraints (“Testing: falsifiability”), merges report |
| **Optional tag** | Catalog metadata: `neutral`, `product-family`, `engineering-family`, `governance` |

## See also

- [`README.md`](README.md) — install and bundled examples (includes **route**, **bootstrap-session**, **check-standards**, **log-event**, **merge-outputs**, **summarize-evidence**)
- [`../versona/README.md`](../versona/README.md) — Versona catalog + Sampling
- [`../versona/VERSONA-SKILL-MATRIX.md`](../versona/VERSONA-SKILL-MATRIX.md) — tasklet ↔ Versona mapping
- [`agents/ORCHESTRATION.md`](../../../../agents/ORCHESTRATION.md) — container recipes
