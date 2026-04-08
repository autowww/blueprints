---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona contract

Every **`kind: discipline`** Versona Cursor rule template follows this standard structure for **identity**, **bridge-awareness**, and—when the team uses the **standard structured report**—output per **§5**. A discipline Versona is a **virtual persona** for one professional lens. Activities include advice, drafting, handoffs, and—when useful—a **§5-shaped discipline review**; no single activity defines “Versona.” For **kinds** (routing, family aggregators, meta, workflow), **interfaces**, **processes**, **sessions**, and **logging** alignment, see [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md). For the **kind/domain tree** and template index, see [`catalog/ANCESTRY.md`](catalog/ANCESTRY.md). **Source files:** templates live under [`versona/catalog/`](catalog/) (and optional [`versona-generic.mdc.template`](versona-generic.mdc.template) at the `versona/` root); exact paths are in [`catalog/TEMPLATE-INDEX.md`](catalog/TEMPLATE-INDEX.md).

**Shared baseline:** Each `versona-*.mdc.template` includes a duplicated **`## Baseline (inherited)`** section (Layer 0). The canonical source is [`_includes/GENERIC-VERSONA-BASELINE.md`](_includes/GENERIC-VERSONA-BASELINE.md)—update that file first, then propagate verbatim into all templates.

## Required sections

### 1. Frontmatter

```
---
description: Forge Versonas — {Discipline} Versona (discipline-focused virtual persona). {One-sentence purpose.} Structured §5 output when using the standard report shape.
globs: (configured by consuming repo — e.g. docs/requirements/**/*, docs/architecture/**/*)
alwaysApply: false
---
```

### 2. Identity

- **Discipline name** and core question.
- **Family** (Engineering / Data / Product / Governance / Cross-cutting).
- **Knowledge base path** — relative path to the discipline package in `blueprints/disciplines/`.
- **Bridge document** — the `*-SDLC-PDLC-BRIDGE.md` that maps discipline activities to lifecycle phases.

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
4. Update Knowledge references to point to the correct discipline package.
5. Calibrate **§5 report protocol** using the discipline's bridge document phase alignment.
6. Test with sample Ore/Ingots/Sparks from different phases to verify review depth calibration.
7. **Optional thin operations:** reuse or add **tasklets** (single-operation Cursor rules) under [`../tasklets/`](../tasklets/README.md); see [`TASKLET-TAXONOMY.md`](../tasklets/TASKLET-TAXONOMY.md) for execution plane vs cognition and **discipline overlay** rules.
8. For **session folders**, **process diagrams**, and **handoffs**, use [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §§5–8.
9. Keep **`## Baseline (inherited)`** in sync with [`_includes/GENERIC-VERSONA-BASELINE.md`](_includes/GENERIC-VERSONA-BASELINE.md); set the `<!-- Ancestry: ... -->` line per [`catalog/ANCESTRY.md`](catalog/ANCESTRY.md).

## Recommended globs (Product family)

See [`RECOMMENDED-GLOBS.md`](RECOMMENDED-GLOBS.md) when shipping Versonas with file-scoped Cursor attachment.
