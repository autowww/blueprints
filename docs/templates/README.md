# Templates — documentation blueprint

Copy these into **`docs/`** in your repository using **`../scripts/init-docs-workspace.sh`** (recommended) or manually. The init script strips `.template.` from filenames and replaces `{{PROJECT_NAME}}` / `{{DATE}}` placeholders.

## Root docs

| File | Target | Use for |
|------|--------|---------|
| [`INDEX.template.md`](INDEX.template.md) | `docs/INDEX.md` | Hub linking every documentation area. |
| [`PROJECT.template.md`](PROJECT.template.md) | `docs/PROJECT.md` | Stack, compliance, repo context. |

*`docs/ROADMAP.md` is seeded from `blueprints/sdlc/templates/ROADMAP.template.md`.*

## Product functional (`docs/product/`)

| File | Target | Use for |
|------|--------|---------|
| [`VISION.template.md`](VISION.template.md) | `docs/product/VISION.md` | Problem, goals, non-goals, success metrics. |
| [`PERSONAS.template.md`](PERSONAS.template.md) | `docs/product/PERSONAS.md` | Segments or lightweight personas. |
| [`CAPABILITY.template.md`](CAPABILITY.template.md) | `docs/product/CAPABILITY.md` | One capability in a capability map. |
| [`JOURNEY.template.md`](JOURNEY.template.md) | `docs/product/JOURNEY.md` | One end-to-end user journey. |
| [`FEATURE-SPEC.template.md`](FEATURE-SPEC.template.md) | `docs/product/FEATURE-SPEC.md` | Detailed behavior for a feature or domain. |

## Requirements (`docs/requirements/`)

| File | Target | Use for |
|------|--------|---------|
| [`requirements/STRUCTURE-PROPOSAL.template.md`](requirements/STRUCTURE-PROPOSAL.template.md) | `docs/requirements/STRUCTURE-PROPOSAL.md` | ID scheme, folder layout, frontmatter, WBS/RBS conventions. |
| [`requirements/INDEX.template.md`](requirements/INDEX.template.md) | `docs/requirements/INDEX.md` | Milestone → epic → story TOC. |
| [`requirements/WBS.template.md`](requirements/WBS.template.md) | `docs/requirements/WBS.md` | Human-readable work breakdown. |
| [`requirements/WBS.template.csv`](requirements/WBS.template.csv) | `docs/requirements/WBS.csv` | Machine-readable work breakdown. |
| [`requirements/risks/README.template.md`](requirements/risks/README.template.md) | `docs/requirements/risks/README.md` | RBS layout and conventions. |
| [`requirements/risks/RBS.template.md`](requirements/risks/RBS.template.md) | `docs/requirements/risks/RBS.md` | Risk process (scoring, cadence). |
| [`requirements/traceability/themes-matrix.template.csv`](requirements/traceability/themes-matrix.template.csv) | `docs/requirements/traceability/themes-matrix.csv` | Theme ↔ requirement mapping. |
| [`requirements/traceability/tests-matrix.template.csv`](requirements/traceability/tests-matrix.template.csv) | `docs/requirements/traceability/tests-matrix.csv` | Test ↔ requirement mapping. |

## ADR (`docs/adr/`)

| File | Target | Use for |
|------|--------|---------|
| [`adr/README.template.md`](adr/README.template.md) | `docs/adr/README.md` | ADR index and format guide. |

## Engineering areas

| File | Target | Use for |
|------|--------|---------|
| [`architecture/README.template.md`](architecture/README.template.md) | `docs/architecture/README.md` | System overview placeholder. |
| [`development/README.template.md`](development/README.template.md) | `docs/development/README.md` | Development guide placeholder. |
| [`development/CI-CD.template.md`](development/CI-CD.template.md) | `docs/development/CI-CD.md` | CI/CD pipelines and quality gates. |
| [`testing/README.template.md`](testing/README.template.md) | `docs/testing/README.md` | Test plan conventions. |
| [`release/README.template.md`](release/README.template.md) | `docs/release/README.md` | Distribution and compliance. |
| [`security/README.template.md`](security/README.template.md) | `docs/security/README.md` | Non-secret security notes. |
| [`operations/README.template.md`](operations/README.template.md) | `docs/operations/README.md` | Runbooks and ops. |

After copying, remove or replace placeholder text. Link optional IDs to **`docs/requirements/`** when applicable.
