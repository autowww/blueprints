---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Customer Success — body of knowledge

This document describes **Customer Success** as a discipline: helping customers achieve outcomes with the product, sustaining engagement, and reducing preventable churn — through onboarding, health intelligence, support and self-service, feedback systems, retention plays, expansion, and structured success planning.

**How CS relates to PDLC and SDLC:** CS is **PDLC-heavy** after initial launch (especially **P4–P6**) and relies on **SDLC** for scalable product and platform capabilities. See [**CS-SDLC-PDLC-BRIDGE.md**](CS-SDLC-PDLC-BRIDGE.md).

**Practice topics:** See [**practices/README.md**](practices/README.md).

---

## 1. Customer success principles

| Principle | What it means | Practical signals |
|-----------|---------------|-------------------|
| **Proactive vs. reactive** | Anticipate failure modes (low usage, missed milestones, support patterns) and intervene before renewal or churn events — while still excelling at reactive resolution. | Leading indicators on dashboards; playbooks triggered before SLA breach; QBRs used for steering, not only firefighting. |
| **Customer-centric** | Optimize for **customer outcomes** (their business results, jobs-to-be-done), not only internal metrics — without confusing "the customer" with "the loudest stakeholder." | Success definitions co-authored with customers; segmentation by use case; PM/CS alignment on "definition of value delivered." |
| **Data-driven** | Decisions on coverage, risk prioritization, and product investments use **operational and experiential data**, with explicit uncertainty and bias checks. | Health score lineage documented; experiment readouts for retention initiatives; qualitative + quantitative triangulation. |
| **Cross-functional** | CS is an **orchestration layer** across product, engineering, sales, marketing, finance (billing), and support — not a silo that "owns satisfaction." | Shared account strategy; clear RACI for escalations; product reviews fed by VoC pipelines. |
| **Outcome-focused** | Activities tie to **observable outcomes** (adoption of capabilities linked to value hypotheses, renewal likelihood, expansion readiness) rather than vanity touchpoints. | Success plans with measurable milestones; onboarding completion tied to activation metrics; support deflection tied to root-cause reduction. |

---

## 2. Onboarding

**Goal:** compress **time-to-value (TTV)** — the elapsed time from contract or signup to **first meaningful outcome** (activation), then to **habitual use** of capabilities that matter.

### Time-to-value optimization

| Lever | Description |
|-------|-------------|
| **Clarify the "first success"** | Define, per segment, the smallest end-state that proves value (e.g. first report shipped, first integration live, first workflow automated). |
| **Remove sequential bottlenecks** | Parallelize setup tasks; pre-provision where safe; default sensible configurations. |
| **Instrument the journey** | Funnel metrics from signup → key events → milestone completion; identify drop-off steps with product analytics. |
| **Align human effort** | High-touch CSM steps only where marginal value is high; digital-led onboarding for long tail. |

### Guided setup patterns

| Pattern | Use when |
|---------|----------|
| **Checklist with persistence** | Users return across sessions; tasks have clear done criteria. |
| **Wizard / stepper** | Strict dependencies between steps; compliance or technical ordering matters. |
| **Empty-state CTAs** | User lands in a shell; next actions are contextual to role and tenant state. |
| **Sandbox / sample data** | Abstract product; users need safe exploration before production configuration. |
| **Concierge onboarding** | Enterprise complexity; stakeholder map; security reviews; mutual success plan. |

### Progressive disclosure

Reveal complexity **as needed**: start with defaults and happy path; expose advanced configuration, edge cases, and administrative tools after core activation. Reduces cognitive load and support tickets from premature options.

### Onboarding segmentation by persona

| Dimension | Why it matters |
|-----------|----------------|
| **Role** | Admin vs. end user vs. executive sponsor — different tasks, messaging, and training. |
| **Maturity** | Digital natives vs. regulated or change-averse organizations — different change management. |
| **Commercial context** | Land vs. expand; trial vs. paid; self-serve vs. enterprise — different success criteria and touch intensity. |
| **Use case** | Same product, different jobs-to-be-done — different milestones and help content. |

