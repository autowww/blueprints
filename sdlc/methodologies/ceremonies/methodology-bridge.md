# Methodology bridge — foundation intents ↔ named ceremonies

## Purpose

This file is the **crosswalk** between methodology-neutral **intent types** (C1–C6 in [`ceremony-foundation.md`](ceremony-foundation.md)) and what **Scrum, Kanban, phased delivery, and XP** usually **call** the rituals that satisfy those intents. Use it when:

- You **blend** frameworks (e.g. Scrum cadence + Kanban flow metrics).
- You rename meetings but want to verify **no intent is orphaned**.
- You **onboard** people who know one methodology and need to map vocabulary.

**Forks (detail + event-level suggestions):** [Scrum](scrum.md) · [Kanban](kanban.md) · [Phased](phased.md) · [XP](xp.md) · [SAFe](safe.md) · [Lean](lean.md) · [Spiral](spiral.md) · [V-Model](v-model.md) · [DevOps](devops.md) · [Forge](forge.md)

---

## Bridge matrix — intent × methodology (typical “nodes”)

Cells list **common names** for practices that **primarily** serve that intent. One **calendar event** may cover **multiple** intents (e.g. planning = C1 + C2); see fork files for primary → secondary ordering.

| Intent | Scrum (typical) | Kanban (typical) | Phased (typical) | XP (typical) | SAFe (typical) | Lean (typical) | Spiral (typical) | V-Model (typical) | DevOps (typical) | Forge (typical) |
|--------|-----------------|------------------|------------------|--------------|----------------|----------------|------------------|-------------------|------------------|------------------|
| **C1 Align** | Sprint Goal conversation; backlog refinement themes | Replenishment context; service strategy | Requirements / design **reviews**; charter alignment | Planning game (scope negotiation); onsite customer dialogue | **PI Planning** (vision, architecture briefing); portfolio strategic themes | **Value-stream mapping**; strategic A3 | **Spiral planning** (Q1: objectives, alternatives) | **Requirements review**; stakeholder alignment | **Architecture review** with operability lens; SLO setting | **Refinement** (Ore → Ingot); Bellows challenge at decision points |
| **C2 Commit** | Sprint Planning (forecast + Sprint Backlog) | **Replenishment**; pulling into “ready/doing” | Phase entry authorization; **baseline** sign-off to enter build | Stories selected for immediate iteration | PI Planning (team breakouts, **PI Objectives**); Iteration Planning | **Pull-based** selection; last responsible moment | Q1 + Q4: commit to risk-reduction approach | **Design review**; test plan paired with design | **Sprint planning** includes deployment and infra tasks | **Planning** (Ingot → Sparks); iteration scope; **Charge** selection |
| **C3 Sync** | **Daily Scrum** | Stand-up / flow meeting | **Coordination** meetings inside a phase; integration forums | Pair rotation check-ins; implicit in pairing | Daily Stand-up + **ART Sync** (Scrum of Scrums, PO Sync) | **Stand-up** (flow-focused); **Gemba** walks | **Dev sync** (Q3); approach varies by spiral | **Development sync** during implementation (bottom of V) | **Stand-up** includes pipeline health and deployment status | **Daily sync** (Charge confirmation); hat declaration; blocker surfacing |
| **C4 Inspect** | **Sprint Review** | Service delivery review (service vs expectations) | **UAT**; milestone demos; validation reviews | **Small release** feedback; customer acceptance | **System Demo**; Iteration Review; **I&A** (quantitative review) | Customer feedback; **delivery review** | **Prototype demo**; **anchor-point review** (Q4) | **Test result review**; acceptance review (top-right of V) | **Deployment review**; **SLO review**; DORA metrics | **Review** (evidence assessment); Bellows discipline challenge |
| **C5 Improve** | **Sprint Retrospective** | Ops review; Kaizen / retrospective cadence | **Post-phase** lessons; process audits (lighter between gates) | Team reflection; coach feedback loops | **I&A** (problem-solving workshop); Iteration Retrospective | **Kaizen** events; **A3** problem-solving; **Five Whys** | **Retrospective**; risk-prediction accuracy review | **Post-phase lessons** (often deferred; better teams add mid-cycle retros) | **Blameless post-mortem**; **pipeline retrospective** | **Retro** (metrics, Ember Log review, Bellows tuning); learning → new Ore |
| **C6 Assure** | **Definition of Done** + increment quality; release may be separate | **Policies** / DoD per column; release train | **IV&V**; test phase exit; **release approval** | **TDD**, **CI**, collective ownership | **Continuous delivery pipeline**; built-in quality; release on demand | **Built-in quality** practices; policy-driven DoD | **Risk review** (Q2); evidence-based milestone gates | **Test readiness review**; traceability gates per V-level | **Automated pipeline gates**; CI/CD quality checks | **Assay Gate** (evidence-based release decision); per-work-type evidence |

