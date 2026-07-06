---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge SDLC orchestration — roles, phases, merge, trace

This document is the **methodology orchestration** layer for Forge: it sits **above** individual **discipline** Versonas (which own **§5 specialist judgment**) and **beside** **routing** (`versona-all`). It defines **phase-aware** contracts for **A–F**, **merge ownership**, and **trace outputs**. The Cursor workflow rule **`versona-forge-sdlc`** implements this playbook in chat.

**Supersession:** When **external compliance** or **org-mandated controls** conflict with this playbook, follow [`../standards/precedence.md`](../standards/precedence.md); orchestration **recommends**, it does not **waive** law or policy.

**Machine-readable companion:** [`workflows/phases.json`](workflows/phases.json) (same phase IDs and fields, for tooling).

---

## 1. Role boundaries (who does what)

| Rule / package | **Routes** (picks 2–4 lenses) | **Orchestrates** (ordered/parallel plan across methodology) | **Merges** (multi-lens §5 into one report) | **Owns specialist judgment** (discipline §5) |
|----------------|------------------------------|---------------------------------------------------------------|--------------------------------------------|---------------------------------------------|
| **`versona-all`** | **Yes** — fast recommendation table | No | No | No |
| **`versona-forge-sdlc`** | **Indirect** — plan lists which rules to invoke | **Yes** — phase-aware **Forge SDLC** pass | **Assigns merge owner** (human, family aggregator, or explicit consolidation step) | No — **delegates** to discipline/family |
| **`versona-family-*`** | No | **Within one domain** only | **Yes** — consolidates that family’s disciplines | **Per child** discipline templates |
| **`versona-pm`** (discipline) | Suggested next Versonas in §5 | No | No | **Yes** — governance §5 |
| **`versona-product-management`** (discipline) | Suggested next Versonas in §5 | No | No | **Yes** — product §5 |
| **`forge-product-manager`** (Cursor package under `product-manager/`) | No | **Product bootstrap** dialog (vision, roadmap, WBS authoring) | No | **Authoring** product artifacts — not a §5 discipline gate |
| **`versona-roadmap-gate`** | Optional `versona-all` | **Roadmap-only** playbook (DoR → PM → follow-ons) | No | No |
| **`versona-project-setup`** | No | **Repo / submodule / rules** bootstrap checklist | No | No |
| **`versona-sampling`** | No | **Demo** meta + tasklets | Merges **tasklet** outputs only | No |

**Prescriptive rule:** **Specialist judgment** lives in **discipline** (and **family_aggregator** merge of specialists). **Methodology orchestration** (`versona-forge-sdlc`) sequences work and names **who merges**; it does not replace Architecture, Security, or Compliance §5 conclusions.

---

## 2. Conceptual flow (main paths)

```blueprint-diagram
key: swimlane
alt: Orchestration routes through routing optional discipline family merge
title: Forge orchestration main paths
summary: How routing, phase-aware orchestration, discipline passes, merge, and trace outputs connect in one governed cycle.
node: Conceptual flow (main paths)
detail: Two complementary lanes for delivery orchestration and inspect-and-adapt feedback.
more: Section 2 frames the default sequence before the numbered walkthrough that follows this diagram.
node: Lane A
detail: The primary path from lens selection through orchestrated discipline work.
more: Typically begins with optional versona-all routing, then versona-forge-sdlc phase planning and rule invocations.
node: handoff
detail: Explicit transfer between routing, orchestration, and specialist discipline passes.
more: Each handoff should name merge owners and work_item_refs so context stays traceable across rules.
node: shared outcome
detail: Consolidated artifacts and trace outputs the orchestration run must leave behind.
more: Includes the orchestration plan, discipline §5 pointers, and Ember Log when scope or risk acceptance changed.
node: Lane B
detail: The parallel inspect-and-adapt path for refining plans and specialist outputs.
more: Teams re-run routing or discipline passes when context is stale or merge disagreements surface.
node: inspect / adapt
detail: Review merged outputs against phase contracts and escalation defaults.
more: Section 3 merge table and phase A–F contracts in section 4 guide when to escalate versus rework.
node: feedback
detail: Lessons and decisions loop back into the next orchestration cycle.
more: Trace outputs and Ember Log entries inform subsequent Ore intake and phase triggers.
node: Note: Typical pattern:
detail: The numbered list below expands each lane into concrete rule invocations.
fallback_ascii: |
  Conceptual flow (main paths)

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback

  Note: Typical pattern:
```

**Typical pattern:**