### Success milestones

Milestones are **binary, observable checkpoints** (e.g. "SSO configured," "first API call with production key," "team invited and active"). Each should map to:

- **Owner** (customer, partner, internal)
- **Evidence** (system event, attestation, or artifact)
- **Target date** (where applicable)
- **Risk flag** if missed (feeds health model)

### Onboarding completion metrics

| Metric class | Examples |
|--------------|----------|
| **Activation rate** | % reaching first success in T days |
| **Time to activate** | Median / P90 elapsed time to milestone |
| **Step completion** | Funnel conversion per onboarding step |
| **Human-assisted ratio** | Hours of CSM / PS per onboarded account (cost-to-serve) |
| **Early support volume** | Tickets in first 30/60/90 days tied to onboarding topics |

---

## 3. Customer health scoring

**Purpose:** prioritize attention, **standardize risk conversation** across CS/sales/product leadership, and trigger **playbooks** — not to replace human judgment.

### Health score components

| Component | Typical signals | Caveats |
|-----------|-----------------|--------|
| **Engagement** | Login frequency, depth/breadth of usage, feature adoption tied to value hypotheses | Can be high while outcomes stall (busywork); normalize by role and expected usage pattern. |
| **Adoption** | Activation milestones, integration health, seat utilization, workflow penetration | Distinguish "installed" from "used in production." |
| **Support** | Ticket volume, severity trends, reopen rate, time-to-resolution vs. SLA | Product bugs vs. training gaps require different responses — tag root cause. |
| **Sentiment** | CSAT after interactions, executive relationship notes, qualitative risk flags | Small-N bias; combine with behavioral data. |
| **NPS / advocacy** | Relationship-level or in-product NPS where program design supports it | Lagging; volatile in small samples; not a sole health driver. |

### Scoring models

| Model | Strengths | Risks |
|-------|-----------|-------|
| **Rule-based (weighted dimensions)** | Explainable; easy to govern; good MVP | Weights can become political; brittle across segments |
| **Segmented rules** | Aligns thresholds by customer class | Maintenance overhead |
| **Supervised ML (churn / expansion propensity)** | Captures nonlinear interactions | Explainability and drift management required; needs labeled outcomes |
| **Hybrid** | Rules for governance + ML for prioritization | Requires clear arbitration when signals conflict |

### Risk tiers

| Tier | Typical intent |
|------|----------------|
| **Healthy** | Standard cadence; digital engagement; identify expansion signals |
| **Watch** | Increased monitoring; targeted outreach; product/training interventions |
| **At-risk** | Executive alignment; success plan reset; commercial and technical remedies |
| **Critical** | Escalation path; rescue playbook; renewal decision brought forward |

### Automated alerts

- **Routing:** owner (CSM, pooled digital CS, support lead) by segment and severity.
- **Deduplication:** avoid alert storms from correlated signals (e.g. outage + ticket spike).
- **Closed-loop:** alert → action → outcome logged; measure precision/recall of alerts over time.

---

## 4. Support operations

### Tiered support model (L1 / L2 / L3)

| Tier | Scope (typical) |
|------|-----------------|
| **L1** | Triage, known issues, account admin, how-to, routing — **breadth** |
| **L2** | Deeper troubleshooting, configuration, bug characterization, workaround design — **depth** |
| **L3** | Engineering-engaged diagnosis, patches, root-cause analysis — **specialist** |

Clear **escalation criteria** (severity, customer tier, security, data loss risk) prevent both **escalation spam** and **stuck tickets**.

### SLA definition and measurement

| Element | Guidance |
|---------|----------|
| **Response vs. resolution** | Separate commitments; resolution often depends on customer responsiveness. |
| **Business hours vs. 24/7** | Match contract and incident class; avoid implicit promises from marketing copy. |
| **Severity matrix** | Impact × urgency; maps to targets and escalation clocks. |
| **Measurement** | Ticket timestamps, pause reasons, customer-visible vs. internal clocks; audit for gaming. |

