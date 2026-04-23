---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Recommended Cursor `globs` for Versonas

Forge Versona templates ship with **empty `globs:`** so each repo opts in. **Prefer** the patterns below so attachment aligns with the **canonical storage model** in [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md) — not ad-hoc repo trees.

**Principle:** `globs` should cover **where this Versona reads** per its **Artifact I/O** table ([`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) §2a). Narrow or widen to match your repo; document **overrides** in the template.

## Cross-cutting glob bundles (compose as needed)

| Bundle | Glob pattern | Maps to artifact class |
|--------|----------------|------------------------|
| **Specs / WBS** | `docs/requirements/**/*` | Specs, requirements ([`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md) §3.4) |
| **ADRs** | `docs/adr/**/*` | Architecture decisions §3.5 |
| **Architecture prose** | `docs/architecture/**/*` | Architecture narratives, diagram links §3.5 |
| **Product functional** | `docs/product/**/*` | Product journeys, capabilities §3.4 / structure doc |
| **Testing / QA docs** | `docs/testing/**/*` | Test plans §3.6 / structure doc |
| **Release** | `docs/release/**/*` | Release checklists §3.7 |
| **Forge operational** | `forge/**/*` | Charge, config, evidence packs, waivers §1 |
| **Versona sessions** | `forge-logs/versona/**/*` | Session markdown, outputs, diagrams §3.2 |
| **Intake / ledger (optional)** | `forge-logs/versona-track/**/*` | Request ledger JSONL |
| **Evidence packs** | `forge/evidence/**/*` | Assay / audit bundles §3.7 |
| **Recipe outputs** | `agents/workspaces/**/*` | Execution plane artifacts §1 |

## Product family (installed rule names)

| Rule | Suggested `globs` (comma-separated in `.mdc` frontmatter) |
|------|------------------------------------------------------------|
| `versona-product-management.mdc` | `docs/product/**/*`, `docs/requirements/**/*`, `docs/adr/**/*`, `forge/**/*`, `forge-logs/versona/**/*` |
| `versona-ba.mdc` | `docs/requirements/**/*`, `docs/product/**/*`, `docs/adr/**/*`, `forge-logs/versona/**/*` |
| `versona-ux.mdc` | `docs/product/**/*`, `docs/requirements/**/*`, `docs/architecture/**/*` |
| `versona-marketing.mdc` | `docs/product/**/*`, `docs/release/**/*` |
| `versona-cs.mdc` | `docs/product/**/*`, `docs/release/**/*` |
| `versona-family-product.mdc` | `docs/product/**/*`, `docs/requirements/**/*`, `forge/**/*`, `forge-logs/versona/**/*` |

## Engineering family

| Rule | Suggested `globs` |
|------|-------------------|
| `versona-se.mdc` | `docs/architecture/**/*`, `docs/adr/**/*`, `docs/requirements/**/*`, `forge-logs/versona/**/*` |
| `versona-architecture.mdc` | `docs/architecture/**/*`, `docs/adr/**/*`, `docs/requirements/**/*` |
| `versona-devops.mdc` | `docs/development/**/*`, `docs/architecture/**/*`, `agents/**/*`, `forge/**/*` |
| `versona-testing.mdc` | `docs/testing/**/*`, `docs/requirements/**/*`, `forge/evidence/**/*`, `forge-logs/versona/**/*` |
| `versona-frontend.mdc` | `docs/architecture/**/*`, `docs/requirements/**/*`, `docs/product/**/*` |
| `versona-mobile.mdc` | Same as frontend |
| `versona-iot.mdc` | `docs/architecture/**/*`, `docs/requirements/**/*` |
| `versona-family-engineering.mdc` | `docs/architecture/**/*`, `docs/adr/**/*`, `docs/requirements/**/*`, `docs/testing/**/*`, `forge/evidence/**/*`, `forge-logs/versona/**/*` |

## Data, Governance, Cross-cutting

| Rule | Suggested `globs` |
|------|-------------------|
| `versona-bigdata.mdc` | `docs/architecture/**/*`, `docs/requirements/**/*`, `docs/product/**/*` |
| `versona-datascience.mdc` | `docs/architecture/**/*`, `docs/product/**/*`, `docs/requirements/**/*` |
| `versona-pm.mdc` | `docs/requirements/**/*`, `forge/**/*`, `ember-logs/**/*`, `forge-logs/versona/**/*` |
| `versona-security.mdc` | `docs/architecture/**/*`, `docs/adr/**/*`, `forge/evidence/**/*`, `agents/workspaces/**/*`, `forge-logs/versona/**/*` |
| `versona-compliance.mdc` | `docs/requirements/**/*`, `docs/product/**/*`, `docs/release/**/*`, `forge/evidence/**/*`, `forge/waivers/**/*`, `forge-logs/versona/**/*` |

## Routing, meta, workflow

| Rule | Suggested `globs` |
|------|-------------------|
| `versona-all.mdc` | `docs/requirements/**/*`, `docs/architecture/**/*`, `forge/**/*`, `forge-logs/versona/**/*` |
| `versona-sampling.mdc` | `docs/**/*.md`, `forge/**/*`, `forge-logs/versona/**/*` |
| `versona-project-setup.mdc` | `forge/**/*`, `sdlc/**/*`, `.cursor/rules/**/*` |
| `versona-roadmap-gate.mdc` | `docs/**/*.md`, `forge/**/*` |
| `versona-forge-sdlc.mdc` | `docs/requirements/**/*`, `docs/adr/**/*`, `forge/**/*`, `forge-logs/**/*`, `ember-logs/**/*` |
| `versona-cursor-rules-sync.mdc` | `.cursor/rules/**/*`, `forge/**/*` |

**Family aggregator:** use the **union** of child disciplines or a single broad pattern; prefer **`docs/requirements/**/*`** + **`docs/architecture/**/*`** + **`forge-logs/versona/**/*`** over unbounded `docs/**/*` unless the repo is doc-only.

**Tasklets** (`forge-tasklet-*.mdc`): e.g. `docs/requirements/**/*.md`, `docs/architecture/**/*.md`, `forge/**/*`, `forge-logs/versona/**/*`, or leave empty for manual `@` invocation.

See also: [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md), [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) §2a, [`../tasklets/README.md`](../tasklets/README.md).