1. Optional **`versona-all`** when the team is unsure which lenses matter.
2. **`versona-forge-sdlc`** for a **phase-aligned** plan (this doc + `phases.json`).
3. Invoke **discipline** rules (or **`versona-family-*`** when the whole domain should run).
4. **Merge** per phase rules (family template, Governance PM, or human consolidation).
5. **Trace:** session folder, Ember Log, optional §5.1 standards fields ([`../standards/README.md`](../standards/README.md)).

---

## 3. Merge and escalation defaults

| Situation | **Merge owner** | **Escalate when** |
|-----------|-----------------|-------------------|
| Multiple **Product** lenses on same Ore/Ingot | **`versona-family-product`** or human PM | Strategic conflict → **Ember Log** + Product hat |
| Multiple **Engineering** lenses on same Spark | **`versona-family-engineering`** or Tech lead consolidation | Critical severity disagreement → **Architecture** + **Assay** evidence |
| **Security vs Compliance** vs delivery pressure | **Separate** §5 passes; **Governance** (`versona-pm`) or human **Assay** owner merges **release** decision | **L1–L2** control conflict → [`../standards/precedence.md`](../standards/precedence.md), not vote |
| **Router** disagrees with orchestrator | **Orchestrator** wins for **ordering**; **discipline** wins for **technical truth** | Stale context — re-run with explicit `work_item_refs` |

---

## 4. Phase-aware workflow contracts (A–F)

```blueprint-diagram
key: linear
alt: Phases A through F with optional parallel discipline passes merging to trace outputs
title: Phase-aware workflow contracts
summary: How Forge SDLC phases A–F bound triggers, parallel discipline passes, merge rules, and trace outputs.
node: Phase-aware workflow contracts (A–F)
detail: The six lifecycle phases that structure methodology orchestration contracts.
more: Ceremonies C1–C6 map through foundation-connection.md; Sparks use discover: through release: prefixes per SDLC.md.
node: Start
detail: A phase begins when its triggers and entry conditions are satisfied.
more: Section 4 defines triggers per phase—from new Ore intake in Discover to Assay Gate pass in Release.
node: Core steps (see walkthrough below)
detail: Parallel or sequential discipline passes governed by merge and escalation defaults.
more: Each phase table specifies when lenses run in parallel, required sequential order, and who merges §5 outputs.
node: Outcome
detail: Phase-complete trace artifacts and handoff to the next lifecycle stage.
more: Outputs include Ore, Ingot, or Spark records, §5 artifacts, evidence packs, and Ember Log decisions.
node: Note: Triggers
detail: Entry signals that activate each phase contract are listed per phase below.
more: Triggers span Ore intake and refinement through Assay readiness, verify Sparks, and ship checklist completion.
fallback_ascii: |
  Phase-aware workflow contracts (A–F)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: Triggers
```

Ceremony mapping (C1–C6) stays in [`../foundation-connection.md`](../foundation-connection.md). Sparks use phase prefixes `discover:` … `release:` per [`../../SDLC.md`](../../SDLC.md).

### A — Discover

| Contract element | Guidance |
|------------------|----------|
| **Triggers** | New **Ore**; problem/opportunity intake; retro → new Ore |
| **Entry conditions** | Raw intent captured; hat declared if solo/multi-hat |
| **Standards checks** | L1 data class / jurisdiction hints → **Compliance** early if unknown PII |
| **Parallel when** | **Product** lenses (PM, BA, UX) + **cross-cutting** (Security, Compliance) **in parallel** on **different aspects** of same Ore — OK if outputs merged before Ingot |
| **Sequential when** | **Compliance** “in scope?” before **Marketing** claims if regulated sector |
| **Merge rules** | **`versona-family-product`** or PM-led summary; cross-cutting concerns **listed**, not voted down by product |
| **Escalation** | Ore too large → split Ore; legal blocker → **Bank** + counsel |
| **Trace outputs** | Ore record + optional `forge-logs/versona/.../outputs/` + Ember Log if scope accepted |

### B — Specify

| Contract element | Guidance |
|------------------|----------|
| **Triggers** | Refinement (**Ore → Ingot**); `specify:` Sparks |
| **Entry conditions** | Ore triaged; acceptance path visible |
| **Standards checks** | **Compliance** for DPIA/lawful basis; **Security** for data flows |
| **Parallel when** | **BA** + **PM** + **Architecture** sketch in parallel **after** problem statement shared |
| **Sequential when** | **BA** acceptance shape **before** **Architecture** non-functional hardening on same Ingot |
| **Merge rules** | **Ingot** owner (usually Product hat) consolidates; **versona-pm** if delivery date/dependency conflict |
| **Escalation** | Cannot agree AC → **Rework** Ingot, not silent Spark split |
| **Trace outputs** | Ingot doc + §5 artifacts + Ember Log on AC cuts |