### Ticket management workflows

Consistent **taxonomy** (category, product area, root cause, customer segment), **definition of done**, and **linkage to product backlog** for recurring themes.

### Knowledge base architecture

| Practice | Rationale |
|----------|-----------|
| **Search-first IA** | Users start with symptoms; structure around tasks and errors. |
| **Single source of truth** | Avoid duplicate articles across portals; version with product releases. |
| **Article quality loop** | Deflection rate, linked ticket reduction, and CSAT on articles. |

### Chatbot and AI support

Use for **deflection** and **triage** when grounded in **curated content** and **safe escalation** paths. Guardrails: hallucination risk, PII handling, audit logs, handoff to human with context.

### Community-driven support

Forums, user groups, and champions reduce load and increase peer learning — require **moderation**, **official staff presence**, and **integration** with product docs so answers stay current.

---

## 5. Self-service

### Help center design

- Task-based navigation, strong search, and consistent terminology with the product UI.
- Role-based collections (admin, developer, end user).
- Clear **status** for incidents and deprecations.

### In-app guidance

| Mechanism | Best for |
|-----------|----------|
| **Tooltips** | Field-level ambiguity; low intrusion |
| **Walkthroughs / tours** | First-run and new feature launches |
| **Contextual help** | Deep screens where docs map 1:1 to UI location |
| **Inline validation** | Prevent misconfiguration before save |

### FAQ management

Cull stale entries; tie FAQs to **top ticket drivers**; measure whether FAQ views precede ticket reduction.

### Video tutorials

Effective for procedural tasks; maintain **captions** and **versioning** alongside releases.

### Developer documentation as support

For API/SDK products, **reference docs, guides, OpenAPI quality, error catalogs, and status pages** are primary CS surfaces — invest in discoverability and examples to reduce integration churn.

---

## 6. Feedback loops

### NPS / CSAT / CES methodology (overview)

| Metric | What it measures | Notes |
|--------|------------------|-------|
| **NPS** | Loyalty / referral propensity (relationship or transactional) | Useful for trend and segment comparison; not a diagnostic tool alone. |
| **CSAT** | Satisfaction with an interaction or episode | Sensitive to recency; good for support and onboarding milestones. |
| **CES** | Effort to get an issue resolved or a job done | Predicts disloyalty in many B2B/B2C contexts; strong for friction hunting. |

### Survey design and timing

- **Sample** to avoid fatigue; stratify by segment for fairness.
- **Trigger** surveys on meaningful events (resolution, milestone, renewal window) — not random noise.
- **Close the loop:** acknowledge feedback when promised; route detractors to owners.

### Feature request management

