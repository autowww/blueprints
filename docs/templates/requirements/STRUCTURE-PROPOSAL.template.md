# Requirements structure — proposal for review

This document is the **current proposal** for spec-driven IDs, folder layout, traceability, **WBS**, and **RBS**. Edit here until you freeze v1, then scaffold folders under `milestones/`.

---

## 1. ID scheme (compact, no leading zeros)

**Principles**

- **All numeric segments** use **no leading zeros**: `M1`, `M1E1`, `M1E1S1`, `M1E1S1T1` (not `M1E001`).
- IDs are **concatenated** without extra separators between segment letters and numbers.
- `E`, `S`, `T` are **literal letters**.

**Patterns**

| Level     | Pattern              | Example     | Meaning                          |
|-----------|----------------------|-------------|----------------------------------|
| Milestone | `M{n}`               | `M1`        | Milestone 1                      |
| Epic      | `M{n}E{n}`           | `M1E3`      | Epic 3 under milestone 1        |
| Story     | `M{n}E{n}S{n}`       | `M1E3S2`    | Story 2 under that epic          |
| Task      | `M{n}E{n}S{n}T{n}`   | `M1E3S2T4`  | Task 4 under that story          |

**Counters**

- Epic / story / task numbers are **per parent** (each epic's stories start at `S1`, etc.).
- There is **no fixed digit width**; `M1E10` is valid.

**Sorting caveat**

- Plain **string sort** in explorers or CSV may order `M1E10` before `M1E2`. Prefer **natural sort** in tools, or accept manual ordering in `INDEX.md` / WBS.

**Risk IDs (RBS)**

- Separate namespace: **`R{n}`** with no leading zeros (`R1`, `R2`, …). See `docs/requirements/risks/`.

**Filenames (recommended)**

- Mirror the ID: `M1E3-epic.md`, `M1E3S2-story.md`, `M1E3S2T4-task.md`.

---

## 2. Master roadmap & WBS

| Artifact | Path | Purpose |
|----------|------|---------|
| **Master roadmap** | `docs/ROADMAP.md` | Milestone + **epic status** and **% complete** (roll-up from WBS or manual override) |
| **WBS (machine)** | `docs/requirements/WBS.csv` | Full breakdown **to story level** + **status** |
| **WBS (human)** | `docs/requirements/WBS.md` | Same content as readable tables (optional duplicate; keep in sync) |

Epic **% complete** in `docs/ROADMAP.md` should follow the rule documented there (typically: % of stories in `done` per epic).

---

## 3. Risk breakdown structure (RBS)

Risks are **not** the same artifact as WBS tasks. They use:

- **`docs/requirements/risks/register.csv`** — master list with `scope` + `scope_id` (milestone → task).
- **`docs/requirements/risks/RBS.md`** — lightweight process (scoring, cadence).
- **`docs/requirements/risks/README.md`** — why we **do not** mirror the full milestone tree by default; optional `items/R{n}.md` for long write-ups.

**Recommendation:** **Single register + optional `items/`**, not a full parallel `milestones/M1/epics/.../risks/` tree. Reasons: risks often span multiple requirements; one sorted register is easier to review. If you later need browse-by-epic, add **`by-scope/M1E3.md`** index files that list risk IDs only.

---

## 4. Folder structure — nested by milestone

```text
docs/
  requirements/
    INDEX.md                      # TOC: milestones → epics → stories
    WBS.csv                       # Work breakdown to stories + status
    WBS.md                        # Human-readable mirror of WBS.csv
    STRUCTURE-PROPOSAL.md         # This file
    traceability/
      themes-matrix.csv
      tests-matrix.csv
    risks/
      README.md                   # RBS layout and conventions
      RBS.md                      # Risk process
      register.csv                # Master risk register
      items/                      # Optional: R1.md, R2.md, …
    milestones/
      M1/
        milestone.md
        epics/
          M1E1/
            epic.md
            stories/
              M1E1S1/
                story.md
                tasks/
                  M1E1S1T1-task.md
                  M1E1S1T2-task.md
      M2/
        milestone.md
        ...
```

---

## 5. File content (spec-driven)

Each `.md` file uses **YAML frontmatter** + **Markdown body**.

**Common frontmatter keys**

```yaml
---
id: M1E3S2
parent: M1E3
milestone: M1
type: story            # milestone | epic | story | task
status: draft          # draft | ready | backlog | in_progress | done | cancelled
themes: [THEME-LLM]    # optional; see themes matrix
---
```

---

## 6. Themes (separate traceability)

**File:** `docs/requirements/traceability/themes-matrix.csv`

**Columns (suggested):** `theme_id`, `requirement_id`, `level`, `notes`

- **requirement_id**: any `M1`, `M1E3`, `M1E3S2`, `M1E3S2T4`

---

## 7. Tests (future-proof, lightweight)

- `tests-matrix.csv`: `requirement_id`, `test_kind`, `artifact`

---

## 8. SDLC & documentation map

- **Frozen blueprint & policy:** [`../../blueprints/sdlc/README.md`](../../blueprints/sdlc/README.md) · [`../../blueprints/sdlc/POLICY.md`](../../blueprints/sdlc/POLICY.md)
- **Process & DoD:** [`../../blueprints/sdlc/SDLC.md`](../../blueprints/sdlc/SDLC.md) — phases, Definition of Done, what to update per phase.
- **Full doc layout:** [`../../blueprints/sdlc/DOCUMENTATION-STRUCTURE.md`](../../blueprints/sdlc/DOCUMENTATION-STRUCTURE.md) — `docs/` tree, conventions.
- **Documentation blueprint:** [`../../blueprints/docs/README.md`](../../blueprints/docs/README.md) — frozen IA + templates.
- **Product functional (mutable):** [`../product/INDEX.md`](../product/INDEX.md)
- **Entry point:** [`../INDEX.md`](../INDEX.md) — links to all active documentation areas.

---

## 9. Open decisions (confirm before scaffolding)

| # | Question | Proposal |
|---|----------|----------|
| 1 | Story layer mandatory? | Yes — acceptance criteria at story; tasks are implementation slices. |
| 2 | Leading zeros on E/S/T? | **No** — use `E1`, `S1`, `T1` style throughout. |
| 3 | Filename language | English `milestone.md` / `epic.md` / `story.md` + ID prefix on task files. |

---

## 10. Next step after approval

1. Scaffold `docs/requirements/milestones/` with your milestone and epic tree.
2. Keep **[`docs/INDEX.md`](../INDEX.md)** updated as new guides are added.

---

*Template — adapt IDs, folder paths, and conventions to your organization.*
