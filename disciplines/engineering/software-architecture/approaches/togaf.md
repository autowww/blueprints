---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# TOGAF and the Architecture Development Method (ADM)

**TOGAF** (The Open Group Architecture Framework) is an **enterprise architecture** framework. Its best-known part is the **Architecture Development Method (ADM)** — a cyclic, phase-based process for developing and governing architectures across business, information systems, and technology domains. It targets **portfolio-scale** change, not a single team’s sprint backlog.

| Concept | Role |
|---------|------|
| **Enterprise continuum** | From generic foundation → common systems → industry → organization-specific |
| **ADM** | Iterative method to produce architectures and govern implementation |
| **Architecture repository** | Central store for artifacts, standards, and reusable building blocks |

---

## ADM phases (overview)

| Phase | Name | Typical focus |
|-------|------|----------------|
| **Preliminary** | Framework & principles | Scope, governance, architecture capability, tailoring TOGAF |
| **A** | Architecture vision | Stakeholders, constraints, high-level vision, approval to proceed |
| **B** | Business architecture | Business capabilities, processes, organization, motivation |
| **C** | Information systems architectures | Data + application architectures (often split into C1/C2 in practice) |
| **D** | Technology architecture | Platforms, standards, infrastructure patterns |
| **E** | Opportunities & solutions | Consolidated gap analysis, transition architectures, work packages |
| **F** | Migration planning | Roadmaps, sequencing, dependencies, business value |
| **G** | Implementation governance | Ensure projects align with architecture; waivers and compliance |
| **H** | Architecture change management | Monitor environment; trigger new ADM cycle when change warrants |
| **Requirements management** | Continuous | Cross-cutting; requirements flow through all phases |

*Note:* The Open Group publishes the authoritative phase definitions; names and emphasis may evolve with the standard edition — always check your adopted version.

---

## ADM cycle — phase dependencies (conceptual)

```blueprint-diagram
key: swimlane
alt: ADM cycle — phase dependencies (conceptual)
title: ADM cyclic phase handoffs
summary: How ADM phases pass governed artifacts forward while continuous feedback loops refine the architecture cycle.
node: ADM cycle — phase dependencies (conceptual)
detail: Entry framing how iterative ADM phases depend on one another across the cycle.
more: Phases B through H each consume prior outputs and produce inputs for downstream work; preliminary sets governance before phase A begins.
node: Lane A
detail: Primary path where each ADM phase delivers artifacts to the next.
more: Business, information systems, and technology phases (B–D) hand consolidated views into opportunities, migration planning, and implementation governance.
node: handoff
detail: Formal transfer of phase outputs into downstream architecture work.
more: Gap analysis, transition architectures, and work packages at phase E depend on artifacts from B–D before roadmaps and sequencing at F.
node: shared outcome
detail: Governed architecture baselines and roadmaps the organization can implement.
more: Phase G aligns projects to architecture; approved outputs land in the architecture repository for reuse and compliance review.
node: Lane B
detail: Parallel lane where environment change and delivery evidence reshape the cycle.
more: Cross-cutting requirements management and phase H change management monitor drift from approved baselines.
node: inspect / adapt
detail: Review implementation compliance, waivers, and environmental shifts against current architecture.
more: Phase G governance and phase H triggers detect when a new ADM iteration is warranted rather than relying on stale blueprints.
node: feedback
detail: Change requests and updated requirements loop back into a new or revised cycle.
more: Phase H explicitly monitors the environment; tailoring encourages time-boxing rather than treating ADM as a waterfall gate.
fallback_ascii: |
  ADM cycle — phase dependencies (conceptual)

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

---

## Architecture repository — typical contents

| Area | Contents |
|------|----------|
| **Metamodel** | Relationships between entities (capabilities, applications, data, technology) |
| **Reference library** | Industry templates, vendor patterns, reusable models |
| **Standards** | Approved products, versions, interfaces, coding and integration standards |
| **Governance log** | Decisions, deviations, waivers, architecture board minutes |

---

## Deliverables matrix (illustrative — tailor to your standard)

| Phase | Examples of outputs (not exhaustive) |
|-------|--------------------------------------|
| Preliminary | Architecture principles, governance model, scope statement |
| A | Stakeholder map, vision doc, statement of architecture work |
| B | Capability map, process models, organization view |
| C | Application portfolio, data entities, information flows |
| D | Technology standards catalog, platform reference model |
| E | Gap analysis, candidate roadmaps, consolidated architecture |
| F | Migration plan, transition architectures, initiative sequencing |
| G | Compliance assessments, project architecture reviews |
| H | Change requests, updated architecture cycle triggers |

Formal TOGAF lists **specific artifacts** per phase; use the standard as the source of truth when certifying or contracting.

---

## TOGAF vs lighter approaches

| Situation | TOGAF often fits | TOGAF often overkill |
|-----------|------------------|----------------------|
| **Org size / spread** | Many business units, shared platforms, central EA team | Single product team, one deployable system |
| **Regulation** | Sector mandates, audit trails for architecture decisions | Low regulatory surface |
| **Portfolio** | Application rationalization, multi-year transformation | Greenfield MVP with one codebase |
| **Maturity** | Established architecture board, funded EA function | Ad-hoc decisions + ADRs only |

Lighter substitutes for small orgs: **C4 + ADRs**, **arc42**, lean **value stream / capability** sketches, and explicit **tech radar** governance.

---

## Tailoring — minimum viable TOGAF by org scale

| Org profile | Minimum useful slice |
|-------------|----------------------|
| **Startup / small team** | Skip full ADM; borrow **principles** + **vision (A-lite)** + ADRs |
| **Scale-up / multi-team** | A + simplified B/C/D as one-page views; **G-lite** via RFCs |
| **Enterprise** | Full ADM or phased adoption; repository + board; integrate with PPM |

Tailoring is **explicitly encouraged** by TOGAF practice: adopt the method, don’t photocopy every artifact.

---

## Certification path (typical)

| Credential | Level | Notes |
|------------|-------|-------|
| **TOGAF® Enterprise Architecture Foundation** | Entry | Core concepts, ADM overview, vocabulary |
| **TOGAF® Enterprise Architecture Practitioner** | Applied | Scenarios, tailoring, ADM application |
| **TOGAF® Enterprise Architecture Certified** | Advanced | Deeper certification track per The Open Group catalog |

Exact exam names and tiers change — verify on [The Open Group certification pages](https://www.opengroup.org/certifications/togaf).

---

## Anti-patterns (in practice)

| Anti-pattern | Symptom | Better direction |
|--------------|---------|------------------|
| **ADM as waterfall gate** | Months before delivery sees architecture | Time-box phases; integrate with iterative delivery |
| **Artifact theater** | Huge templates nobody reads | Tailor outputs to decisions and risks |
| **EA ivory tower** | Blueprints ignored by teams | Co-create with product/engineering; link to ADRs and C4 |

---

## External references

- [The Open Group — TOGAF](https://www.opengroup.org/togaf) — standard, certification, overview.
- TOGAF Standard documentation (licensed/purchased per Open Group terms) — authoritative phase and content definitions.

*Keep project-specific architecture decisions in docs/adr/ and system documentation in docs/architecture/, not in this file.*
