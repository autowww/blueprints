# Versona contract

Every Versona Cursor rule template follows this standard structure to ensure consistency, bridge-awareness, and structured output.

## Required sections

### 1. Frontmatter

```
---
description: Forge Versonas — {Discipline} challenge agent. {One-sentence purpose.}
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

List the key documents the Versona agent should reference:

- Discipline README (body of knowledge overview).
- Bridge document (phase alignment, anti-patterns, role mapping).
- Specific sub-documents (approaches, patterns, techniques) relevant to challenges.

### 4. Challenge protocol

- **When to challenge:** Which Forge ceremonies and decision points activate this Versona.
- **Phase awareness:** How challenge intensity maps to SDLC phases A–F (from the bridge document's phase alignment table).
- **What to inspect:** Specific aspects of work items (Ore, Ingots, Sparks, evidence) to examine.
- **Scope boundaries:** What this Versona does NOT challenge (to avoid overlap with other disciplines).

### 5. Output format

Every Versona challenge produces structured output:

```markdown
## Versona challenge: {Discipline}

**Work item:** {Ore/Ingot/Spark ID and title}
**Phase:** {current SDLC phase}
**Challenge intensity:** {high/medium/low — based on phase relevance}

### Concerns

| # | Concern | Severity | Recommendation |
|---|---------|----------|----------------|
| 1 | {description} | {critical/significant/minor} | {specific action} |

### Evidence requests

- {What evidence would resolve the concern}

### Recommendation

{Proceed / Proceed with conditions / Rework / Bank}
```

### 6. Forge context

- **State awareness:** Understand the Forge state model (Ore → Ingot → Spark → Charge → Done → Released).
- **Hat awareness:** Recognize which hat the user is wearing and adjust challenge accordingly.
- **Ember Log integration:** Suggest Ember Log entries for decisions resulting from the challenge.

## Creating a new Versona

1. Copy the closest existing template.
2. Update Identity with the new discipline's details.
3. Update Knowledge references to point to the correct discipline package.
4. Calibrate Challenge protocol using the discipline's bridge document phase alignment.
5. Test with sample Ore/Ingots/Sparks from different phases to verify intensity calibration.
