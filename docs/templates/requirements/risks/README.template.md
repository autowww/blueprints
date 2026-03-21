# Risk breakdown structure (RBS)

Risks are **separate** from the WBS: the same risk can touch several requirements, or sit at **milestone** level only.

## Recommended layout

| Piece | Purpose |
|-------|---------|
| **`register.csv`** | Single source of truth: risk ID, title, **scope** (milestone / epic / story / task), **scope_id**, probability, impact, status, mitigation, links |
| **`items/`** (optional) | One file per risk for long narratives: `R12.md` with YAML frontmatter + body |
| **No mirrored tree** | Avoid duplicating `milestones/M1/epics/.../risks/` unless you need physical separation per release — see below |

### Why not mirror the full milestone/epic/story folder tree?

- **Pros of mirroring:** Easy to find "all risks under this epic" by browsing folders.
- **Cons:** Risks often **span** levels (e.g. an auth risk affects both security and UX epics); duplicate paths; harder to get a single sorted register.

**Proposal:** Keep **`register.csv`** authoritative. Optionally add **`by-scope/`** with tiny index files, e.g. `by-scope/M1E3.md` listing only risk IDs for that epic (generated or hand-maintained). Full mirror of `milestones/...` is optional and only worth it for large programs.

### Risk ID pattern

- **`R{n}`** globally (no leading zeros: `R1`, `R2`, …) — short and grep-friendly.
- In `register.csv`, **`scope_id`** references the same IDs as specs: `M1`, `M1E3`, `M1E3S1`, etc.

### Relationship to traceability

- Optional column or sidecar: **`related_requirement_ids`** (comma-separated) for many-to-many links.
- Themes stay in `traceability/themes-matrix.csv`; risks stay here unless you add `traceability/risks-themes.csv` later.

See also **`RBS.md`** in this folder for process (review cadence, scoring).
