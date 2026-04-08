---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# SDD I/O schema — ceremonies & process slots

**Purpose:** Define a **repeatable, machine- and human-friendly** shape for specifying **inputs, outputs, preconditions, and artifacts** for any **ceremony intent (C1–C6)** or **named process slot** (planning, gate, refinement, …). Use this so **agents**, **engineers**, and **product** share one contract.

**Pairs with:** [Spec-driven development overview](https://forgesdlc.com/methodology-spec-driven.html) · [Ceremony foundation](../ceremonies/ceremony-foundation.md) · Templates in [`../../templates/sdd/`](../../templates/sdd/README.md)

---

## When to use which template

| You are specifying… | Template file |
|---------------------|-----------------|
| A **foundation intent** (C1–C6) or a **calendar event** mapped to intents | [`CEREMONY-INTENT.template.md`](../../templates/sdd/CEREMONY-INTENT.template.md) |
| A **process step** or **gate** (sequential slice of work, often phased or release) | [`PROCESS-SLOT.template.md`](../../templates/sdd/PROCESS-SLOT.template.md) |

---

## Document structure (required sections)

Every SDD ceremony/process spec **SHOULD** include these sections **in order** (copy from the template):

| Section | Meaning |
|---------|---------|
| **SDD metadata** | YAML frontmatter: `sdd_id`, `kind`, `version`, `maps_to`, `status` |
| **Summary** | One short paragraph: what this slot does in the delivery system |
| **Boundaries** | In scope / out of scope for **this** spec (prevents ceremony creep) |
| **Preconditions** | What must **already be true** or **available** before the slot starts |
| **Inputs** | **Consumed** during the slot (read, discussed, transformed)—each with **type**, **owner**, **format**, **example** |
| **Outputs** | **Produced** by the end of the slot—each with **consumer**, **storage location**, **example** |
| **Postconditions** | Observable **done** criteria (checkboxes) |
| **Participants** | **RACI-style** or **lead + required participants** |
| **Artifact register** | Fine-grained list: id, name, type, producer → consumer |
| **Traceability** | Work-unit IDs, doc paths, tracker links |
| **Filled example** | **Concrete** instance (same headings, fictional but realistic project) |

---

## YAML frontmatter (normative keys)

```yaml
---
sdd_id: SDD-C1-ALIGN           # unique, stable string
kind: ceremony_intent         # ceremony_intent | process_slot
version: "1.0"
status: draft                 # draft | active | deprecated
maps_to:
  ceremony_intents: [C1]      # C1..C6; empty [] for pure process slots
  methodology_events: []      # optional: ["Sprint Planning — Part 1", …]
  sdlc_phases: [A, B]           # optional: A–F touch
title: "Align on intent — horizon H"
owner_archetype: "Demand & value"   # from roles-archetypes if useful
---
```

---

## Input / output row shape (tables)

Use **one row per artifact** (not one row per meeting). Minimum columns:

**Preconditions**

| ID | Artifact | Format | Owner | Ready when (criterion) |
|----|----------|--------|-------|------------------------|

**Inputs**

| ID | Name | Type | Source | Format | Example (snippet) |
|----|------|------|--------|--------|-------------------|

**Outputs**

| ID | Name | Type | Primary consumer | Storage / system | Example (snippet) |
|----|------|------|------------------|------------------|---------------------|

**Artifact register** (optional extra granularity)

| Art-ID | Name | Kind | Producer | Consumer | Versioning |
|--------|------|------|----------|----------|------------|

---

## Quality rules

1. **Examples are mandatory** — at least one **filled example** per spec; vague rows without examples are incomplete.  
2. **IDs are stable** — `sdd_id` and row `ID` columns do not change meaning mid-flight; use a new version or new `sdd_id` if semantics shift.  
3. **One consumer minimum** — every **output** names **who** uses it next (person, role, or system).  
4. **Chat is not storage** — outputs must name **repo path**, **tracker object**, or **tool**; “verbal agreement” is not an output row unless followed by a **written** record in the named system.  
5. **Maps to C1–C6** — ceremony specs should tag **intent(s)** so the [foundation](../ceremonies/ceremony-foundation.md) and methodology forks stay aligned.

---

## Handbook subchapters (HTML)

- [SDD schema & templates](../../docs/spec-driven-sdd-schema.html)  
- [Ceremonies (SDD I/O)](../../docs/spec-driven-sdd-ceremonies.html)  
- [Process slots (SDD I/O)](../../docs/spec-driven-sdd-process.html)

---

## Related templates (repo paths)

| Path | Use |
|------|-----|
| [`blueprints/sdlc/templates/sdd/CEREMONY-INTENT.template.md`](../../templates/sdd/CEREMONY-INTENT.template.md) | Blank ceremony / intent SDD spec |
| [`blueprints/sdlc/templates/sdd/PROCESS-SLOT.template.md`](../../templates/sdd/PROCESS-SLOT.template.md) | Blank process step / gate SDD spec |
