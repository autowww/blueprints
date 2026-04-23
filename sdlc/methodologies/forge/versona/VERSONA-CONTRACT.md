---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona contract

Every **`kind: discipline`** Versona Cursor rule template follows this standard structure for **identity**, **bridge-awareness**, and—when the team uses the **standard structured report**—output per **§5**. A discipline Versona is a **virtual persona** for one professional lens. Activities include advice, drafting, handoffs, and—when useful—a **§5-shaped discipline review**; no single activity defines “Versona.” For **Skills**, **tasklets**, and **recipe** stubs each template should lean on, see [`VERSONA-SKILL-MATRIX.md`](VERSONA-SKILL-MATRIX.md). For **canonical paths**, **artifact formats**, and **read/write** ownership, see [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md). For **kinds** (routing, family aggregators, meta, workflow), **interfaces**, **processes**, **sessions**, and **logging** alignment, see [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md). For **standards precedence**, per-Versona profiles, and traceability fields, see [`../standards/README.md`](../standards/README.md). For **enriched** machine-readable artifacts (optional), session tree detail, Rules vs recipes split, and diagram IR, see [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) and [`../schemas/README.md`](../schemas/README.md). For the **kind/domain tree** and template index, see [`catalog/ANCESTRY.md`](catalog/ANCESTRY.md). **Source files:** templates live under [`versona/catalog/`](catalog/) (and optional [`versona-generic.mdc.template`](versona-generic.mdc.template) at the `versona/` root); exact paths are in [`catalog/TEMPLATE-INDEX.md`](catalog/TEMPLATE-INDEX.md).

**Shared baseline:** Each `versona-*.mdc.template` includes a duplicated **`## Baseline (inherited)`** section (Layer 0). The canonical source is [`_includes/GENERIC-VERSONA-BASELINE.md`](_includes/GENERIC-VERSONA-BASELINE.md)—update that file first, then propagate verbatim into all templates.

## Required sections

### 1. Frontmatter

```
---
description: Forge Versonas — {Discipline} Versona (discipline-focused virtual persona). {One-sentence purpose.} Structured §5 output when using the standard report shape.
globs: (see [`RECOMMENDED-GLOBS.md`](RECOMMENDED-GLOBS.md) — align with [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md) §1)
alwaysApply: false
---
```

### 2. Identity

- **Discipline name** and core question.
- **Family** (Engineering / Data / Product / Governance / Cross-cutting).
- **Knowledge base path** — relative path to the discipline package in `blueprints/disciplines/`.
- **Bridge document** — the `*-SDLC-PDLC-BRIDGE.md` that maps discipline activities to lifecycle phases.

### 2a. Artifact I/O declaration (discipline templates)

Each **`kind: discipline`** template MUST include an **`## Artifact I/O`** section (after **Knowledge references** or **§5 report protocol**, but before **Output format**—pick one placement and keep consistent across templates). It makes **read/write** paths explicit for agents and humans. Normative path definitions: [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md).

Use this **table shape** (adapt rows; use `N/A` when not applicable):

```markdown
## Artifact I/O

| Field | Canonical paths (repo-relative) |
|-------|----------------------------------|
| **Required inputs** | e.g. `docs/requirements/**/*`, `docs/adr/*.md` — what must exist or be pasted before a useful §5 pass |
| **Optional inputs** | e.g. `docs/architecture/**/*`, `forge/evidence/<pack-id>/` |
| **Produced outputs** | e.g. `forge-logs/versona/<actor>/<session-id>/outputs/section5-{discipline}.md`, optional `outputs/handoff.json` |
| **Canonical storage** | Default session root: `forge-logs/versona/<actor>/<session-id>/` (see blueprint `ARTIFACT-CONTRACTS.md` §3.2) |
| **Downstream consumers** | e.g. next Versona, human Assay owner, CI — who reads the outputs |
```

**Authoring rule:** Prefer **canonical** paths from [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md) §1. If the repo uses **legacy** locations, add a second row **“Repo overrides”** listing actual paths until migration.

**Other kinds** (`routing`, `family_aggregator`, `meta`, `workflow`): SHOULD declare **Artifact I/O** when they read or write files; at minimum state **outputs** (e.g. routing table in chat only → say **ephemeral / chat** and optional `outputs/routing-decision.json`).

### 3. Knowledge references

List the key documents the Versona should reference:

- Discipline README (body of knowledge overview).
- Bridge document (phase alignment, anti-patterns, role mapping).
- Specific sub-documents (approaches, patterns, techniques) relevant to discipline work.

### 4. §5 report protocol (standard structured discipline review)

Other **activities** (advice, drafting, orchestration within discipline scope) are permitted per [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md). This section defines when and how to produce the **§5 structured report**—the **normative** shape below when teams choose that output.

