---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Test plan — [scope]

**Scope:** [milestone, epic, release, or story group]  
**Owner:** [name / role]  
**Status:** draft | ready | executed  
**Related:** WBS / story IDs: …  
**Reference:** [`testing/APPROACHES.md`](../../disciplines/engineering/testing/APPROACHES.md) (test levels, types, techniques) · [`testing/AUTOMATION-LANDSCAPE.md`](../../disciplines/engineering/testing/AUTOMATION-LANDSCAPE.md) (framework selection)

## 1. Objectives

What quality bar this plan must demonstrate (e.g. regressions prevented, acceptance criteria covered).

## 2. In scope / out of scope

| In scope | Out of scope |
|----------|--------------|
| | |

## 3. Test levels

| Level | What | Design techniques | Who | Notes |
|-------|------|-------------------|-----|-------|
| Unit | | | | |
| Integration | | | | |
| API / contract | | | | |
| UI / instrumented | | | | |
| Manual / exploratory | | | | |

Adjust rows to match your stack (e.g. add visual/snapshot, remove API/contract if not applicable). For **design techniques** see [`testing/APPROACHES.md`](../../disciplines/engineering/testing/APPROACHES.md) §4 (equivalence partitioning, boundary value, decision table, state transition, exploratory, etc.).

## 4. Environments

- **Build:** [debug / release / CI variant]
- **Devices / OS:** [emulator API levels, physical devices]
- **Data:** [fixtures, anonymized prod-like data]

## 5. Traceability

| Requirement / story ID | Automated cases | Manual checks |
|--------------------------|-----------------|---------------|
| | | |

Link to `docs/requirements/traceability/tests-matrix.csv` if you maintain one.

## 6. Entry and exit criteria

- **Entry:** [e.g. feature branch merged to integration; CI green on main]
- **Exit:** [e.g. all must-fix defects closed; Owner sign-off]

## 7. Risks and mitigations

| Risk | Mitigation |
|------|------------|
| | |

## 8. Automation stack (optional)

Document the test automation frameworks chosen for this scope. See [`testing/AUTOMATION-LANDSCAPE.md`](../../disciplines/engineering/testing/AUTOMATION-LANDSCAPE.md) §7 for selection guidance.

| Tier | Framework | Version | Notes |
|------|-----------|---------|-------|
| Unit / component | | | |
| API / contract | | | |
| E2E / UI | | | |
| BDD runner | | | |
| Cloud / device farm | | | |

---

*Template — copy to `docs/testing/` or embed sections in a story spec.*