**Empty-looking cells:** XP often **embeds** C3/C6 in practices rather than a named meeting—see [XP fork](xp.md). Lean **embeds** C6 in engineering practices rather than ceremonies. Spiral **embeds** C6 in Q2 risk analysis. **Forge** adds Bellows (discipline challenge agents) as a cross-cutting challenge mechanism activated at any ceremony—see [Forge fork](forge.md).

---

## Cross-methodology suggestions

These apply **regardless** of framework; tune with your [roles](../roles-archetypes.md) and [phases](../../SDLC.md).

| Topic | Suggestion |
|-------|------------|
| **Cover every intent** | Over a **horizon** (e.g. two weeks), you should **touch** C1–C6 somehow—not necessarily six meetings. Missing **C5** shows up as repeating mistakes; missing **C4** as surprise rejection at release. |
| **Don’t double-book intents** | If **C2** happens only in a giant monthly meeting, **C3** still needs a **lighter** rhythm or async channel so blockers don’t wait four weeks. |
| **Name intents in invites** | e.g. “Daily — **C3** sync; not for backlog reorder (**C2**)” reduces PO hijack. |
| **Blends** | **Scrumban:** keep Scrum **C2/C4** time-boxes if helpful; add Kanban **WIP** and **aging** to **C3/C5**. **Phased + iterative:** use **gates** for **C6** at phase exits; use **Sprint Review–style C4** inside implementation for stakeholders. **SAFe + Kanban teams:** ART cadence (PI Planning, System Demo) provides **C1/C4** at program level; individual teams may use Kanban flow instead of iteration time-boxes. |
| **Evidence** | For **C6** in regulated contexts, store **decisions** where **Steer** expects them ([`phased-delivery.md`](../phased-delivery.md)); git activity alone is rarely enough. |
| **Tracking** | Ceremonies **consume** aggregates from [`sdlc/TRACKING-FOUNDATION.md`](../../../../sdlc/TRACKING-FOUNDATION.md) pattern repos—they don’t replace **work-unit ids** in commits. |

---

## Per-intent bridge notes (how methodologies differ)

### C1 Align

- **Scrum:** Sprint Goal + Product Goal connection.  
- **Kanban:** Alignment often **continuous** via policy and replenishment **context**, less a single “goal statement.”  
- **Phased:** Alignment **frozen** at baselines—later change is **change control**, not casual replanning.  
- **XP:** **Customer** proximity compresses alignment into **ongoing** conversation.
- **SAFe:** PI Planning creates **ART-wide alignment** around vision, architecture, and PI Objectives — stronger alignment event than any single-team ceremony.
- **Lean:** **Value-stream mapping** and strategic **A3** drive alignment on what is valuable and where waste lies.
- **Spiral:** **Spiral planning** (Q1) defines objectives, alternatives, and constraints for each cycle — alignment is revisited every spiral.
- **V-Model:** **Requirements review** establishes the top of the V — alignment on what the system must do and how acceptance will be tested.
- **DevOps:** **Architecture review with operability lens** — include SLOs, monitoring, and deployment strategy in design decisions from the start.

### C2 Commit

- **Scrum:** Explicit **forecast** for one Sprint.  
- **Kanban:** **Pull** when capacity and policy allow—commitment is **flow-based**, not necessarily a batch.  
- **Phased:** Commitment = **authorized to enter next phase** with a **package**.  
- **XP:** **Small batches**—commitment horizon is **short** by design.
- **SAFe:** **PI Objectives** are the commitment unit — teams forecast committed and stretch objectives for the entire PI (8–12 weeks).
- **Lean:** **Pull-based** selection at the **last responsible moment** — commitment is flow-governed, not calendar-bound.
- **Spiral:** Commitment is to a **risk-reduction approach** for the current spiral, not to a fixed deliverable scope.
- **V-Model:** Commitment includes **both** the design approach **and** the paired test approach — test plans are drafted during design.
- **DevOps:** Planning includes **deployment tasks**, infrastructure work, and reliability improvements alongside feature work.

### C3 Sync

