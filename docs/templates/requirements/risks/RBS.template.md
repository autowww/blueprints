# Risk breakdown structure — process

## Scope levels

A risk may apply at:

| Level     | Example `scope_id` | Typical use |
|-----------|---------------------|-------------|
| Milestone | `M1`                | Schedule slip, vendor dependency |
| Epic      | `M1E3`              | API policy change, design uncertainty |
| Story     | `M1E3S1`            | UX confusion, edge case complexity |
| Task      | `M1E3S1T2`          | Concrete implementation hazard |

**Rule:** Set **`scope`** + **`scope_id`** to the **lowest** level where the risk is meaningfully owned; use **`related_requirement_ids`** when it also affects other IDs.

## Scoring (lightweight)

Suggested columns in `register.csv`:

- **probability** / **impact**: `low` | `medium` | `high` (or 1–3).
- **status**: `open` | `mitigating` | `accepted` | `closed`.

## Cadence

- Review **open** risks when an epic moves to `done` or monthly.
- Close or downgrade when mitigation ships or assumption is validated.

## Files

| File | Role |
|------|------|
| `register.csv` | Master list |
| `items/R{n}.md` | Optional deep dive per risk |