Single **intake** channel; transparent **status** (under consideration, planned, shipped, won't do with rationale); link requests to **themes** to avoid one-off prioritization chaos.

### Voice of customer (VoC) programs

Regular synthesis (win/loss, QBR notes, advisory boards, community, support taxonomy) into **themed insights** for product and GTM — with **evidence depth** cited.

### Closing the feedback loop

Customers who take time to respond should see **visible action** or **honest explanation**. This increases future response quality and trust.

---

## 7. Churn prevention

### Early warning signals

Behavioral (usage cliffs, failed jobs, admin churn), commercial (invoice issues, downgrades), relational (sponsor departure), support (repeat P1s), and **competitive intelligence** (evaluation keywords in tickets).

### Intervention playbooks by risk tier

| Tier | Example plays |
|------|----------------|
| **Watch** | Targeted education, office hours, health check-in, fix known friction |
| **At-risk** | Success plan reset, executive business review, roadmap alignment, commercial flexibility |
| **Critical** | War room, named engineering/product sponsor, migration support if competitor threat |

### Save offers

Discounts, term adjustments, scoped professional services, or feature prioritization — **governed** with finance/legal so saves do not destroy unit economics or train adversarial negotiation.

### Win-back campaigns

Time-bound outreach, clear product delta since departure, and **learning objective** (why they left, what would win them back).

### Exit interviews

Structured for **root cause coding**; share aggregates with product, pricing, and CS leadership — protect customer confidentiality.

### Involuntary churn prevention (failed payments)

Dunning sequences, payment method update UX, account notifications, grace periods, and **finance operations** alignment — often the fastest "retention" win when conflated with voluntary churn in raw churn rates.

---

## 8. Expansion and advocacy

### Upsell / cross-sell triggers

Health **and** opportunity signals: unused entitlements, new use cases, seat growth, integration breadth, organizational expansion, positive outcomes documented in QBRs.

### Account growth strategies

Land-and-expand motion, **mutual success plans** tied to business cases, partner co-sell where applicable, and **usage-based** packaging aligned to value.

### Customer advisory boards (CABs)

Representative customers; strategic themes; safe harbor for preview feedback; clear **no-commitment** framing on roadmap items.

### Referral programs

Align incentives; track quality of referred leads; avoid conflict with partner channels.

### Case studies and testimonials

Pair CS and marketing; **evidence-backed** narratives (metrics, quotes, named logos with approval).

### Community champions

Recognize power users; early access; direct lines to product; **code of conduct** and moderation.

---

## 9. Success planning

### QBRs (Quarterly Business Reviews)

Structured executive sessions: **outcomes achieved**, roadmap alignment, risks, opportunities, and **mutual commitments**. Not a status slideshow — a decision forum.

### Success plans

Living artifact: goals, milestones, owners, metrics, risks, and agreed plays — linked to CRM/CS platform where used.

### Outcome tracking

Connect product telemetry and business KPIs the customer cares about; revisit assumptions each quarter.

### Renewal management

Start **early** (often 90+ days for enterprise); align CS, finance, and legal; separate **value narrative** from **transaction mechanics**.

---

## 10. Competencies table

| Competency | Description |
|------------|-------------|
| **Outcome framing** | Translates product capabilities into customer goals, milestones, and measurable success criteria. |
| **Segmentation and prioritization** | Applies coverage models, tiering, and economic logic to finite CS capacity. |
| **Data literacy** | Reads funnels, health models, and experiment results; collaborates with data science on features and validation. |
| **Support and operations design** | Defines SLAs, workflows, knowledge architecture, and quality loops. |
| **Change management** | Drives adoption across customer stakeholders; aligns sponsors and champions. |
| **Commercial acumen** | Understands contracts, entitlements, renewals, and healthy discounting — partners with sales and finance. |
| **Influence without authority** | Orchestrates product, engineering, and GTM on behalf of customer outcomes. |
| **Communication and facilitation** | Runs QBRs, executive escalations, and difficult renewal conversations with clarity. |
| **VoC synthesis** | Aggregates qualitative and quantitative signals into actionable product feedback. |
| **Program management** | Rolls out onboarding, feedback, and retention programs with metrics and owners. |

---

## 11. External references table

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| TSIA (Technology & Services Industry Association) | https://www.tsia.com/ | Research and frameworks for service, support, and customer growth economics |
| Customer Success Association | https://www.customersuccessassociation.com/ | Community, standards, and professional development for CS practice |
| SuccessHACKER | https://successhacker.co/ | Operating model, education, and playbook-oriented CS guidance |
| Gainsight (Customer Success methodology resources) | https://www.gainsight.com/ | Widely cited CS framework patterns (e.g. outcomes, success planning) — map concepts to your tools |
| ISO/IEC 20000 (service management) | https://www.iso.org/standard/70636.html | Service management system thinking relevant to support operations |
| ITIL (service management practices) | https://www.axelos.com/best-practice-solutions/itil | Incident, problem, knowledge, and service design practices |
| Nielsen Norman Group (help and documentation UX) | https://www.nngroup.com/ | Evidence-based guidance for help systems and self-service UX |

---

*Keep project-specific customer success documentation in `docs/product/customer-success/` and support playbooks in `docs/operations/`, not in this file.*
