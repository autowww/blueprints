---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# V-Model — connection to the SDLC foundation

The V-Model pairs each development level with a corresponding test level, creating **bidirectional traceability** between what is specified and how it is verified. The blueprint's **A–F** phases still apply; the V-Model adds **formal verification structure** and **test-level pairing**.

## 1. SDLC phases A–F (how V-Model maps)

| Phase | V-Model expression | Notes |
|-------|-------------------|-------|
| **A — Shape** | Stakeholder needs analysis; concept of operations | Defines the top of the V (what acceptance tests will validate) |
| **B — Plan** | Requirements analysis + acceptance test planning | Left-side and right-side are planned **together** |
| **C — Build** | System design → detailed design → implementation | Descending left side of the V |
| **D — Verify** | Unit test → integration test → system test | Ascending right side; each level traces to its left-side counterpart |
| **E — Release** | Acceptance testing; deployment readiness | Top-right of the V; validates against stakeholder needs |
| **F — Operate & learn** | Operational validation; field feedback | Post-deployment verification; lessons for next V-cycle |

**Prescriptive rule:** Test plans for each V-level should be drafted **during** the corresponding design phase (left side), not deferred until coding is complete.

## 2. Tracking spine (mandatory link)

V-Model teams maintain the blueprint tracking spine with traceability emphasis:

| Artifact | V-Model mapping |
|----------|-----------------|
| **Intent / request** | Stakeholder need / requirement ID |
| **Spec** | Requirements spec (system-level) + design specs (subsystem/module) |
| **Plan** | Test plans per V-level; traceability matrix |
| **Tasks** | Design and implementation work packages |
| **PRs** | Implementation; link to requirement ID and test case |
| **Reviews** | Design reviews (left-side gates); test reviews (right-side gates) |
| **Release** | Acceptance evidence package; deployment authorization |

**Prescriptive rule:** Maintain a **requirements traceability matrix (RTM)** linking requirements → design → test cases → test results. This is the V-Model's primary value artifact.

## 3. Ceremony intents (C1–C6) ↔ V-Model practices

| Intent | V-Model practice | Notes |
|--------|------------------|-------|
| **C1 — Align & decide** | Requirements review; stakeholder alignment on needs and constraints | Top of the V: what must the system do? |
| **C2 — Plan the slice** | Design review; test plan review (paired) | Commit to both the design approach and the verification approach simultaneously |
| **C3 — Execute & unblock** | Development coordination; integration meetings | During implementation (bottom of V) and integration testing (ascending) |
| **C4 — Review & quality** | Test readiness review; test result review; acceptance review | Each V-level has its own quality gate |
| **C5 — Reflect & improve** | Post-phase lessons; process improvement | Often deferred to end-of-project; better teams add mid-cycle retros |
| **C6 — Knowledge share** | Traceability matrix review; design documentation handoffs | Formal handoffs between V-levels carry knowledge |

## 4. Role archetypes (blueprint hats on a V-Model team)

| V-Model role | Typical archetype emphasis | Notes |
|--------------|----------------------------|-------|
| **Systems engineer** | **Implementer** + **Quality advocate** | Owns requirements decomposition and system-level design |
| **Test manager** | **Quality advocate** + **Orchestrator** | Plans and coordinates testing across V-levels |
| **IV&V lead** | **Quality advocate** (independent) | Independent verification and validation; common in regulated contexts |
| **Development team** | **Implementer** | Implements design and unit tests |
| **Project manager** | **Orchestrator** | Schedule, resources, gate coordination |
| **Sponsor / customer** | **Sponsor proxy** + **Steer** | Accepts at top-right of V (acceptance testing) |

## 5. What V-Model adds beyond the foundation

- **Paired verification** — each design level has a corresponding test level.
- **Early test planning** — test strategy defined during design, not after code.
- **Traceability** — requirements ↔ design ↔ test ↔ result as a first-class artifact.
- **Regulated compliance** — satisfies standards that require formal V&V evidence.

## 6. Anti-patterns (prescriptive "don't")

| Anti-pattern | Fix |
|--------------|-----|
| Test plans written after coding | Draft test plans during the corresponding design phase |
| Traceability matrix maintained only at end | Update RTM as each level is completed |
| Integration testing skipped in favor of system testing | Each V-level catches different defect types; skipping levels hides issues |
| V-Model used for low-risk, small projects | Overhead may not be justified; consider Agile with V-thinking instead |

## 7. References in-repo

- [`https://forgesdlc.com/methodologies-v-model.html`](https://forgesdlc.com/methodologies-v-model.html) — methodology summary + diagram  
- [`../ceremonies/v-model.md`](../ceremonies/v-model.md) — fork table C1–C6  
- [`../../SDLC.md`](../../SDLC.md) — phases and ceremony-intent overview  