- **Scrum:** Daily, **Developers**-centric per Guide.  
- **Kanban:** Frequency scales with **interrupt** rate and **dependency** count.  
- **Phased:** Sync may be **weekly** status + **ad hoc** integration when handoffs are heavy.  
- **XP:** **Pairing** reduces need for status **broadcast** but not for **dependency** sync across pairs.
- **SAFe:** **Two-tier sync** — Daily Stand-up within teams, **ART Sync** (Scrum of Scrums + PO Sync) across teams weekly.
- **Lean:** **Flow-focused** stand-up (board walk) and **Gemba walks** — sync is about the work, not individual status.
- **Spiral:** Sync during Q3 build; teams may use any approach (Agile iterations, focused builds) appropriate to the spiral’s risk profile.
- **V-Model:** **Development sync** during implementation (bottom of V); coordination on integration interfaces.
- **DevOps:** **Pipeline health** and deployment status are part of daily sync; pipeline failures are blockers.

### C4 Inspect

- **Scrum:** Stakeholder-facing **Review** each Sprint.  
- **Kanban:** May be **on demand** or **service review** on a slower cadence than delivery.  
- **Phased:** **Formal** inspection at **gate** with evidence.  
- **XP:** **Frequent** slices to customer or proxy.
- **SAFe:** **System Demo** every iteration (cross-team integration); **I&A** at PI end for quantitative and qualitative review.
- **Lean:** **Customer feedback** on delivered value; **delivery review** measures outcomes, not just outputs.
- **Spiral:** **Prototype demos** validate risk-reduction evidence; **anchor-point reviews** (Q4) evaluate spiral results and gate next investment.
- **V-Model:** **Test result reviews** at each V-level; **acceptance review** validates the complete system against stakeholder needs.
- **DevOps:** **Deployment review** pre-deployment; **SLO review** measures reliability performance; DORA metrics track delivery health.

### C5 Improve

- **Scrum:** **Retro** every Sprint.  
- **Kanban:** Often **separate** service / ops improvement cadence.  
- **Phased:** Improvement may lag until **post-project** unless you add **explicit** retro inside phases.  
- **XP:** **Values** + coach; retro optional if team is **disciplined** elsewhere.
- **SAFe:** **I&A problem-solving workshop** is the primary ART-level improvement; teams also run iteration retros. Improvement items flow into the next PI backlog.
- **Lean:** **Kaizen events**, **A3 problem-solving**, and **Five Whys** — systematic root-cause analysis, not just sentiment-based retros.
- **Spiral:** Retrospective compares **predicted vs actual** risk outcomes; improves risk identification and estimation capability.
- **V-Model:** Improvement is often **post-project** (lessons learned). Better teams add **mid-cycle** retros during long development phases.
- **DevOps:** **Blameless post-mortems** learn from incidents; **pipeline retrospectives** review DORA metrics and reduce toil.

### C6 Assure

- **Scrum:** **DoD** is team-owned; PO **accepts** increment.  
- **Kanban:** **Policies** are first-class; quality is **of the system**.  
- **Phased:** **Independent** verification is common.  
- **XP:** **Technical practices** are the primary assurance mechanism.
- **SAFe:** **Continuous delivery pipeline** and **built-in quality** practices span all teams; **release on demand** decouples release from PI cadence.
- **Lean:** **Built-in quality** practices (TDD, CI, automation) — quality is a practice embedded in flow, not a separate phase or ceremony.
- **Spiral:** **Risk review** (Q2) provides assurance through systematic risk analysis; **anchor-point milestones** gate resource commitment with evidence.
- **V-Model:** **Traceability gates** at each V-level — requirements → design → test cases → test results. **Test readiness reviews** gate test execution.
- **DevOps:** **Automated pipeline gates** (CI/CD) provide continuous assurance — build, test, scan, deploy. Quality is automated, not ceremonial.

---

## How to map your own calendar to C1–C6

1. List recurring events (and **async** rituals: e.g. “Friday PR digest”).  
2. For each, ask: which **outcome** (align, commit, sync, inspect, improve, assure) is **non-negotiable**?  
3. If an event tries to do **all six**, split or **time-box** parts—or accept **weak** outcomes.  
4. Compare to this matrix: if your methodology **expects** a node (e.g. Scrum **Review**) and you skipped it, decide whether another practice **covers** the same intent.  
5. Record **project-specific** names in `sdlc/` (consuming repo), not new blueprint intent IDs.

---

## Related reading

| Doc | Why |
|-----|-----|
| [`ceremony-foundation.md`](ceremony-foundation.md) | Phase × intent matrix; **suggestions by intent** |
| [`README.md`](README.md) | Package index |
| [`roles-archetypes.md`](../roles-archetypes.md) | Who leads each intent |
| [`agile.md`](../agile.md) | Blending under Agile umbrella |
