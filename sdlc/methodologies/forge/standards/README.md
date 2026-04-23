---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge Versona — standards resolution

**Purpose:** Let every Versona **know which standards apply**, **which win when they conflict**, and **what evidence** follows—without copying large control catalogs into Cursor rules.

| Document | Role |
|----------|------|
| [`precedence.md`](precedence.md) | Normative **precedence stack** (L1 external → L6 heuristics) |
| [`VERSONA-STANDARDS-MATRIX.md`](VERSONA-STANDARDS-MATRIX.md) | Human-readable **per-Versona** standards profiles |
| [`versona-standards-matrix.yaml`](versona-standards-matrix.yaml) | Machine-readable matrix (same content; YAML) |
| [`versona-standards-matrix.json`](versona-standards-matrix.json) | Same as JSON for tooling |
| [`schemas/standards-registry.schema.json`](schemas/standards-registry.schema.json) | JSON Schema for **consuming-repo** registries |
| [`schemas/waiver-record.schema.json`](schemas/waiver-record.schema.json) | JSON Schema for **waivers / exceptions** |
| [`examples/registry.example.yaml`](examples/registry.example.yaml) | Example registry (fictional controls) |
| [`examples/waiver.example.yaml`](examples/waiver.example.yaml) | Example waiver |
| [`examples/CONFLICT-SCENARIOS.md`](examples/CONFLICT-SCENARIOS.md) | Security, compliance, product, engineering conflict walkthroughs |

**Contract hook:** §5 structured output may include **Standards traceability** — [`../versona/VERSONA-CONTRACT.md`](../versona/VERSONA-CONTRACT.md) §5.1.

**Baseline hook:** All Versona templates inherit **Standards resolution** from [`../versona/_includes/GENERIC-VERSONA-BASELINE.md`](../versona/_includes/GENERIC-VERSONA-BASELINE.md).

## Adopting in a consuming repository

1. Copy or author **`forge/standards-registry.yaml`** (validate against `schemas/standards-registry.schema.json`) listing **control IDs**, severity, and **evidence** expectations your org actually uses.
2. Put **L1–L2** non-negotiables in **Cursor Team Rules** (or equivalent) with **links** to policy, not full text.
3. Point **`AGENTS.md`** at the registry path and any **L3** repo overrides.
4. Add **Skills** for recurring evidence workflows (DPIA-lite, STRIDE pass, accessibility check) — keep rules thin.
5. Optionally CI-validate the registry YAML against the schema.

Do **not** check classified or client-secret text into blueprints; keep sensitive detail in org systems and **reference by ID** in the registry.
