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
key: flow
alt: Phases A through F with optional parallel discipline passes merging to trace outputs
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
