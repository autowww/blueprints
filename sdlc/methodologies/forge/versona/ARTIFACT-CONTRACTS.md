---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona artifact contracts — canonical storage and formats

**Purpose:** One **canonical storage model** and **artifact class** contract so every consuming repo can converge on the same **Versona-related** layout and every Versona knows **where to read and write**. This document **aligns** with [`DOCUMENTATION-STRUCTURE.md`](../../../DOCUMENTATION-STRUCTURE.md) (`docs/`), [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §7–8, [`VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md), and [`daily/README.md`](../daily/README.md) (`forge/`, `ember-logs/`). It **does not** replace WBS or ALM as the system of record for work item IDs.

**Normative companion:** [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) §2a — what each **template** must declare (inputs, outputs, paths, consumers).

---

## 1. Canonical tree (repository root)

Paths are **relative to the consuming repository root**. Create folders when a team adopts that artifact class.

| Path | Owner (accountability) | Purpose |
|------|------------------------|---------|
| **`forge/charge.md`** | Engineering hat (typically) | Daily Charge — selected Sparks |
| **`forge/journal/YYYY-MM-DD.md`** | Contributor | Day journal — activity, hat, optional session pointers |
| **`forge/evidence/<pack-id>/`** | Governance + implementers | **Evidence pack** root — indexes, logs, exports for **verify/release** (see §3.7); `pack-id` is team-defined slug (often Spark id or release id) |
| **`forge/waivers/`** | Governance | Waiver / exception YAML per [`../standards/schemas/waiver-record.schema.json`](../standards/schemas/waiver-record.schema.json) (optional) |
| **`forge/standards-registry.yaml`** | GRC / tech lead | Control registry per [`../standards/README.md`](../standards/README.md) (optional) |
| **`ember-logs/YYYY-MM-DD.md`** | Team | **Decision memory** — trade-offs, scope, risk acceptance |
| **`forge-logs/versona/<actor>/<session-id>/`** | Session actor | **Versona session** — see §3.2 |
| **`forge-logs/versona-track/`** | Automation / tech lead | **Intake ledger**, optional **graph** JSONL — see [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) |
| **`docs/requirements/**`** | Product + BA | **Specs**, WBS-linked specs, milestones ([`DOCUMENTATION-STRUCTURE.md`](../../../DOCUMENTATION-STRUCTURE.md)) |
| **`docs/architecture/**`** | Engineering | Architecture narratives, diagrams **references** |
| **`docs/adr/`** | Engineering | **ADRs** — `NNNN-title.md` (Markdown) |
| **`docs/product/**`** | Product | Product-functional prose, journeys, GTM notes |
| **`docs/testing/**`** | Engineering + QA | Test plans, strategy (optional per project) |
| **`docs/release/**`** | Governance | Release process, checklists (optional); may **link** into `forge/evidence/` |
| **`agents/recipes/<recipe>/`** | Repo | Recipe **definitions** |
| **`agents/workspaces/<recipe>/`** | CI / recipe | **Recipe outputs** — register in session `artifact-manifest.json` when Versona consumes |

**Alias (session root only):** `forge/versona-sessions/<actor>/<session-id>/` with the **same inner layout** as `forge-logs/versona/...` — document in `forge/README.md` or `sdlc/README.md` ([`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §7.1).

---

## 2. Path resolution (examples)

**Example 1 — BA Versona reviews an Ingot**

- **Read:** `docs/requirements/milestones/M1/epics/E2/story.md` (spec), optional `docs/adr/0003-api-style.md`
- **Write:** §5 report → `forge-logs/versona/<actor>/<session-id>/outputs/section5-ba.md` (or `outputs/REPORT.md`); link spec paths in **Evidence requests**
- **Downstream:** Architecture Versona reads same spec + BA output path from `handoff.json` or `SESSION.md`

**Example 2 — Security Versona after recipe scan**

- **Read:** `agents/workspaces/security-scan/run.log`, `docs/architecture/network.md`
- **Write:** `outputs/artifact-manifest.json` listing workspace paths; §5 in `outputs/section5-security.md`

**Example 3 — Intake before first session**

- **Write:** append `request-ledger.jsonl` under `forge-logs/versona-track/`; `session.manifest.json` references `ledger_entry_id` and `work_item_refs`

---

## 3. Artifact classes — formats and minimal metadata

### 3.1 Requests / intake records

| Property | Value |
|----------|--------|
| **Canonical location** | `forge-logs/versona-track/request-ledger.jsonl` (or `versona-track/ledger/YYYY-MM.jsonl` sharded) |
| **Formats** | **JSON Lines** — one object per line; schema [`../schemas/request-ledger-entry.schema.json`](../schemas/request-ledger-entry.schema.json) |
| **Minimal metadata** | `ledger_entry_id`, `recorded_at`, `work_item_refs`, `status`; optional `primary_session_path` |
| **Ownership** | Tooling or human append; **immutable** lines (append-only); corrections via new line + `status: superseded` |

### 3.2 Session data

| Property | Value |
|----------|--------|
| **Canonical root** | `forge-logs/versona/<actor>/<session-id>/` |
| **Formats** | **`SESSION.md`** — Markdown + YAML frontmatter (human index); optional **`session.manifest.yaml`** / **`session.manifest.json`** ([`../schemas/session-manifest.schema.json`](../schemas/session-manifest.schema.json)) |
| **Minimal metadata** | `session_id`, `started_at`, `work_item_refs` (recommended), `work_item_kind` (recommended) |
| **Subfolders** | `inputs/` (snapshots, copies of specs), `outputs/` (reports, JSON payloads), `diagrams/` (IR + SVG), optional `transcript.md` |
| **Ownership** | Session **actor**; Git policy per [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §7.5 |

### 3.3 Handoff payloads

| Property | Value |
|----------|--------|
| **Canonical location** | `forge-logs/versona/<actor>/<session-id>/outputs/handoff.json` (optional machine-readable); prose summary in `SESSION.md` **Handoffs** |
| **Formats** | **JSON** — [`../schemas/handoff-payload.schema.json`](../schemas/handoff-payload.schema.json); Markdown bullet list acceptable for human-only |
| **Minimal metadata** | `summary`, `artifact_paths`, `created_at`; optional `recommended_next_actor` |

### 3.4 Specs / requirements

| Property | Value |
|----------|--------|
| **Canonical location** | **`docs/requirements/**`** per [`DOCUMENTATION-STRUCTURE.md`](../../../DOCUMENTATION-STRUCTURE.md) (milestones, epics, stories, tasks) |
| **Formats** | **Markdown** (preferred for IDE/agent); **YAML/CSV** for traceability matrices under `docs/requirements/traceability/` when used |
| **Minimal metadata** | Work item id in title or body; link to parent Ingot/Ore where applicable |
| **Versona I/O** | **Read** primary; **write** only when explicitly authoring specs (e.g. BA draft) — prefer **session `outputs/`** for review artifacts, then human **promotes** to `docs/requirements/` |

### 3.5 ADRs / architecture decisions

| Property | Value |
|----------|--------|
| **Canonical location** | **`docs/adr/`** — files `NNNN-short-title.md` |
| **Formats** | **Markdown** with agreed ADR template (status, context, decision, consequences) |
| **Minimal metadata** | Number, **status** (proposed / accepted / superseded), **date** |
| **Supporting diagrams** | **Source** in session `diagrams/` or `docs/architecture/diagrams/` **IR** + **SVG** export; **link** from ADR body |

### 3.6 Reports / reviews (Versona §5 and peers)

| Property | Value |
|----------|--------|
| **Canonical location (Versona-generated)** | `forge-logs/versona/<actor>/<session-id>/outputs/*.md` (e.g. `section5-{discipline}.md` or `REPORT.md`) |
| **Canonical location (promoted / human review)** | Team choice: `docs/development/reviews/` or milestone folder under `docs/requirements/` — **document** in `docs/PROJECT.md` if not default |
| **Formats** | **Markdown** matching [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) §5 |
| **Minimal metadata** | `work_item_refs`, **phase**, **Review depth** in report header |

### 3.7 Evidence packs (Assay / audit)

| Property | Value |
|----------|--------|
| **Canonical root** | **`forge/evidence/<pack-id>/`** — `pack-id` = e.g. `spark-M1E1S2T3` or `release-2026-04-11` |
| **Formats** | **Markdown** `README.md` (index), **JSON** `manifest.json` optional, **files** (logs, screenshots, reports) as produced |
| **Minimal metadata** | List of **Spark** / **Ingot** ids covered; pointers to CI artifacts, session outputs, ADRs |
| **Versona I/O** | **Read** for verify/release Versonas; **write** via recipes + human consolidation — register paths in session **`artifact-manifest.json`** |

### 3.8 Kitchen-sink diagram sources and exports

| Property | Value |
|----------|--------|
| **Session-local** | `forge-logs/versona/<actor>/<session-id>/diagrams/` — **IR** (`*.diagram.json` or team IR), **rendered** `*.svg` |
| **Repo-long-lived** | `docs/architecture/diagrams/` (or `docs/product/diagrams/`) — same IR + SVG pattern |
| **Formats** | **IR:** JSON structure (tool-agnostic); **export:** **SVG** preferred for handbook/kitchen-sink pipelines; avoid **Mermaid-only** as the **sole** methodology format ([`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) §5) |
| **Published shorthand** | `blueprint-diagram` fences in handbook content map from IR or SVG **adapter** |

---

## 4. Allowed formats summary

| Format | Use for |
|--------|---------|
| **Markdown** | SESSION, Ember Log, journal, Charge, specs, ADRs, §5 reports, evidence README |
| **YAML** | Front matter, `session.manifest.yaml`, `forge/forge.config.yaml`, waivers, optional spec metadata |
| **JSON** | `session.manifest.json`, handoff, artifact-manifest, routing-decision, ledger lines, diagram IR |
| **JSONL** | Append-only ledgers and graph analytics |
| **SVG** | Diagram exports |
| **CSV** | Traceability / risk registers under `docs/requirements/` when used |

---

## 5. Downstream consumers (routing)

| Producer artifact | Typical consumers |
|-------------------|-------------------|
| Session `outputs/*.md` (§5) | Next Versona session `inputs/`, human review, **Ember Log** summary |
| `outputs/handoff.json` | Chained session, orchestrator (`versona-forge-sdlc`) |
| `docs/requirements/**` | All discipline Versonas by phase; **forge-planning** |
| `docs/adr/**` | Architecture, Security, Compliance, SE |
| `forge/evidence/**` | Testing, Security, Compliance, **Assay Gate**, Governance |
| Recipe `agents/workspaces/**` | Discipline Versonas, **artifact-manifest.json** |

---

## 6. Migration notes

1. **Existing repos** using only `forge/`, `ember-logs/`, `forge-logs/versona/` — **no change required**; add `forge/evidence/` and `forge-logs/versona-track/` when ready.
2. **Specs under non-`docs/requirements/` paths** — keep working; declare **actual paths** in each Versona template §2a until you migrate ([`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md)).
3. **Globs** — update installed `.mdc` files to [`RECOMMENDED-GLOBS.md`](RECOMMENDED-GLOBS.md) patterns aligned with §1–3.
4. **Mermaid-only diagrams** — replace over time with **IR + SVG** or `blueprint-diagram` pipeline per operating model.

---

## 7. References

- [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) §2a
- [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md)
- [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md)
- [`../schemas/README.md`](../schemas/README.md)
- [`../../../DOCUMENTATION-STRUCTURE.md`](../../../DOCUMENTATION-STRUCTURE.md)
