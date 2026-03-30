# Forge — ceremonies & events (prescriptive)

**Meetings and ceremony intents:** The events below are **Forge meetings**—scheduled, accountable team collaboration. They align with this blueprint’s **ceremony intent** types **C1–C6** ([Ceremony foundation](../ceremonies/ceremony-foundation.md)). In public-facing copy, **meeting** is the preferred label; **ceremony** names the same events when mapping to foundation intents. **Versona sessions** (discipline work under `forge-logs/versona/`) are separate and are not a substitute for these team meetings—see [Meetings vs ceremonies vs Versona sessions](NAMING-REFERENCE.md#meetings-vs-ceremonies-vs-versona-sessions). **Why** (rationale, problem) and **For what** (beneficiary, outcome, decision) are distinct when designing agendas—see [Why vs For what](NAMING-REFERENCE.md#why-vs-for-what) in the naming reference.

Each Forge ceremony below lists **inputs**, **outputs**, **participants**, **timebox**, **agenda**, and **Forge-specific mechanics**. Forge keeps standard ceremony names and adds precision inside them.

Default iteration length: **1 week** (configurable to 2 weeks for exploratory work).

---

## 0. Ongoing — Ore intake

**Intent:** Capture new ideas, requests, issues, and opportunities as Ore before they enter the commitment pipeline.

| | |
|--|--|
| **Inputs** | External requests, feedback, defect reports, hypotheses, stakeholder conversations |
| **Outputs** | Ore items in the backlog with source, problem/opportunity, urgency, expected value |
| **Participants** | Anyone (primarily Product hat) |
| **Cadence** | Continuous |

**Prescriptive rule:** Do not refine or commit Ore during intake. Capture enough for triage; avoid detailed commitments.

---

## 1. Refinement (Ore → Ingot)

**Intent:** **C1** (Align) + **C2** (Plan the slice) — shape selected Ore into Ingots.

| | |
|--|--|
| **Inputs** | Ore backlog, product context, known constraints, discipline knowledge bases |
| **Outputs** | Ingots with: problem statement, value proposition, acceptance route, key constraints, evidence-of-done criteria |
| **Participants** | Product hat (**R**), Engineering hat (**R**), Challenge hat (**O** — Versonas at decision points) |
| **Timebox** | ≤ **1 hour** per session; ~10–15% of iteration capacity on refinement |
| **Cadence** | 1–2× per week |

**Agenda:**

1. Product hat presents top Ore items (5–10 min).
2. Clarify problem, value, and constraints; Engineering hat assesses feasibility (15–20 min).
3. Invoke Versonas on high-risk or high-value items — time-boxed session (10–15 min).
4. Decide: promote to Ingot, merge, Bank, or reject. Document decisions in Ember Log (5–10 min).

**Definition of Ready (Ingot):**

- Problem and value statement clear.
- Acceptance criteria testable.
- Key constraints and dependencies identified.
- Estimated effort range (fits iteration horizon).
- Phase affinity identified (discover/specify/design/build/verify/release).

---

## 2. Planning (Ingot → Sparks)

**Intent:** **C1** + **C2** — decompose Ingots into Sparks and scope the iteration.

| | |
|--|--|
| **Inputs** | Ingot backlog (ordered), team capacity, past iteration metrics, Definition of Done |
| **Outputs** | Sparks with: intent, expected outcome, acceptance route, phase prefix; iteration scope |
| **Participants** | Product hat (**R**), Engineering hat (**R**), Governance hat (**O**) |
| **Timebox** | ≤ **2 hours** per 1-week iteration |

**Agenda:**

1. Product hat proposes iteration focus and highest-value Ingots (10 min).
2. Engineering hat decomposes Ingots into Sparks (30–45 min).
3. Sequence Sparks by risk reduction and learning value (15 min).
4. Confirm scope fits capacity; intentionally leave margin for interruption (10 min).
5. Identify Versona sessions needed before key Sparks begin (5 min).

**Spark quality check:**

- One clear intent.
- One primary expected outcome.
- One practical acceptance route.
- Limited dependency surface.
- Completable in one focused session (~1–4 hours).
- Phase prefix assigned.

---

## 3. Daily sync (Charge confirmation)

**Also called:** Daily sync **meeting** (same event).

**Intent:** **C3** — execute and unblock; confirm today's Charge.

| | |
|--|--|
| **Inputs** | Current Charge, iteration Sparks, known blockers, Ember Log |
| **Outputs** | Updated Charge for the day; surfaced blockers; Banking or unbanking decisions |
| **Participants** | Engineering hat (**R**); Product hat (**O**); others as needed |
| **Timebox** | **15 minutes** |

**Agenda:**

1. Review yesterday's Charge: what completed, what carries forward (3 min).
2. Confirm today's Charge: which Sparks are active (3 min).
3. Surface blockers and Banking decisions (3 min).
4. Declare hat for the day's primary focus (1 min).
5. Identify any Versona sessions needed (2 min).

**Prescriptive rule:** The Charge should be intentionally smaller than theoretical capacity, leaving room for interruption, rework, and learning.

**Same-day follow-up:** When the sync surfaces a blocker, a need for replanning, or a **discipline Versona**, schedule a **separate, time-boxed** session afterward—analogous to the Scrum Guide’s Daily Scrum plus optional follow-on collaboration. **Do not** add standing **extra** sync meetings that only repeat status without new decisions or outcomes.

---

## 4. Review (evidence assessment)

**Intent:** **C4** (Inspect) + **C6** (Assure) — inspect what was achieved and assess evidence quality.

| | |
|--|--|
| **Inputs** | Completed Sparks, increment, Assay Gate criteria, Ember Log |
| **Outputs** | Evidence assessment, stakeholder feedback, backlog updates, Assay Gate readiness determination |
| **Participants** | Product hat (**R**), Engineering hat (**R**), Challenge hat (**R** — Versonas), Governance hat (**R**), stakeholders (**O**) |
| **Timebox** | ≤ **1.5 hours** per 1-week iteration |

**Agenda:**

1. Engineering hat demonstrates working increment (30 min).
2. Product hat assesses against Ingot acceptance criteria (15 min).
3. Versona session: discipline-specific review of increment quality (15 min).
4. Governance hat reviews evidence against Assay Gate criteria (10 min).
5. Decide: ready for Assay Gate, needs more evidence, or scope adjustment (10 min).

---

## 5. Assay Gate (release readiness)

**Intent:** **C6** — evidence-based release decision. Separate from Review to keep the question strict: *is this releasable?*

| | |
|--|--|
| **Inputs** | Evidence package: tests, acceptance confirmations, risk checks, performance data, Ember Log |
| **Outputs** | Release decision (pass / fail with specific gaps); release notes draft |
| **Participants** | Governance hat (**R**), Product hat (**R**), Engineering hat (**R**) |
| **Timebox** | ≤ **30 minutes** |

**Evidence types (configured per work type):**

- Tests passed (unit, integration, E2E as applicable).
- Acceptance criteria met and documented.
- Risk checks completed (security, compliance Versona if applicable).
- Performance / quality thresholds met.
- Stakeholder validation completed (for user-facing changes).
- Rollback or support readiness confirmed.

**Prescriptive rule:** Work that fails the Assay Gate is not failure — it is simply not yet releasable. Adjust scope or gather more evidence; do not lower evidence standards under schedule pressure.

---

## 6. Retro (learning → new Ore)

**Intent:** **C5** — reflect and improve the system of work.

| | |
|--|--|
| **Inputs** | Iteration metrics (Spark throughput, Ore→Ingot conversion, Assay Gate pass rate), Ember Log, Versona session trends, team experience |
| **Outputs** | 1–3 improvement experiments with owners; new Ore from learnings; Versona configuration adjustments |
| **Participants** | All hats (**R**) |
| **Timebox** | ≤ **1 hour** per 1-week iteration |

**Agenda:**

1. Review metrics: Spark throughput, Charge completion rate, Assay Gate results (10 min).
2. Ember Log review: which decisions worked, which assumptions were wrong (10 min).
3. Versona effectiveness: which sessions added value, which created noise (10 min).
4. Generate insights: patterns, systemic issues, process friction (15 min).
5. Commit to 1–3 experiments with owners and due dates (10 min).
6. Feed learnings back as new Ore where applicable (5 min).

### From retro to directives

Retros must be **documented** enough that tooling or Versonas can turn outcomes into updates to project **directives**—Markdown files that govern how the team works (e.g. project `sdlc/` rules, `.cursor/rules/`, team norms, ADR-style process decisions). Treat directive updates as meeting this **minimum bar**:

- **Evidence** — link to retro notes, metrics, or Ember Log entries that justify the change.
- **Owner** — named human accountable for the change (may align with the retro experiment owner).
- **Approval** — explicit sign-off per team governance (e.g. tech lead + product for SDLC rule changes).
- **Review / expiry** — date or trigger for revisiting the directive; avoid stale rules with no owner.

Experiments from the retro (agenda step 5) may **graduate** into directive updates; smaller adjustments may merge directly into norms. This blueprint does not prescribe automation—only traceability and human ownership.

---

## 7. Quick reference — I/O summary

| Ceremony | Primary inputs | Primary outputs |
|----------|----------------|-----------------|
| Ore intake | External requests, feedback | Ore items in backlog |
| Refinement | Ore backlog, constraints | Ingots (ready for planning) |
| Planning | Ingots, capacity, DoD | Sparks, iteration scope |
| Daily sync | Charge, blockers | Updated Charge, unblocked work |
| Review | Increment, evidence | Assessment, feedback, Assay readiness |
| Assay Gate | Evidence package | Release decision |
| Retro | Metrics, Ember Log | Improvement experiments, new Ore |

---

## 8. Links

- [Process maps & lifecycle](process-and-flows.md) · [Foundation connection](foundation-connection.md) · [Ceremony fork](../ceremonies/forge.md)
