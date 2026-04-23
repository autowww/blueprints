---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Solution Evaluation

Assesses whether the delivered solution **actually delivers the expected value** to stakeholders and the organization. This knowledge area closes the feedback loop — it connects delivery outcomes back to the business needs that justified the initiative.

**BABOK alignment:** Knowledge Area 8 (Solution Evaluation).

**Lifecycle mapping:** Primarily **PDLC P5–P6** (Grow, Mature/Sunset) with touchpoints in **SDLC E** (Verify). The most PDLC-heavy knowledge area.

---

## 1. Tasks

### 1.1 Measure solution performance

Assess the actual value delivered by the solution against the expected outcomes defined during strategy analysis and requirements specification.

| Input | Output |
|-------|--------|
| Deployed solution, success metrics (from P3), usage data | Solution performance assessment |

**What to measure:**

| Dimension | Example Metrics | Source |
|-----------|----------------|--------|
| **Functional performance** | Feature usage rates, task completion rates, error rates | Product analytics, A/B tests |
| **Business value** | Revenue impact, cost reduction, productivity improvement | Business reporting, financial data |
| **Stakeholder satisfaction** | NPS, CSAT, support ticket volume, user feedback | Surveys, support systems |
| **Requirements fulfillment** | % of requirements implemented and passing acceptance tests | Traceability matrix, test results |
| **Operational performance** | Availability, response time, incident frequency | Monitoring systems |

**PDLC connection:** Maps directly to **P5 Grow** — the metrics dashboard and outcome measurement defined in [`PDLC.md`](../../../../pdlc/PDLC.md) §5. BA adds rigor by tracing metrics back to specific requirements and business objectives.

### 1.2 Analyze performance measures

When gaps exist between expected and actual performance, investigate root causes.

| Input | Output |
|-------|--------|
| Performance assessment, expected outcomes | Root cause analysis, performance gap identification |

**Common root cause categories:**

| Category | Examples |
|----------|----------|
| **Requirements gap** | Missing requirements, misunderstood business rules, incomplete edge case coverage |
| **Implementation gap** | Requirement correctly specified but incorrectly implemented |
| **Adoption gap** | Solution works correctly but users do not adopt it (UX, training, change management) |
| **Environment gap** | Solution works in test but not in production (data volume, integration, infrastructure) |
| **Market gap** | Requirements were valid at specification time but market/needs changed |

### 1.3 Assess solution limitations

Document constraints and limitations that prevent the solution from delivering its full expected value.

| Input | Output |
|-------|--------|
| Performance analysis, stakeholder feedback, operational data | Solution limitation assessment |

**Limitation types:**
- **Functional limitations** — capabilities the solution lacks or performs inadequately
- **Non-functional limitations** — quality attributes not meeting expectations (performance, scalability, usability)
- **Integration limitations** — gaps in connectivity with other systems
- **Organizational limitations** — processes, skills, or policies that constrain solution value
- **Technical debt** — implementation shortcuts that limit future capability

### 1.4 Assess enterprise limitations

Identify organizational barriers that prevent the solution from delivering its full value — barriers that exist **outside** the solution itself.

| Input | Output |
|-------|--------|
| Solution limitation assessment, organizational context | Enterprise limitation assessment |

**Enterprise limitation examples:**
- Organizational processes not adapted to use the new solution effectively
- Training or skill gaps in the user population
- Data quality issues in upstream systems
- Governance or compliance constraints that limit feature utilization
- Cultural resistance to workflow changes required by the solution

**PDLC connection:** Maps to **P6 Mature/Sunset** — enterprise limitations often determine whether a product can be improved further or should be retired.

### 1.5 Recommend actions

Based on the performance and limitation assessments, recommend a course of action.

| Input | Output |
|-------|--------|
| Performance assessment, limitation assessments, organizational strategy | Action recommendation |

**Recommendation options:**

| Recommendation | When to Apply |
|----------------|---------------|
| **Do nothing** | Performance is acceptable; limitations are minor; cost of change exceeds benefit |
| **Improve** | Performance gaps have identifiable solutions; investment is justified by expected value recovery |
| **Replace** | Fundamental limitations make improvement impractical; better alternatives exist |
| **Retire** | Solution no longer delivers sufficient value; maintenance cost exceeds benefit; market has moved on |

**PDLC connection:** These recommendations feed PDLC stage gate **G5** (continue investing?) and the P6 lifecycle assessment. They may trigger a new cycle back to P1 (new opportunity) or a sunset plan.

---

## 2. Techniques commonly used

| Technique | Usage in This Knowledge Area |
|-----------|------------------------------|
| Metrics and KPIs | Define and measure solution performance (§1.1) |
| Root cause analysis | Investigate performance gaps (§1.2) |
| Gap analysis | Compare actual vs expected outcomes (§1.2) |
| SWOT analysis | Assess solution position relative to alternatives (§1.3) |
| Decision analysis | Evaluate action options (do nothing, improve, replace, retire) (§1.5) |
| Benchmarking | Compare solution performance against industry standards (§1.1) |
| Surveys and questionnaires | Gather stakeholder satisfaction data (§1.1) |
| Data mining / analytics | Analyze usage patterns and performance trends (§1.1, §1.2) |
| Lessons learned | Capture insights for future initiatives (§1.5) |
| Cost-benefit analysis | Quantify improvement vs replacement vs retirement trade-offs (§1.5) |
| Risk analysis | Assess risks of each recommended action (§1.5) |

Full technique catalog: [`techniques/README.md`](../techniques/README.md).

---

## 3. Relationship to PDLC and SDLC

| Solution Evaluation Task | PDLC Mapping | SDLC Mapping |
|--------------------------|--------------|--------------|
| Measure solution performance | P5 Grow: outcome measurement, metrics dashboards | E (Verify): acceptance test results, deployment validation |
| Analyze performance measures | P5: root cause analysis of outcome gaps | — (post-delivery) |
| Assess solution limitations | P5–P6: understanding what limits growth | — (post-delivery) |
| Assess enterprise limitations | P6: organizational barriers to continued value | — (post-delivery) |
| Recommend actions | P5/G5: invest, pivot, or sunset decision; P6: retirement planning | — (may trigger new SDLC cycle) |

### Closing the loop

Solution Evaluation is the knowledge area that **closes the lifecycle loop**:

```blueprint-diagram
key: linear
alt: Diagram
```

Without Solution Evaluation, organizations build and ship but never measure whether the solution satisfied the original business need. This is the **"launch and forget"** anti-pattern identified in [`PDLC-SDLC-BRIDGE.md`](../../../../pdlc/PDLC-SDLC-BRIDGE.md) §8.