- **When to use §5:** Which Forge ceremonies and decision points call for a structured discipline review for this Versona.
- **Phase awareness:** How **review depth** maps to SDLC phases A–F (from the bridge document's phase alignment table).
- **What to inspect:** Specific aspects of work items (Ore, Ingots, Sparks, evidence) to examine.
- **Scope boundaries:** What this Versona does NOT assert outside its bridge (to avoid overlap with other disciplines); recommend handoff or routing when out of scope.

### 5. Structured output format (Contract §5)

When producing the standard structured report, use this shape:

```markdown
## {Discipline} Versona — structured output

**Work item:** {Ore/Ingot/Spark ID and title}
**Phase:** {current SDLC phase}
**Review depth:** {high/medium/low — based on phase relevance}

### Concerns

| # | Concern | Severity | Recommendation |
|---|---------|----------|----------------|
| 1 | {description} | {critical/significant/minor} | {specific action} |

### Evidence requests

- {What evidence would resolve the concern}

### Recommendation

{Proceed / Proceed with conditions / Rework / Bank}
```

#### §5.1 Standards traceability (when material)

When the work item touches **policies, controls, contractual obligations, or evidence packs**, add **after** `**Review depth:**` and **before** `### Concerns` (or immediately after `**Review depth:**` if your template orders sections differently—stay consistent within each discipline):

```markdown
### Standards traceability

- **standards_considered:** Bullet list — control IDs or short names from the consuming-repo registry (`forge/standards-registry.yaml` or equivalent), **Cursor Team Rules**, and methodology layers consulted (L1–L6 per `blueprints/sdlc/methodologies/forge/standards/precedence.md`). Use `N/A — local craft only` when no policy surface applies.
- **standards_applied:** What **actually governed** this pass after applying precedence (which layer won for each material topic).
- **conflicts_detected:** Bullets — each **lower-layer** recommendation that **lost** to a higher layer, with the **winner** stated (e.g. “L6 ‘use prod dump’ vs L1 DPA → L1”).
- **waivers_required:** Open **waiver** or exception records needed (link to `forge/waivers/…` or GRC ticket); `none` if none. Waivers do not negate law—document compensating controls.
- **evidence_obligations:** Concrete artifacts, logs, or links the team must produce or retain for **Assay Gate** / audit, derived from the **winning** controls.
```

Omit the entire **`### Standards traceability`** block only when the session is **explicitly** out of scope for any control or policy (pure style preference, no data, no customer, no org baseline invoked).

**Family aggregators** and **routing** kinds should either **merge** child `standards_*` fields or **summarize** cross-cutting conflicts in their output variant, using the same field names when practical.

#### Suggested handoffs (optional)

Discipline templates may append a **`### Suggested next Versonas`** section **after** `### Evidence requests` and **before** `### Recommendation` (or immediately after `### Recommendation` if a template documents that ordering—stay consistent within each discipline). Content is a short table or bullet list: **which Versona or rule**, **when to invoke**, **why**. This block does **not** replace or weaken the single top-level **Proceed / Proceed with conditions / Rework / Bank** recommendation.

### 6. Forge context

- **State awareness:** Understand the Forge state model (Ore → Ingot → Spark → Charge → Done → Released).
- **Hat awareness:** Recognize which hat the user is wearing and adjust the session accordingly (e.g. review depth when producing a §5 report).
- **Ember Log integration:** Suggest Ember Log entries for decisions resulting from **§5 reviews** or other activities that imply trade-offs or scope change.

## Creating a new Versona

1. Confirm **kind** (`discipline`, `routing`, `family_aggregator`, `meta`, `workflow`) per [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §2; discipline templates follow §1–§6 below.
2. Copy the closest existing template.
3. Update Identity with the new discipline's details.
4. Add **`## Artifact I/O`** per **§2a** and [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md); set **`globs:`** per [`RECOMMENDED-GLOBS.md`](RECOMMENDED-GLOBS.md).
5. Update Knowledge references to point to the correct discipline package.
6. Calibrate **§5 report protocol** using the discipline's bridge document phase alignment.
7. Test with sample Ore/Ingots/Sparks from different phases to verify review depth calibration.
8. **Optional thin operations:** reuse or add **tasklets** (single-operation Cursor rules) under [`../tasklets/`](../tasklets/README.md); see [`TASKLET-TAXONOMY.md`](../tasklets/TASKLET-TAXONOMY.md) for execution plane vs cognition and **discipline overlay** rules.
9. For **session folders**, **process diagrams**, and **handoffs**, use [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §§5–8 and [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md); optional JSON handoffs and manifests per [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md).
10. Keep **`## Baseline (inherited)`** in sync with [`_includes/GENERIC-VERSONA-BASELINE.md`](_includes/GENERIC-VERSONA-BASELINE.md); set the `<!-- Ancestry: ... -->` line per [`catalog/ANCESTRY.md`](catalog/ANCESTRY.md).
11. Align **standards profile** with [`../standards/VERSONA-STANDARDS-MATRIX.md`](../standards/VERSONA-STANDARDS-MATRIX.md); do not paste large control catalogs—**reference** registries and Team Rules.

## Recommended globs (Product family)

See [`RECOMMENDED-GLOBS.md`](RECOMMENDED-GLOBS.md) when shipping Versonas with file-scoped Cursor attachment.
