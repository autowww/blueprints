# Forge — meeting model (operational)

**Purpose:** Preserve the **minimal memorable set** of Forge **meetings**, how they are **delivered** (human-only, hybrid, Versona-assisted), and what **accountability** requires—without inventing a parallel taxonomy. **Meeting** is the primary public term. This document extends [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) (inputs, outputs, agendas) with **delivery modes**, **decision ownership**, and **anti-patterns**.

**Scrum as memory aid:** Forge uses a similar *shape* (short daily sync, time-boxed planning, review, retro, gate) but does **not** copy Scrum mechanics verbatim—see iteration language (Ore → Ingot → Spark → Charge) in [`process-and-flows.md`](process-and-flows.md).

**Charge:** Meetings are **not** modeled as items *inside* **Charge**. Charge is today’s selected Sparks; the **daily sync** *confirms* Charge—see [`daily/README.md`](daily/README.md).

**Artifacts & decisions:** How durable artifacts, owners, and meetings connect across PDLC/SDLC — [`ARTIFACT-AND-DECISION-MODEL.md`](ARTIFACT-AND-DECISION-MODEL.md).

---

## 1. Meeting delivery modes

Meetings use **delivery modes**, not separate object types:

| Mode | Meaning |
|------|---------|
| **Human-only** | Facilitation and accountable decisions are human-led in the room or on a live call. |
| **Hybrid** | Humans in the loop; Versonas prepare drafts, checklists, or §5-shaped discipline passes that humans review and sign. |
| **Versona-only** | Session used to **prepare, simulate, synthesize, or draft** (e.g. async package before a human sign-off). **Not** a substitute for human accountability on binding decisions—see §6. |

---

## 2. Recommended meeting set (lean default)

| Meeting | In default cadence? |
|---------|---------------------|
| **Refinement** (Ore → Ingot) | Yes |
| **Planning** (Ingot → Sparks) | Yes (iteration start) |
| **Daily sync** | Yes (every working day; short) |
| **Review** (inspect increment + evidence posture) | Yes (iteration end) |
| **Assay Gate** (release decision) | Yes when a release candidate exists |
| **Retrospective** | Yes (regular, iteration end) |
| **Ad hoc decision meeting** | **Only** when real decision pressure exists—not a standing weekly slot |

**Ore intake** remains **continuous**, not a scheduled meeting.

---

## 3. Refinement vs Planning

| Question | Answer |
|----------|--------|
| **Default** | **Refinement is its own meeting.** Different primary question: shape *what* is plannable (Ore → Ingot) vs commit *how much* and *which* Sparks (Planning). |
| **Conditional merge** | **Very small teams** or **very low Ore throughput** may use **one combined calendar block** (“Planning + refinement”) **only if** Ingots still satisfy **Definition of Ready** *before* Sparks are committed—you merged the *schedule*, not the *gate*. |
| **Never** | Treating refinement as *always* part of Planning—this collapses backlog shaping into scope commitment and invites thrash. |

---

## 4. Meeting matrix (delivery modes)

| Meeting | Trigger / cadence (lean) | Timebox (typical) | Human-only | Hybrid | Versona-only |
|---------|--------------------------|-------------------|------------|--------|----------------|
| Refinement | 1× weekly (2× if Ore flow is high) | ≤ 1 h | ✓ | ✓ | ✓ (draft; **Ingot promotion** human-signed) |
| Planning | Start of 1-week iteration | ≤ 2 h | ✓ | ✓ | ✓ (decomposition drafts; **scope** human-signed) |
| Daily sync | Every working day | 15 min | ✓ | ✓ | ⚠ prefer assistant, not sole chair |
| Review | End of iteration | ≤ 1.5 h | ✓ | ✓ | ✓ (prep; **readiness** human) |
| Assay Gate | When candidate + evidence package ready | ≤ 30 min | ✓ | ✓ | ✓ (checklist; **release** human) |
| Retrospective | End of iteration | ≤ 1 h | ✓ | ✓ | ✓ (themes; **experiments** human-owned) |
| Ad hoc decision | Decision pressure only | 30–90 min | ✓ | ✓ | ✓ (options; **decision** human) |

**Daily sync:** Versona-only is a poor fit as the *team* event; use Versona to **support** a human-led standup, or stay human-only when presence is required.

---

## 5. Per-meeting specification

Each subsection uses the same field names. **Inputs** means tracking-spine material (Ore, Ingots, Charge, logs)—not a separate “artifact object” taxonomy.

### 5.1 Refinement (Ore → Ingot)

