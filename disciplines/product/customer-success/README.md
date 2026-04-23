---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Customer Success

Reusable, **project-agnostic** blueprint for **Customer Success (CS)** — the discipline of helping users and customers realize value from a product after adoption, sustaining engagement, and reducing preventable churn through proactive orchestration, support excellence, and feedback-driven improvement.

Customer Success answers **"How do we help users achieve their goals and reduce churn?"** — a question that is strongest in PDLC **P4–P6** (launch through growth, renewal, and transition) and depends on **SDLC** for the systems that scale onboarding, guidance, health telemetry, and support.

| Document | Purpose |
|----------|---------|
| [**CUSTOMER-SUCCESS.md**](CUSTOMER-SUCCESS.md) | Principles, onboarding, health scoring, support ops, self-service, feedback loops, churn prevention, expansion, success planning, competencies, references |
| [**CS-SDLC-PDLC-BRIDGE.md**](CS-SDLC-PDLC-BRIDGE.md) | How CS maps across PDLC P1–P6 and SDLC A–F — lifecycle emphasis, roles, artifacts, calibration by business model, anti-patterns |
| [**practices/**](practices/README.md) | Index of practice-guide topics (onboarding design, health scoring, support ops, feedback programs, churn playbooks) |

## Relationship to other packages

| Package | How Customer Success relates |
|---------|------------------------------|
| [**Marketing**](../marketing/README.md) | Marketing **acquires** and often **activates** demand; Customer Success **retains** and **expands** relationships. Handoffs (MQL/SQL to closed-won, launch messaging vs. onboarding truth) must align so promises match the post-sale experience. |
| [**UX / UI Design**](../ux-design/README.md) | UX makes the product **usable**; CS ensures users **adopt** capabilities that matter — through onboarding, in-product guidance, help content, and support pathways. Poor UX inflates support cost; strong CS surfaces friction signals back to product and design. |
| [**Business Analysis**](../ba/README.md) | BA clarifies **needs** and **requirements**; CS validates **outcomes in production** — whether capabilities translate to customer results. Solution evaluation and VoC feed the same evidence loop. |
| [**PDLC**](../../../pdlc/README.md) | **P4** onboarding and launch readiness; **P5** retention, expansion, and health; **P6** migration, sunset, and offboarding — CS is a primary execution lens for post-launch lifecycle management. See [**CS-SDLC-PDLC-BRIDGE.md**](CS-SDLC-PDLC-BRIDGE.md). |
| [**SDLC**](../../../sdlc/README.md) | CS depends on delivery of **support tooling** (ticketing, CRM, success platform integrations), **in-app guidance** (tooltips, tours, contextual help), and **analytics instrumentation** for health scores and funnel metrics. |
| [**Data**](../../data/README.md) / [**Data Science**](../../data/data-science/README.md) | **Health scoring**, **churn prediction**, **propensity models**, and **segmentation** require clean event data, labeled outcomes, and governed analytics. CS consumes models; data teams own feature stores and validation. |
| [**Engineering**](../../engineering/README.md) | Implements integrations, customer data pipelines, admin consoles, billing hooks, and in-product experiences that CS programs rely on at scale. |
| [**Security**](../../security/README.md) / [**Compliance**](../../security/compliance/README.md) | Customer data in CS systems (contracts, communications, surveys) must respect access control, retention, and regulatory boundaries (e.g. GDPR, sector rules). |
| [**Governance**](../../governance/README.md) | Executive sponsorship, target operating model, and cross-functional forums (e.g. QBR cadence with sales/product) align CS with company strategy. |

## Scope

This package covers **Customer Success as a discipline** — not a single tool vendor or job title. It includes:

- **Principles** — proactive vs. reactive service, customer-centricity, data-informed prioritization, cross-functional orchestration, outcome focus
- **Onboarding and time-to-value** — guided setup, progressive disclosure, persona-based journeys, milestones, completion metrics
- **Customer health** — composite scores, risk tiers, alerting, feedback between CS and product/data
- **Support operations** — tiering, SLAs, workflows, knowledge base, automation and community support models
- **Self-service** — help centers, in-app guidance, FAQs, multimedia learning, developer docs as frontline support
- **Feedback systems** — NPS, CSAT, CES, VoC, feature intake, closing the loop
- **Churn prevention and recovery** — early warning, playbooks, save offers, win-back, exit learning, payment failure handling
- **Expansion and advocacy** — growth plays within accounts, CABs, referrals, case studies, champions programs
- **Success planning** — QBRs, success plans, outcome tracking, renewal management

Reference bodies of knowledge and industry frameworks: **TSIA** (technology services research and benchmarks), **Gainsight** and similar **Customer Success platform** methodology (e.g. outcomes hierarchy, success planning patterns), **SuccessHACKER** (playbooks and operating model content), **Customer Success Association** and adjacent communities (standards of practice, competency development). Use vendor-neutral patterns here; map tools to your stack locally.

---

*Keep project-specific customer success documentation in `docs/product/customer-success/` and support playbooks in `docs/operations/`, not in this file.*
