---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Strategy Analysis

Defines the **business need**, understands the **current state**, envisions the **future state**, and recommends a **change strategy** and **solution scope**. This is the knowledge area most closely aligned with PDLC phases P1–P3.

**BABOK alignment:** Knowledge Area 3 (Strategy Analysis).

**Lifecycle mapping:** Primarily **PDLC P1–P3** (Discover Problem, Validate Solution, Plan & Commit). Strategy Analysis provides the analytical backbone for product discovery and investment decisions.

---

## 1. Tasks

### 1.1 Analyze current state

Document the existing situation — capabilities, processes, organizational context, pain points, constraints — as a factual baseline for change.

| Input | Output |
|-------|--------|
| Business need, organizational context | Current state description (capabilities, processes, pain points, constraints) |

**What to document:**
- Existing capabilities and their effectiveness
- Current processes and their bottlenecks
- Organizational structure and decision-making patterns
- Technology landscape and constraints
- Regulatory environment
- Existing solutions and their limitations

**PDLC connection:** This maps directly to **P1 Discover Problem** — the BA provides structured analysis of the problem space, complementing the PM's user research and market analysis.

### 1.2 Define future state

Articulate the desired outcomes — what the organization looks like after the change is successfully implemented.

| Input | Output |
|-------|--------|
| Current state description, business objectives | Future state description (desired capabilities, outcomes, success criteria) |

**Elements of future state:**
- Business goals and objectives the change will achieve
- New or improved capabilities required
- Process changes expected
- Organizational changes needed
- Metrics that will indicate success
- Constraints and assumptions

**PDLC connection:** Maps to **P1–P2** — the future state vision aligns with the product vision in `docs/product/vision/`, but from an organizational perspective rather than market perspective.

### 1.3 Assess risks

Identify threats and opportunities that could affect the change initiative's success.

| Input | Output |
|-------|--------|
| Current state, future state, organizational context | Risk assessment (identified risks, probability, impact, mitigation strategies) |

**Risk categories for BA:**
- **Requirements risk** — incomplete, ambiguous, or volatile requirements
- **Stakeholder risk** — disengaged sponsors, conflicting stakeholder needs
- **Organizational risk** — resistance to change, capability gaps, political barriers
- **Technical risk** — feasibility concerns, integration complexity (shared with SDLC)
- **External risk** — regulatory changes, market shifts, competitor moves

**Project mapping:** Risk analysis outputs feed into `docs/requirements/risks/` (the project's risk register and RBS).

### 1.4 Define change strategy

Recommend the overall approach to achieving the future state — build vs buy, phased vs big-bang, scope boundaries, transition approach.

| Input | Output |
|-------|--------|
| Current state, future state, risk assessment, organizational constraints | Change strategy (recommended approach, scope, transition plan, resource needs) |

**Change strategy elements:**
- Solution approach (build, buy, configure, outsource, or combination)
- Implementation approach (phased, big-bang, pilot, parallel)
- Scope boundaries (what is in and out for this initiative)
- Transition needs (training, data migration, process changes)
- Resource and timeline estimates
- Success criteria and measurement approach

**PDLC connection:** Maps to **P3 Plan & Commit** — the change strategy becomes the business case and investment decision for the stage gate (G3). It shapes what enters SDLC Phase A.

### 1.5 Define solution scope

Delineate the boundary of the solution — what capabilities are included, what is deferred, and what is explicitly excluded.

| Input | Output |
|-------|--------|
| Change strategy, business objectives, constraints | Solution scope (in-scope capabilities, out-of-scope items, deferred items, dependencies) |

**Scope artifacts:**
- In-scope capability list with rationale
- Out-of-scope list with rationale (prevents scope creep)
- Deferred items with conditions for future inclusion
- External dependencies and integration boundaries
- Assumptions and constraints affecting scope

**SDLC connection:** Solution scope becomes the **input to SDLC Phase A (Discover)** — it defines the boundaries of what the delivery team will build. Maps to `docs/requirements/` structure.

---

## 2. Techniques commonly used

| Technique | Usage in This Knowledge Area |
|-----------|------------------------------|
| SWOT analysis | Assess organizational strengths, weaknesses, opportunities, threats (§1.1, §1.3) |
| PESTLE analysis | Assess external factors affecting the initiative (§1.3) |
| Benchmarking | Compare current capabilities against industry standards or competitors (§1.1) |
| Root cause analysis | Understand why current state problems exist (§1.1) |
| Gap analysis | Compare current state to future state (§1.2) |
| Decision analysis | Evaluate change strategy options (§1.4) |
| Scope modeling | Define solution boundaries (§1.5) |
| Business model canvas | Articulate value proposition and business model for the change (§1.4) |
| Feasibility analysis | Assess viability of proposed change strategy (§1.4) |
| Risk analysis | Identify and assess risks to the change initiative (§1.3) |
| Document analysis | Review existing documentation, contracts, regulations (§1.1) |
| Estimation | Size the change effort and required resources (§1.4) |

Full technique catalog: [`techniques/README.md`](../techniques/README.md).

---

## 3. Relationship to PDLC and SDLC

| Strategy Analysis Task | PDLC Mapping | SDLC Mapping |
|------------------------|--------------|--------------|
| Analyze current state | P1 Discover Problem: structured analysis of the problem space | — (upstream of delivery) |
| Define future state | P1–P2: future state vision complements product vision | — (upstream of delivery) |
| Assess risks | P2–P3: risk assessment informs stage gate decisions (G1, G2, G3) | Risk register feeds into `docs/requirements/risks/` |
| Define change strategy | P3 Plan & Commit: change strategy shapes investment decision and GTM plan | — (upstream of delivery) |
| Define solution scope | P3 → SDLC handoff: scope definition creates the boundary for SDLC Phase A | Phase A receives scope as input |

### Overlap with PDLC

Strategy Analysis and PDLC P1–P3 cover similar ground from different angles:

| Concern | Strategy Analysis (BA) | PDLC P1–P3 (PM) |
|---------|------------------------|------------------|
| Problem framing | Organizational needs, process gaps, capability deficiencies | User pain points, market opportunity, competitive landscape |
| Solution direction | Change strategy, build/buy/configure decision | Product vision, solution hypothesis validation |
| Investment decision | Business case with quantified costs and benefits | Stage gate review with success metrics and resource request |
| Scope definition | Capability boundaries, integration scope, transition needs | Feature scope, MVP definition, roadmap phasing |

In practice, these activities often happen **concurrently** — the PM leads market/user analysis while the BA leads organizational/requirements analysis. Their outputs converge at the P3/G3 stage gate.