| Field | Detail |
|-------|--------|
| **Name** | Refinement |
| **For what** | Turn selected Ore into **Ingots** plannable with clear acceptance and evidence expectations. |
| **Why** | Without shaping, Planning commits guesses; rework rises. |
| **Primary decision question** | Which Ore becomes an Ingot (ready), merged, Banked, or rejected—and on what terms? |
| **Trigger / cadence** | Standing: 1× weekly (2× if intake is heavy). |
| **Suggested timebox** | ≤ 1 h; ~10–15% iteration capacity on refinement over the week. |
| **Allowed delivery modes** | All three; Versona-only may draft Ingots; **human** signs promote/Bank/reject. |
| **Required participants** | Product hat (**R**), Engineering hat (**R**), Challenge hat (**O** — Versonas at decision points). |
| **Human owner** | Product (value/scope framing); Engineering (feasibility band). |
| **Versona owner/support** | Discipline Versonas by risk (architecture, security, compliance). |
| **Required inputs** | Ore backlog, product context, constraints, discipline knowledge links. |
| **Recommended pre-work** | Ranked Ore list; rough sizing; known dependencies. |
| **Agenda / flow** | (1) Top Ore (5–10m) → (2) Problem/value/constraints + feasibility (15–20m) → (3) Versona time-box on high-risk items (10–15m) → (4) Decisions + Ember Log (5–10m). |
| **Created or updated** | Ingots; Ember Log; optional `forge-logs/` notes. |
| **Decisions expected** | Promote / merge / Bank / reject; recorded assumptions. |
| **Exit criteria** | Each promoted Ingot meets Definition of Ready (problem, acceptance, constraints, effort band, phase affinity). |
| **Anti-patterns** | Detailed iteration commitment here; skipping Challenge on risky items; “refinement” that is secretly Planning. |
| **What must never happen** | Binding iteration commitment or Spark pull in this meeting (belongs in Planning). |

### 5.2 Planning (Ingot → Sparks)

| Field | Detail |
|-------|--------|
| **Name** | Planning |
| **For what** | Decompose Ingots into **Sparks**, sequence for risk reduction, fit scope to **capacity** for the iteration. |
| **Why** | Aligns execution with capacity; makes trade-offs explicit before the week runs. |
| **Primary decision question** | What is in scope for this iteration—and in what order—given capacity and risk? |
| **Trigger / cadence** | Start of each iteration (default 1 week). |
| **Suggested timebox** | ≤ 2 h per 1-week iteration. |
| **Allowed delivery modes** | All three; Versona may propose Spark breakdown; **humans** commit scope. |
| **Required participants** | Product (**R**), Engineering (**R**), Governance (**O**). |
| **Human owner** | Product + Engineering (scope content); Governance (policy/evidence fit). |
| **Versona owner/support** | PM/architecture/compliance Versonas as needed. |
| **Required inputs** | Ordered Ingot backlog, capacity, past metrics, Definition of Done. |
| **Recommended pre-work** | Ingots ready; optional Spark candidates drafted. |
| **Agenda / flow** | Focus proposal → decompose → sequence by risk/learning → capacity + margin → Versona needs before risky Sparks. |
| **Created or updated** | Sparks with phase prefixes; iteration scope; Charge seed for day one. |
| **Decisions expected** | In/out list; ordering; explicit “not this week.” |
| **Exit criteria** | Spark quality check passes; scope fits with **slack**; Versona needs flagged. |
| **Anti-patterns** | Ore→Ingot work here; 100% capacity fill; hiding dependencies. |
| **What must never happen** | Treating **Charge** as the planning container (Charge is **daily execution**, confirmed at sync). |

### 5.3 Daily sync

| Field | Detail |
|-------|--------|
| **Name** | Daily sync |
| **For what** | Execute and unblock: confirm today’s **Charge**, hats, blockers, Banking. |
| **Why** | Short loop prevents silent drift. |
| **Primary decision question** | What is today’s Charge—and what must change (Banking, help, follow-up)? |
| **Trigger / cadence** | Every working day. |
| **Suggested timebox** | **15 minutes** (strict). |
| **Allowed delivery modes** | Human-only or hybrid preferred; Versona as **support** (draft Charge, blocker summary), not accountable chair. |
| **Required participants** | Engineering (**R**); Product (**O**); others if blocked. |
| **Human owner** | Engineering (flow); Product (priority/Banking prompts). |
| **Versona owner/support** | Optional: prep of blocker list—does not replace facilitation accountability. |
| **Required inputs** | Current Charge, iteration Sparks, blockers, Ember Log. |
| **Recommended pre-work** | Spark states updated; blockers listed. |
| **Agenda / flow** | Yesterday → today’s Charge → blockers/Banking → hat → Versona needs → **schedule** time-boxed follow-ups (do not expand this meeting). |
| **Created or updated** | Charge for the day; follow-up invites; Ember Log if decisions. |
| **Decisions expected** | Banking/unbanking; who pulls which Spark; whether a follow-up is needed. |
| **Exit criteria** | Everyone knows Charge and next touch on blockers. |
| **Anti-patterns** | Status theater; problem-solving in the 15m; extra standing meetings that duplicate without new decisions. |
| **What must never happen** | Modelling the **meeting** as an item **inside** Charge; letting this become a 45m project meeting. |

