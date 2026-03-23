# Phased delivery — connection to the SDLC foundation

Phased delivery organizes work into **sequential or overlapping stages** with **gates** (approvals, artifacts). The blueprint’s **A–F** phases still apply as a **lifecycle vocabulary**; phased methods add **baselines**, **change control**, and **formal sign-off**.

## 1. SDLC A–F vs project stages

| Blueprint phase | Typical phased stage artifacts |
|-----------------|--------------------------------|
| **A — Shape** | Charter, business case, high-level requirements |
| **B — Plan** | Schedule, WBS, detailed design baseline |
| **C — Build** | Construction / implementation per baseline |
| **D — Verify** | Test phases (unit, integration, UAT), audits |
| **E — Release** | Deployment plan, go-live checklist, handover |
| **F — Operate & learn** | Warranty, hypercare, benefits realization |

**Prescriptive rule:** Map your **stage names** to A–F in the **project RAID** or handbook so agents and audits speak one language.

## 2. Tracking spine (mandatory)

Phased projects often use documents more than boards; still maintain:

| Artifact | Phased expression |
|----------|-------------------|
| **Intent** | CR / requirement ID in RM tool |
| **Spec** | SRS, design doc baseline |
| **Plan** | WBS + schedule activity |
| **Tasks** | Work packages |
| **PRs** | Still link implementation to requirement IDs |
| **Reviews** | Inspection records, approval signatures |
| **Release** | Release record, CM tag |

## 3. Ceremony intents ↔ phased meetings

| Intent | Phased ceremony examples |
|--------|---------------------------|
| **C1** | Steering committee; gate review **go/no-go** |
| **C2** | Planning workshop; design review |
| **C3** | War room; weekly status (execution) |
| **C4** | Test readiness review; UAT sign-off |
| **C5** | Post-implementation review (PIR); lessons learned |
| **C6** | Knowledge transfer; training handover |

## 4. Role archetypes

| Role | Archetypes |
|------|------------|
| **Sponsor / SRO** | **Sponsor proxy**, **Steer** |
| **Project / program manager** | **Orchestrator** |
| **Business analyst** | **Orchestrator**, **Implementer** (specs) |
| **Tech lead / architect** | **Quality advocate**, **Implementer** |
| **Delivery team** | **Implementer** |

## 5. Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| Gate as paperwork only | Define **objective exit criteria** per gate |
| Late scope via informal email | Route through **change control** (see blueprint change chapter) |
| UAT as first real user test | Shift **C4** left with incremental builds where possible |

## 6. Links

- [`https://forgesdlc.com/methodologies-phased-delivery.html`](https://forgesdlc.com/methodologies-phased-delivery.html) · [ceremonies/phased.md](../ceremonies/phased.md)
