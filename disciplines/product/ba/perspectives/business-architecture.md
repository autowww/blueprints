---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Business Architecture perspective

How business analysis adapts when the initiative is **enterprise-scale** — spanning multiple products, business units, or organizational capabilities. Business Architecture provides the strategic lens that connects individual product/project BA work to the broader organizational context.

**BABOK alignment:** BABOK v3 Business Architecture perspective.

**Related blueprints:** [`blueprints/pdlc/PDLC.md`](../../../../pdlc/PDLC.md) (product lifecycle at portfolio level) · [`blueprints/sdlc/methodologies/safe.md`](../../../../sdlc/methodologies/safe.md) (scaled agile).

---

## 1. How Business Architecture changes the BA focus

| Project-Level BA Focus | Enterprise BA Focus |
|-----------------------|---------------------|
| Solution requirements for one product | Capability requirements across the organization |
| Single stakeholder group | Cross-functional, cross-business-unit stakeholders |
| Project scope definition | Portfolio-level investment prioritization |
| Feature-level traceability | Capability-level traceability to business strategy |
| Solution evaluation for one product | Cross-portfolio value assessment |

---

## 2. Knowledge area shifts

| Knowledge Area | Business Architecture Adaptation |
|----------------|----------------------------------|
| **BA Planning & Monitoring** | Plan BA at the enterprise level — who owns which capability domain, what governance structure coordinates cross-product requirements. |
| **Strategy Analysis** | Current state is the enterprise capability map. Future state is the target operating model. Change strategy is the transformation roadmap. |
| **Elicitation & Collaboration** | Stakeholders include executive leadership, business unit heads, enterprise architects. Elicitation focuses on strategic intent and organizational constraints. |
| **Requirements Life Cycle Management** | Requirements are managed across a portfolio — traceability links capabilities to strategic objectives, multiple products, and organizational KPIs. |
| **Requirements Analysis & Design Definition** | Models include capability maps, value stream maps, organizational models, and information architecture — not just system-level models. |
| **Solution Evaluation** | Evaluation at the capability level — does the portfolio of solutions collectively deliver strategic objectives? |

---

## 3. Business Architecture concepts

### 3.1 Capability mapping

A **capability** is something the organization does (or needs to do) to achieve its objectives — independent of how it is implemented.

| Level | Example | BA Activity |
|-------|---------|-------------|
| **Level 0** | The enterprise itself | Strategic context |
| **Level 1** | Major business capabilities (e.g., "Customer Management", "Product Delivery", "Financial Reporting") | Strategy analysis — current state assessment |
| **Level 2** | Sub-capabilities (e.g., "Customer Onboarding", "Order Fulfillment") | Gap analysis — where are capability deficiencies? |
| **Level 3** | Detailed capabilities (e.g., "Identity Verification", "Shipping Label Generation") | Requirements analysis — what solutions must these capabilities provide? |

**Usage:** Capability maps provide the **structure** for organizing strategy analysis across the enterprise. They connect business strategy (why) to solution requirements (what) to delivery (how).

### 3.2 Value stream mapping

A **value stream** traces the flow of value from a triggering event to the delivery of value to a stakeholder.

| Element | Description |
|---------|-------------|
| **Trigger** | Event that starts the value stream (customer request, market signal, regulatory change) |
| **Stages** | Sequential steps that add value (intake, processing, delivery, support) |
| **Participants** | Business units, roles, systems involved at each stage |
| **Value delivered** | The outcome the stakeholder receives |
| **Pain points** | Bottlenecks, waste, quality issues at each stage |

**BA usage:** Value stream analysis identifies **where** BA effort should focus — stages with the most pain points or the greatest gap between current and desired performance.

### 3.3 Organizational modeling

| Model | Purpose |
|-------|---------|
| **Organization chart** | Formal reporting structure — identifies decision-making authority |
| **RACI matrix** (enterprise-level) | Clarifies accountability across business units for shared capabilities |
| **Stakeholder map** | Influence/interest matrix for enterprise-level change initiatives |
| **Operating model** | How the organization delivers value — coordination, standardization, diversification |

---

## 4. Business Architecture techniques

| Technique | Enterprise BA Usage |
|-----------|---------------------|
| **Capability mapping** | Define current and target enterprise capabilities; identify gaps |
| **Value stream mapping** | Analyze end-to-end value delivery; identify optimization opportunities |
| **Business model canvas** | Articulate the business model for the enterprise or business unit |
| **SWOT analysis** | Assess enterprise-level strategic position |
| **Portfolio analysis** | Evaluate and prioritize investments across the product portfolio |
| **Balanced scorecard** | Link strategic objectives to measurable KPIs across perspectives |
| **Enterprise data modeling** | Define enterprise-level information architecture and data ownership |
| **Heat mapping** | Visualize capability maturity, investment levels, or strategic importance |
| **Wardley mapping** | Map components by value chain position and evolution stage |
| **Target operating model** | Define the desired future organizational structure and processes |

---

## 5. Business Architecture artifacts

| Artifact | Purpose | Where It Lives |
|----------|---------|----------------|
| **Capability map** | Visual inventory of organizational capabilities | Enterprise architecture documentation (outside individual product repos) |
| **Value stream map** | End-to-end value delivery flow with pain points | Enterprise architecture or program-level documentation |
| **Strategic roadmap** | Multi-initiative transformation plan | Program/portfolio level; per-product roadmap in `docs/ROADMAP.md` |
| **Investment portfolio** | Prioritized list of capability investments | Portfolio management (outside individual repos) |
| **Enterprise stakeholder register** | Cross-initiative stakeholder analysis | Program level; per-project version using [`templates/stakeholder-register.template.md`](../templates/stakeholder-register.template.md) |

---

## 6. When to apply this perspective

| Situation | Apply Business Architecture? | Reasoning |
|-----------|------------------------------|-----------|
| Single product, single team | No — project-level BA is sufficient | Enterprise overhead not justified |
| Single product, enterprise customer base | Partially — understand customer's business architecture | Helps align product capabilities with customer organization |
| Multi-product portfolio | Yes — coordinate capabilities across products | Avoid duplication, ensure strategic alignment |
| Enterprise transformation | Yes — this is the primary lens | Cross-organizational impact requires enterprise-level analysis |
| Platform / shared services | Yes — multiple consumers depend on the platform | Capability mapping identifies all consumers and their needs |

---

## 7. Common pitfalls in enterprise BA

| Pitfall | Description | Remedy |
|---------|-------------|--------|
| **Ivory tower architecture** | Business architecture team creates models disconnected from delivery teams | Embed business architects in delivery; ensure capability maps link to product backlogs |
| **Capability sprawl** | Capability map grows to hundreds of items with no clear prioritization | Limit to 3 levels; prioritize by strategic importance and gap severity |
| **Missing delivery connection** | Strategic roadmap exists but no clear path to SDLC delivery | Use [`BA-SDLC-PDLC-BRIDGE.md`](../BA-SDLC-PDLC-BRIDGE.md) to connect enterprise strategy to product delivery |
| **Analysis without action** | Enterprise models are created, presented, and filed — no investment decisions follow | Tie capability analysis directly to portfolio investment decisions; kill models nobody acts on |
