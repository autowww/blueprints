---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Process: <process-id>

<!-- Abstract process template — replace angle-bracket placeholders. Link from SESSION.md process_id when used. -->

**Goal:** <!-- outcome -->

**Entry triggers:** <!-- ceremony, gate, or event -->

**Related framework:** `blueprints/sdlc/methodologies/forge/versona/VERSONA-FRAMEWORK.md` §5

## Inputs

| Input | Owner | Required |
|-------|-------|----------|
| | Human / system | yes / no |

## Steps

| Step | Owner type | Description | Outputs |
|------|------------|-------------|---------|
| 1 | Human | | |
| 2 | Versona:discipline | | |
| 3 | Tasklet / Recipe | | |

Owner type values: `Human` | `Versona:discipline` | `Versona:routing` | `Versona:meta` | `Tasklet` | `Recipe`

## Flow

```blueprint-diagram
key: sequence
alt: Flow
title: Versona process sequence
summary: How an entry trigger advances through governed owner steps to a traceable outcome handoff.
node: Flow
detail: Names the bounded process this template documents.
more: Link from SESSION.md process_id so each Versona session maps to one reviewable flow definition.
node: Actor / trigger
detail: A ceremony, gate, or event starts the process.
more: Entry triggers are declared at the top of the template so prerequisites and ownership stay explicit before work begins.
node: System step
detail: Human, Versona, or tasklet work executes the step table.
more: Owner types include Human, Versona:discipline, Versona:routing, Versona:meta, Tasklet, and Recipe per the Steps section.
node: Outcome / handoff
detail: Produces artifacts, decisions, or Ember Log entries for downstream use.
more: Outputs feed the next process, Assay Gate, or release path listed under Downstream consumers.
fallback_ascii: |
  Flow

  Actor / trigger
      |
      v
  System step
      |
      v
  Outcome / handoff
```

## Outputs

- <!-- artifacts, decisions, Ember Log expectations -->

## Downstream consumers

- <!-- next process, Assay Gate, release -->

## Tasklets and recipes (optional)

- Cognition tasklets: `blueprints/sdlc/methodologies/forge/tasklets/`
- Execution recipes: `agents/recipes/<name>/` — see `blueprints/agents/ORCHESTRATION.md`
