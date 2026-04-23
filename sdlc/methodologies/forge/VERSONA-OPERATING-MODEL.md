---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona operating model — process-first layout, artifacts, and tooling split

This document defines a **process-first** operating model for **enriched** Versona work: where to put **request intake**, **session** material, **handoffs**, **evidence**, **diagram exports**, and **graph-friendly** records in any **consuming repository**. Full **artifact taxonomy** (specs, ADRs, evidence packs, report locations, formats): [`versona/ARTIFACT-CONTRACTS.md`](versona/ARTIFACT-CONTRACTS.md). It **extends** the session and logging model in [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) (§§7–8) and the **Ember Log** / **day journal** pairing in [`daily/README.md`](daily/README.md); it does **not** replace them.

**Schemas (machine-readable contracts):** [`schemas/`](schemas/) — JSON Schema files referenced below. They are **optional** until a team turns on validation or automation; human-readable `SESSION.md` and Ember Log entries remain valid.

**Terminology:** **Work item references** stay **Ore / Ingot / Spark** (and team WBS / external ALM IDs). This model does **not** introduce a new work-item ID scheme. **Ledger** and **graph** identifiers are **operational** (correlation, analytics), not replacements for Forge work units.

**Supersession:** When **external compliance** (organizational policy, regulator, customer contract) conflicts with this methodology, **compliance wins**. Full **L1–L6** stack and conflict handling: [`standards/precedence.md`](standards/precedence.md). Teams map required evidence and retention into the same tree where possible; where impossible, document the override in `forge/` or `sdlc/README.md` and keep **work_item_refs** pointing at the authoritative system of record.

---

## 1. Canonical repository tree (cross-repo)

