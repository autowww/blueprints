---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Scrum — roles (prescriptive)

Normative terms: [**Scrum Guide**](https://scrumguides.org/scrum-guide.html). This page adds **blueprint** expectations: archetypes, event participation, and RACI-style clarity.

## 0. Scrum Team vs sub-accountabilities

The **Scrum Team** = **Product Owner** + **Scrum Master** + **Developers** (one team, shared success). **Developers** means everyone who creates the increment—not only people with “developer” in their job title (e.g. testers, UX in the team count here). The Guide separates **accountabilities** so ordering/value, process health, and build/quality do not collapse into one overloaded role.

## 0.1 Map to this blueprint (foundation)

| Foundation element | PO | SM | Developers |
|--------------------|----|----|------------|
| **Phases A–F** | Strong in **A–B** (shape/plan intent); **D–E** acceptance lens | **C–F** via facilitation & impediments | **B–E** build/verify; **F** via retro actions |
| **Tracking spine** (intent → PR → release) | Owns **value ordering** and **acceptance** at boundaries | Ensures **transparency** (boards, metrics honest) | **Link work** to PBIs/tasks; meet **DoD** |
| **Ceremony intents C1–C6** | **C1/C2** in planning & refinement; **C4** in Review | **C3–C5** facilitation default | **C2–C4** execution; **C5** co-owner of improvements |
| **Archetypes** (see [roles-archetypes.md](../roles-archetypes.md)) | Sponsor proxy, Orchestrator | Orchestrator, Quality advocate | Implementer, Quality advocate |

## 0.2 Commitments and who “holds” them

Scrum’s commitments are **Product Goal**, **Sprint Goal**, **Definition of Done**. No single role owns them alone in practice—use this as a **default split**:

| Commitment | Primary steward | Others |
|------------|-----------------|--------|
| **Product Goal** | PO (articulates, keeps visible) | SM (ensures focus); Developers (technical implications) |
| **Sprint Goal** | **Whole Scrum Team** (negotiated in Planning) | PO proposes scope direction; Developers assert feasibility |
| **Definition of Done** | **Developers** (create/maintain quality standard) | PO must not weaken DoD for “speed”; SM escalates if org blocks DoD |

## 1. The three accountabilities

### Product Owner (PO)

| Aspect | Prescriptive guidance |
|--------|------------------------|
| **Accountable for** | Maximizing product value from the work of the Scrum Team; effective Product Backlog management |
| **Typical archetypes** | **Sponsor proxy**, **Orchestrator** (prioritization with stakeholders) |
| **Single wringable neck** | One PO per product (not a committee); may delegate *execution* of backlog edits but not *accountability* |
| **Daily involvement** | Available for clarification; not required at every Daily Scrum (team choice) |

**Outputs owned or approved by PO:** Product Goal statement, ordered backlog, transparent backlog items, release intent per increment.

### Scrum Master (SM)

| Aspect | Prescriptive guidance |
|--------|------------------------|
| **Accountable for** | Establishing Scrum as defined; team effectiveness |
| **Typical archetypes** | **Orchestrator** (facilitation), **Quality advocate** (organizational impediments to good practice) |
| **Serves** | Scrum Team, PO, wider organization (coaching, teaching, facilitating change) |
| **Not** | Project manager, team lead who assigns tasks, sole note-taker |

**Outputs:** Impediment visibility, improvement backlog items, facilitated events, transparency on Scrum health.

### Developers (the whole Scrum Team minus PO/SM for “who builds”)

| Aspect | Prescriptive guidance |
|--------|------------------------|
| **Accountable for** | All aspects of quality each Sprint; creating the plan for the Sprint (Sprint Backlog); adapting plan daily toward Sprint Goal |
| **Typical archetypes** | **Implementer** (primary), **Quality advocate** (shared), **Orchestrator** (rotating facilitator for Daily Scrum) |
| **Cross-functional** | All skills needed to produce Done increment (or honest gap = escalation) |

**Outputs:** Increment meeting Definition of Done, Sprint Backlog updates, technical debt visibility, estimates used in planning.

## 2. Event participation matrix (who must be where)

Legend: **R** = required · **O** = optional but common · **—** = not expected

| Event | PO | SM | Developers | Stakeholders |
|-------|----|----|------------|--------------|
| **Backlog refinement** (ongoing) | R | O | R | O |
| **Sprint Planning** | R | R | R | — |
| **Daily Scrum** | — | O | R | — |
| **Sprint Review** | R | R | R | R (invited) |
| **Sprint Retrospective** | R* | R | R | — |

\*PO attends unless team explicitly experiments with Dev-only retro variant **and** PO gets a separate feedback loop — document that exception; default is **PO present**.

### Daily Scrum facilitation

The **Developers** run the Daily Scrum; **any Developer** may facilitate. The **SM** may facilitate only if requested—and should coach the team toward self-management rather than permanently hosting.

## 2.1 Backlog refinement — RACI-style (ongoing)

| Outcome | PO | SM | Developers |
|---------|----|----|------------|
| Order & clarity of top backlog | **A**/R | C | C |
| Item “ready” (acceptance, size) | **A** on value | C | **R** (feasibility, splitting) |
| Estimates / forecast input | C | C | **R** |

## 3. RACI-style view (per event outcome)

### Sprint Planning — outcomes

| Outcome | PO | SM | Developers |
|---------|----|----|------------|
| Sprint Goal proposed & agreed | **A**/R | C | R |
| Selected PBIs for sprint | **A** | C | C |
| Sprint Backlog plan (how) | C | C | **A**/R |
| Forecast / capacity alignment | C | C | R |

**A** = accountable, **R** = responsible, **C** = consulted.

### Sprint Review — outcomes

| Outcome | PO | SM | Developers |
|---------|----|----|------------|
| Increment demonstrated | C | F | **R** |
| Stakeholder feedback captured | **R** | F | C |
| Product Backlog updates | **A**/R | C | C |

**F** = facilitate (often SM).

### Sprint Retrospective — outcomes

| Outcome | PO | SM | Developers |
|---------|----|----|------------|
| Safe discussion | C | **R** | R |
| Improvement actions | R | C | **R** |
| Follow-through tracking | C | **R** | R |

## 4. Interface with “extra” roles (chapter leads, architects)

| External role | How it fits Scrum |
|-----------------|-------------------|
| **Engineering lead / architect** | Participates as Developer or specialist; does not override Developers’ plan without team agreement |
| **Sponsor** | Feeds PO; attends Review when useful |
| **PM (non-PO)** | Coordination role — must not contradict PO ordering; clarify with PO |
| **Chapter / guild lead** | Same as engineer: participates as Developer unless explicitly outside the Scrum Team |
| **Stakeholders** | Not part of the Scrum Team; attend **Review** by invitation; no Sprint Backlog edits |

## 4.1 Anti-patterns (by accountability)

| Anti-pattern | Why it hurts | Lean fix |
|--------------|--------------|--------|
| **PO committee** or “everyone prioritizes” | No clear ordering; slow decisions | Single PO accountable; others advise |
| PO writes all stories alone | Misses technical risk and “ready” | Developers in refinement (**2.1**) |
| **SM assigns tasks** | Destroys Developer ownership of plan | Team pulls work; SM removes impediments |
| SM only admin / Jira clerk | Scrum theory not lived; no improvement | SM coaches org + team on empiricism |
| **Tech lead overrides** Developers’ plan | Breaks collective ownership | Lead contributes as Developer; escalate conflicts to PO/SM |
| Skipping PO from Retro without agreement | Loses systemic product feedback | Default PO in Retro; document exceptions |

## 4.2 Agentic SDLC (same accountabilities)

Coding agents **do not** replace PO acceptance, SM’s process accountability, or Developers’ ownership of quality and Sprint Backlog plan. Treat agent output like any other contribution: traceable to PBIs, reviewed by humans, covered by **DoD**. See [agentic-sdlc.md](../agentic-sdlc.md).

## 4.3 Scaling note

Multiple teams on one product (e.g. Nexus, LeSS) add **roles or events at scale** but keep the same **three accountabilities** per team; align PO structure so **one ordered backlog** per product is unambiguous.

## 5. Links

- [Foundation connection](foundation-connection.md) · [Ceremonies](ceremonies-prescriptive.md) · [roles-archetypes.md](../roles-archetypes.md)