### 5.4 Review

| Field | Detail |
|-------|--------|
| **Name** | Review |
| **For what** | Inspect the increment, assess evidence quality, gather feedback, judge **Assay readiness** (not the final ship verdict unless policy merges sessions). |
| **Why** | Connects building to expectations before release pressure peaks. |
| **Primary decision question** | Does the increment meet intent—and are we ready to pursue release evidence / Assay? |
| **Trigger / cadence** | End of iteration. |
| **Suggested timebox** | ≤ 1.5 h. |
| **Allowed delivery modes** | All three for prep; stakeholder-facing demo usually human or hybrid. |
| **Required participants** | Product (**R**), Engineering (**R**), Challenge (**R**), Governance (**R**), stakeholders (**O**). |
| **Human owner** | Product (acceptance narrative); Engineering (demo truth). |
| **Versona owner/support** | Discipline Versonas; evidence summaries. |
| **Required inputs** | Completed Sparks, increment, Assay criteria, Ember Log. |
| **Recommended pre-work** | Demo script; evidence index; known gaps. |
| **Agenda / flow** | Demo → acceptance → discipline review → evidence vs Assay criteria → readiness (distinct from Assay pass/fail). |
| **Created or updated** | Feedback; backlog updates; Assay readiness notes. |
| **Decisions expected** | More evidence vs scope adjust vs proceed toward Assay. |
| **Exit criteria** | Clear readiness position; gaps with owners. |
| **Anti-patterns** | Slide-only review; skipping evidence; lowering Assay standards to match demo mood. |
| **What must never happen** | Confusing **readiness** with **Assay Gate** without an explicit evidence package and governance path. |

### 5.5 Assay Gate (release decision)

| Field | Detail |
|-------|--------|
| **Name** | Assay Gate |
| **For what** | Evidence-based **release** decision—strict question, separate from Review in [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md). |
| **Why** | Keeps “looks good” separate from “releasable under policy.” |
| **Primary decision question** | Is this candidate releasable now—with defined evidence—yes or no? |
| **Trigger / cadence** | When release candidate + evidence package exist (often same week as Review). |
| **Suggested timebox** | ≤ 30 min. |
| **Allowed delivery modes** | All three for pre-checks; **pass/fail** and exceptions are **human** (Governance + Product + Engineering per prescriptive doc). |
| **Required participants** | Governance (**R**), Product (**R**), Engineering (**R**). |
| **Human owner** | Governance (policy bar); Product (user/value risk); Engineering (technical truth). |
| **Versona owner/support** | Compliance/security Versonas may pre-audit; output feeds humans. |
| **Required inputs** | Tests, acceptance, risk checks, performance as configured, Ember Log, rollback/support readiness. |
| **Recommended pre-work** | Evidence index complete; gaps explicit. |
| **Agenda / flow** | Evidence walkthrough → gap decision → pass/fail with remediations → release notes handoff. |
| **Created or updated** | Release decision; release notes draft; Ember Log for risk acceptance. |
| **Decisions expected** | Ship, hold, or ship with explicit conditions. |
| **Exit criteria** | Unambiguous outcome; owners for follow-up Sparks if any. |
| **Anti-patterns** | “Ship anyway”; Assay as second demo; rubber-stamping Versona text. |
| **What must never happen** | **Versona-only** “release approval” with no human sign-off on accountability. |

### 5.6 Retrospective

| Field | Detail |
|-------|--------|
| **Name** | Retrospective |
| **For what** | Improve the **system of work**: metrics, Ember Log, Versona effectiveness, experiments. |
| **Why** | Without it, friction repeats; learning does not become Ore. |
| **Primary decision question** | What will we **experiment** with next iteration—and who owns it? |
| **Trigger / cadence** | End of iteration; ≤ 1 h. |
| **Suggested timebox** | ≤ 1 h. |
| **Allowed delivery modes** | All three; themes may be Versona-synthesized; **committed experiments** need human owners. |
| **Required participants** | All hats (**R**). |
| **Human owner** | Rotating facilitator; Governance ensures follow-through to directives when needed. |
| **Versona owner/support** | May cluster themes from logs; does not replace psychological safety and ownership. |
| **Required inputs** | Iteration metrics, Ember Log, Versona trends, team experience. |
| **Recommended pre-work** | Data pulled; anonymized themes optional. |
| **Agenda / flow** | Metrics → Ember Log → Versona value/noise → insights → 1–3 experiments with owners/dates → new Ore where useful. |
| **Created or updated** | Experiments; new Ore; optional directive updates (see retro section in [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md)). |
| **Decisions expected** | Which experiments; what to log as debt. |
| **Exit criteria** | At least one owned experiment or explicit “no change” with rationale. |
| **Anti-patterns** | Blame; infinite venting; items with no owner. |
| **What must never happen** | Retro outcomes that never connect to Ember Log or directives when process change is claimed. |