Use **one** convention per repo. Defaults below align with [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §7 and [`agents/ORCHESTRATION.md`](../../../agents/ORCHESTRATION.md).

### 1.1 Core (already in the framework)

| Location | Purpose |
|----------|---------|
| `forge-logs/versona/<actor>/<session-id>/` | **Session** root: `SESSION.md`, `inputs/`, `outputs/`, optional `transcript.md` |
| `ember-logs/YYYY-MM-DD.md` | **Decision memory** (trade-offs, scope, risk acceptance) |
| `forge/journal/YYYY-MM-DD.md` | **Day journal** (activity, hat, optional session pointers) |
| `agents/workspaces/<recipe>/` | **Recipe** execution outputs (execution plane) |
| `agents/recipes/<recipe>/` | **Recipe** definitions (entry scripts, README) |

**Alias:** `forge/versona-sessions/<actor>/<session-id>/` may replace `forge-logs/versona/…` if documented locally; keep the **same** inner layout and manifest fields.

### 1.2 Enriched additions (optional until adopted)

| Location | Purpose |
|----------|---------|
| `forge-logs/versona/<actor>/<session-id>/session.manifest.json` | **Machine-readable** mirror of session metadata (JSON Schema: [`schemas/session-manifest.schema.json`](schemas/session-manifest.schema.json)); may coexist with `session.manifest.yaml` |
| `forge-logs/versona/<actor>/<session-id>/outputs/handoff.json` | **Handoff payload** for the next actor or Versona (Schema: [`schemas/handoff-payload.schema.json`](schemas/handoff-payload.schema.json)) |
| `forge-logs/versona/<actor>/<session-id>/outputs/routing-decision.json` | **Routing** output when a routing Versona or tool records a machine-readable decision (Schema: [`schemas/routing-decision.schema.json`](schemas/routing-decision.schema.json)) |
| `forge-logs/versona/<actor>/<session-id>/outputs/artifact-manifest.json` | **Index** of files produced in the session or pulled from recipes (Schema: [`schemas/artifact-manifest.schema.json`](schemas/artifact-manifest.schema.json)) |
| `forge-logs/versona/<actor>/<session-id>/diagrams/` | **Diagram-as-code IR** (`.json` or other agreed IR), plus **rendered** exports (e.g. `.svg`) from a kitchen-sink or site pipeline — see §5 |
| `forge-logs/versona-track/request-ledger.jsonl` | **Append-only** request / intake lines (one JSON object per line; Schema: [`schemas/request-ledger-entry.schema.json`](schemas/request-ledger-entry.schema.json)) |
| `forge-logs/versona-track/graph-analytics.jsonl` | **Append-only** graph-friendly **events** and **edges** (one JSON object per line; Schema: [`schemas/graph-analytics-record.schema.json`](schemas/graph-analytics-record.schema.json)) |

**Sharding default:** If `request-ledger.jsonl` or `graph-analytics.jsonl` grows large, shard by month: `versona-track/ledger/YYYY-MM.jsonl` and `versona-track/graph/YYYY-MM.jsonl`, preserving the same **per-line** JSON shapes.

**Git policy:** Same as [`VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §7.5 — commit summaries and manifests where audit needs it; gitignore large transcripts or secret-bearing inputs per team policy.

---

## 2. Machine-readable artifacts

| Artifact | When to write | Schema | Typical binding |
|----------|----------------|--------|-----------------|
| **Request ledger entry** | Intake of a new Versona **request** (from human, agent, or ticket webhook) before or as the first session starts | [`request-ledger-entry.schema.json`](schemas/request-ledger-entry.schema.json) | Append one line to `versona-track/request-ledger.jsonl`; reference `ledger_entry_id` from `session.manifest.json` |
| **Session manifest** | Session start; update on close or major activity boundary | [`session-manifest.schema.json`](schemas/session-manifest.schema.json) | `session.manifest.json` (and/or YAML mirror); `SESSION.md` frontmatter stays the human index |
| **Routing decision** | After **routing** Versona or script emits a structured recommendation | [`routing-decision.schema.json`](schemas/routing-decision.schema.json) | `outputs/routing-decision.json` |
| **Handoff payload** | Before **sequential handoff** to another Versona or human | [`handoff-payload.schema.json`](schemas/handoff-payload.schema.json) | `outputs/handoff.json`; next session sets `parent_session` / copies `inputs/` as needed |
| **Artifact manifest** | After a **recipe** run or when consolidating **evidence** paths | [`artifact-manifest.schema.json`](schemas/artifact-manifest.schema.json) | `outputs/artifact-manifest.json` and/or pointers into `agents/workspaces/<recipe>/` |
| **Graph analytics record** | Optional **telemetry** for analytics (session linked, handoff edge, evidence link) | [`graph-analytics-record.schema.json`](schemas/graph-analytics-record.schema.json) | Append to `versona-track/graph-analytics.jsonl` |

**Ember Log** entries remain **Markdown** (with optional HTML comment hints per [`VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §8.1). Do not require JSON in Ember Log for methodology compliance.

---

## 3. Responsibility split — Rules, AGENTS.md, Skills, subagents, recipes

| Layer | Owns | Should not own |
|-------|------|----------------|
| **Cursor Rules** (`.cursor/rules/*.mdc`, including Versona templates) | **Discipline identity**, bridge scope, **§5** protocol when used, **routing** heuristics, pointers to blueprint docs and **schemas** | Long procedural runbooks better expressed as recipes; secrets; repo-wide policy exceptions |
| **AGENTS.md** (repo root, optional) | **Repo-wide** defaults: where `versona-track/` lives, gitignore policy, **compliance** overrides, “always attach X when discussing Sparks”; optional link or paste of [**Markdown-canonical workspace policy**](../markdown-canonical-workspace-policy.md) when the repo adopts that profile | Per-discipline §5 tables (belongs in Versona rules) |
| **Skills** (Cursor **Skills**, e.g. under `.cursor/skills/` or team path) | **Repeatable short workflows** (checklists, command sequences) that **invoke** rules or scripts with a stable prompt | Full discipline knowledge bases (link to `blueprints/disciplines/` instead) |
| **Subagents** (or delegated agent tasks) | **Isolated** exploration with a **narrow** output contract (e.g. produce `routing-decision.json` draft, summarize `inputs/`) | Final **Proceed / Rework** verdict without human visibility when governance requires review |
| **Execution recipes** (`agents/recipes/`, Docker/CI) | **Deterministic** steps, **artifacts**, logs, **evidence** files; write outputs under `agents/workspaces/<recipe>/` and register in **artifact manifest** | Open-ended interpretation of policy (return artifacts; Versona or human interprets) |

**Default:** **Cognition** (analysis, §5 reports, routing suggestions) stays in **Rules** + **Skills**; **execution** (build, test, export, scrape) stays in **recipes**. **Subagents** are optional accelerators with the same split: narrow **cognition** subtasks vs **recipe** invocation.

**Catalog:** which Versona invokes which Skill, tasklet, and recipe stub — [`versona/VERSONA-SKILL-MATRIX.md`](versona/VERSONA-SKILL-MATRIX.md).

---

## 4. Process alignment

- **Process documents** (ordered activities, owners: Human | Versona | Tasklet | Recipe) remain as in [`VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §5.
- **Enriched** runs add: optional **ledger** line on intake, **session.manifest.json** at open, **artifact-manifest** after recipe steps, **handoff.json** when chaining, **graph-analytics** lines when analytics is enabled.

---

## 5. Diagram strategy (kitchen-sink–compatible, not Mermaid-specific)

**Goal:** Diagrams that can flow from **authoring** → **static site** or **handbook** pipelines without locking the methodology to a single grammar.

1. **Diagram-as-code IR** — Store **structured** diagram source under `diagrams/` (e.g. `*.diagram.json` or team-agreed JSON) describing nodes, edges, and labels. This IR is **tool-agnostic**; converters may target SVG, HTML, or other emitters.
2. **Kitchen Sink adapter** — In handbook or product sites, **blueprints** content may use **` ```blueprint-diagram `** fenced blocks (see [`process-and-flows.md`](process-and-flows.md)) as the **published** shorthand; consuming generators map IR → that surface or to **SVG** assets.
3. **Exported SVG** — Check in or generate **SVG** under `diagrams/` when the pipeline produces a file artifact suitable for evidence packs and review.
4. **Artifact manifest** — Register each diagram file with `artifact_kind`: `diagram_ir` or `diagram_rendered` and optional `diagram_adapter` (e.g. `blueprint_diagram`, `svg_asset`, `external_uri`).

**Anti-pattern:** Defining methodology **only** in terms of one vendor diagram grammar. Prefer **IR + adapter** so Mermaid, Graphviz, or other backends remain **replaceable** at the project layer.

---

## 6. Migration notes

Summary: **No breaking change** to existing `SESSION.md`-only folders.

1. **Existing sessions** — Continue to validate against human expectations; add `session.manifest.json` only when a team enables tooling.
2. **New fields** — Use `versona_session_schema_version` in manifest (see [`versona/MIGRATIONS.md`](versona/MIGRATIONS.md)) when adopting schema versions from this folder.
3. **Ledger** — Backfill optional: append ledger lines for **open** work when turning on `versona-track/`; link `work_item_refs` to Ore/Ingot/Spark or external keys **without** minting new Forge IDs.
4. **Changelog** — Table row in [`versona/MIGRATIONS.md`](versona/MIGRATIONS.md) when schema files change incompatibly.

---

## 7. References

- [`versona/ARTIFACT-CONTRACTS.md`](versona/ARTIFACT-CONTRACTS.md) — canonical paths and formats for all Versona-related artifacts
- [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) — sessions, handoffs, Ember Log, journal
- [`versona/VERSONA-CONTRACT.md`](versona/VERSONA-CONTRACT.md) — discipline rule shape, §2a Artifact I/O, §5 output, §5.1 standards traceability
- [`standards/README.md`](standards/README.md) — precedence, registries, per-Versona profiles
- [`foundation-connection.md`](foundation-connection.md) — Forge ↔ foundation tracking
- [`setup/CURSOR-RULES-ALIGNMENT.md`](setup/CURSOR-RULES-ALIGNMENT.md) — rule install and manifest
- [`tasklets/README.md`](tasklets/README.md) — cognition tasklets
- [`agents/docs/VERSONA-EXECUTION-TASKLETS.md`](../../../agents/docs/VERSONA-EXECUTION-TASKLETS.md) — execution plane
- [`schemas/README.md`](schemas/README.md) — schema index