### C — Design

| Contract element | Guidance |
|------------------|----------|
| **Triggers** | **Ingot → Sparks** planning; `design:` Sparks; ADR need |
| **Entry conditions** | Ingot **Ready** for technical decomposition |
| **Standards checks** | **Security** threat assumptions; **Compliance** for design-time controls |
| **Parallel when** | **Architecture** + **Data** + **SE** review **different** Sparks — parallel |
| **Sequential when** | **Architecture** **system shape** before **SE** **module-level** §5 on **same** Spark |
| **Merge rules** | **`versona-family-engineering`** when whole stack unclear; else lead engineer merges ADR + Spark list |
| **Escalation** | Architecture split vote → **Ember Log** + optional **Assay** design checkpoint |
| **Trace outputs** | ADR links on Sparks; design session outputs |

### D — Build / Charge

| Contract element | Guidance |
|------------------|----------|
| **Triggers** | Daily **Charge**; `build:` Sparks; **C3** daily sync |
| **Entry conditions** | Spark in **Charge**; DoD understood |
| **Standards checks** | **Org** coding baseline (L2/L3); **agentic** standards when AI-assisted ([`../../agentic-coding-standards.md`](../../agentic-coding-standards.md)) |
| **Parallel when** | **SE** + **Testing** + **DevOps** on **same** Spark only if **separate concerns** (code vs test vs pipeline) — merge in one review or CI |
| **Sequential when** | **SE** implementation **before** **Testing** §5 **sign-off** on same change set (typical) |
| **Merge rules** | Implementer merges code; **Testing** §5 feeds **Review** / **Verify** |
| **Escalation** | **Blocked** vs **Banked** per [`../process-and-flows.md`](../process-and-flows.md) |
| **Trace outputs** | PRs, CI logs, session notes |

### E — Verify

| Contract element | Guidance |
|------------------|----------|
| **Triggers** | **Review**; **Assay** prep; `verify:` Sparks |
| **Entry conditions** | Build artifacts available; test plan aligned |
| **Standards checks** | **Compliance** evidence; **Security** for penetration/review gates |
| **Parallel when** | **Testing** + **Security** + **Compliance** **parallel** on **release candidate** — merge at **Assay** |
| **Sequential when** | **Testing** “must fix” **before** **Security** final pass on same build |
| **Merge rules** | **Governance** hat or **versona-pm** consolidates **Assay** readiness table |
| **Escalation** | Critical findings → **Rework** or scoped **Proceed with conditions** with dated follow-up Sparks |
| **Trace outputs** | Evidence pack links; Assay record |

### F — Release

| Contract element | Guidance |
|------------------|----------|
| **Triggers** | **Assay Gate** pass; `release:` Sparks; ship checklist |
| **Entry conditions** | **E** evidence complete per work type |
| **Standards checks** | **L1–L2** release controls; customer comms if contractual |
| **Parallel when** | **DevOps** (ship) + **Marketing** + **CS** prep **parallel** after **Assay** decision |
| **Sequential when** | **Assay** decision **before** any **production** promotion |
| **Merge rules** | **Governance** / release manager owns **go/no-go** narrative |
| **Escalation** | Emergency bypass → **explicit waiver** + Ember Log ([`../standards/schemas/waiver-record.schema.json`](../standards/schemas/waiver-record.schema.json)) |
| **Trace outputs** | Release notes, tags, Ember Log decision, learning → **Ore** |

---

## 5. Trace outputs (orchestration layer)

Every **`versona-forge-sdlc`** run should leave:

1. **Orchestration plan** (markdown) — phases touched, **parallel vs sequential** steps, **merge owner**, suggested rule invocations.
2. **Pointers** to discipline §5 outputs (paths or session IDs).
3. **Ember Log** line when scope, priority, or risk acceptance changed.
4. Optional **§5.1 standards traceability** on the consolidating pass ([`../versona/VERSONA-CONTRACT.md`](../versona/VERSONA-CONTRACT.md) §5.1).

---

## 6. References

- [`../versona/catalog/workflow/versona-forge-sdlc.mdc.template`](../versona/catalog/workflow/versona-forge-sdlc.mdc.template)
- [`../versona/VERSONA-FRAMEWORK.md`](../versona/VERSONA-FRAMEWORK.md)
- [`../planning/README.md`](../planning/README.md)
- [`../../../../agents/ORCHESTRATION.md`](../../../../agents/ORCHESTRATION.md) — **execution** recipes (different from methodology orchestration)
