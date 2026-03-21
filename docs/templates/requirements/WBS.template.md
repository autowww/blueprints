# Work breakdown structure (WBS)

Human-readable mirror of [`WBS.csv`](WBS.csv). Keep both in sync; the CSV is the machine-readable source.

## Column definitions

| Column | Meaning |
|--------|---------|
| `id` | Work-unit ID (`M1`, `M1E1`, `M1E1S1`) |
| `type` | `milestone` / `epic` / `story` |
| `title` | Short name |
| `status` | `draft` / `ready` / `backlog` / `in_progress` / `done` / `cancelled` |
| `parent` | Parent ID |
| `notes` | Optional freeform |

## Breakdown

<!-- Paste or generate tables from WBS.csv. Example: -->

| id | type | title | status | parent | notes |
|----|------|-------|--------|--------|-------|
| M1 | milestone | Milestone 1 | active | — | |

---

*Update when scope or status changes. See [`../ROADMAP.md`](../ROADMAP.md) for epic-level summary.*
