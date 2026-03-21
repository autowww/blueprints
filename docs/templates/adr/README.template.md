# Architecture Decision Records (ADR)

**Purpose:** Capture **significant, somewhat stable** technical decisions so future you (or others) knows *why* something was chosen.

## When to write an ADR

- Choosing a library or pattern with **migration cost** (e.g. networking stack, DI, storage).
- Security or privacy approach that affects multiple features.
- Anything you'd otherwise re-debate every six months.

**Skip** trivial choices and one-off implementation details—those belong in PRs or story specs.

## Format

- **Filename:** `0001-short-title.md`, `0002-...` (increment; title in lowercase kebab-case).
- **Template:**

```markdown
# ADR 0001: Title

## Status
Proposed | Accepted | Superseded by ADR 0007

## Context
What problem or constraint triggered this?

## Decision
What we decided.

## Consequences
Positive and negative; what we'll revisit later.
```

## Index

| ADR | Title | Status |
|-----|-------|--------|
| — | *(none yet)* | — |

---

*Add rows to the table when you create ADRs.*
