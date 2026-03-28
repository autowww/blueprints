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
alt: Diagram
```

## Outputs

- <!-- artifacts, decisions, Ember Log expectations -->

## Downstream consumers

- <!-- next process, Assay Gate, release -->

## Tasklets and recipes (optional)

- Cognition tasklets: `blueprints/sdlc/methodologies/forge/tasklets/`
- Execution recipes: `agents/recipes/<name>/` — see `blueprints/agents/ORCHESTRATION.md`