### 5.7 Ad hoc decision meeting

| Field | Detail |
|-------|--------|
| **Name** | Ad hoc decision meeting |
| **For what** | Resolve **one** contested decision under pressure (scope fork, architecture choice, incident response, policy exception). |
| **Why** | Prevents gridlock without inventing a standing committee. |
| **Primary decision question** | What do we decide now—with owners and log entry—and what is explicitly deferred? |
| **Trigger / cadence** | Only when **real decision pressure** exists. |
| **Suggested timebox** | 30–90 min (single topic). |
| **Allowed delivery modes** | All three; Versona may branch-analysis; **decision** human. |
| **Required participants** | Minimum: accountable hat owners + affected implementers; Challenge/Governance as needed. |
| **Human owner** | Named domain owner (in invite). |
| **Versona owner/support** | Scenario analysis; draft ADR text. |
| **Required inputs** | Problem statement, options, constraints, blast radius; links to Ore/Ingot/Spark when applicable. |
| **Recommended pre-work** | One-pager or Versona digest **before** the meeting. |
| **Agenda / flow** | Frame → options → criteria → decision → Ember Log → actions. |
| **Created or updated** | Ember Log; ADR; Spark updates. |
| **Decisions expected** | One primary decision or explicit escalation path. |
| **Exit criteria** | Logged outcome with owners; no vague “later” without trigger date. |
| **Anti-patterns** | Standing weekly “decision meeting”; revisiting with no new information. |
| **What must never happen** | Replacing Refinement, Planning, or Retro with perpetual ad hoc chaos. |

---

## 6. Decisions kept (accountability)

| Decision type | Minimum human sign-off |
|---------------|-------------------------|
| Ore → Ingot promotion / Bank / reject | Product + Engineering (Challenge engaged at risk) |
| Iteration scope & Spark commitment | Product + Engineering; Governance when policy-bound |
| Banking / major priority shift | Product (with Engineering per team policy) |
| Assay pass / fail / ship with conditions | Governance + Product + Engineering |
| Risk acceptance / policy exception | Governance + domain owner; **Ember Log** |
| Retro experiments | Named human owners; directive changes per governance |

**Versona-only** tracks may **prepare and recommend**; they do not **own** these accountabilities.

---

## 7. Drift signals

| Drift | Symptom |
|-------|---------|
| Planning eats Refinement | Ingots vague; mid-week scope churn. |
| Daily sync becomes mini-planning | 15m → 45m; Charge thrashes daily. |
| Review ≡ Assay | Ship without evidence-package discipline. |
| Versona-only substitute for accountability | Log shows “AI approved” with no human owner. |
| Charge as object model | Meetings nested under Charge instead of confirming Charge at sync. |

---

## 8. Inconsistencies to resolve locally

| Topic | Tension | Resolution |
|-------|---------|------------|
| Versona sessions vs meetings | [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md): Versona sessions are not a *substitute* for team meetings | Treat **delivery mode** as how the *same* meeting type is run; raw `forge-logs/versona/` work without a meeting record is still not a team meeting. |
| Review vs Assay same day | Convenience vs strict separation | Same *day* allowed; **distinct decision questions** and minutes. |
| Daily sync + Versona-only | Weak fit for team event | Prefer hybrid; Versona supports, does not chair. |

---

## 9. Open questions (tailor per team)

1. Governance **always** in Planning/Assay vs on-call async sign-off?  
2. Combined Review + Assay time block: when is evidence maturity high enough?  
3. 2-week iterations: scale timeboxes linearly or keep caps?  
4. Minimum stakeholder attendance at Review for internal increments?  
5. Regulated contexts: does Assay require specific Versona §5 outputs in the evidence package every time, or only per work type?

---

## Related

- [Ceremonies (prescriptive)](ceremonies-prescriptive.md) · [Naming reference](NAMING-REFERENCE.md) · [Foundation connection](foundation-connection.md) · [Forge ceremonies fork](../ceremonies/forge.md)
