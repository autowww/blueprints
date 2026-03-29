# Marketing

Reusable, **project-agnostic** blueprint for **Marketing** — the discipline of acquiring, engaging, and retaining users for digital products through positioning, channels, growth systems, and measurable go-to-market execution.

Marketing answers **"how do we acquire, engage, and retain users?"** — a question that is **PDLC-heavy** (especially P3 Plan & Commit, P4 Launch, P5 Grow) and depends on **SDLC** for instrumentation, SEO implementation, and experiment infrastructure.

| Document | Purpose |
|----------|---------|
| [**MARKETING.md**](MARKETING.md) | Principles, digital channels, growth engineering, positioning, analytics, GTM, content, pricing, competencies, references |
| [**MKT-SDLC-PDLC-BRIDGE.md**](MKT-SDLC-PDLC-BRIDGE.md) | How Marketing maps across SDLC phases A–F and PDLC phases P1–P6 — emphasis on P3–P5 and Build/Frontend/DevOps touchpoints |
| [**channels/**](channels/README.md) | Index for channel-specific guides (SEO, SEM, content, email, social, referral/affiliate, developer relations) |
| [**growth/**](growth/README.md) | Index for growth engineering guides (funnel optimization, A/B infrastructure, referrals, retention, activation) |

## Relationship to other packages

| Package | How Marketing relates |
|---------|------------------------|
| [`blueprints/pdlc/`](../../../pdlc/README.md) | **Lifecycle context** — P3 positioning and GTM strategy; P4 launch, comms, and channel readiness; P5 growth loops, retention, and monetization experiments. |
| [`blueprints/sdlc/`](../../../sdlc/README.md) | **Build** implements analytics events and consent; **Frontend** ships SEO, structured data, and landing experiences; **Verify** can include marketing-site and tracking QA. |
| [`blueprints/disciplines/product/ux-design/`](../ux-design/README.md) | UX shapes what Marketing promotes — messaging must match the actual product experience; onboarding and activation are a shared funnel. |
| [`blueprints/disciplines/product/ba/`](../ba/README.md) | BA clarifies stakeholder and market needs; value propositions and ICP definitions should align with requirements and capability language. |
| [`blueprints/disciplines/data/data-science/`](../../data/data-science/README.md) | Segmentation, propensity models, uplift measurement, and attribution analysis depend on data science and analytics engineering. |
| [`blueprints/disciplines/engineering/frontend/`](../../engineering/frontend/README.md) | Technical SEO, Core Web Vitals, SSR/SSG choices, and tag manager / analytics integration are Frontend concerns with Marketing requirements. |
| [`blueprints/disciplines/engineering/devops/`](../../engineering/devops/README.md) | Feature flags, experiment assignment services, and reliable event pipelines often need DevOps and platform patterns at scale. |
| [`blueprints/disciplines/security/`](../../security/README.md) | **Constrains** data collection, cookies, identity resolution, and third-party scripts — Marketing must design for privacy-by-design and least privilege. |
| [`blueprints/disciplines/security/compliance/`](../../security/compliance/README.md) | GDPR, ePrivacy, CAN-SPAM, CASL, and sector rules govern consent, email, and profiling — GTM and martech must be compliant by design. |
| [`blueprints/BRIDGES.md`](../../../BRIDGES.md) | Index of discipline ↔ SDLC ↔ PDLC bridge documents across the blueprint set. |

## Scope

This package covers **Marketing as a discipline** for digital products — not a single channel checklist. It includes:

- **Strategic foundations** — product–market fit as a prerequisite, segmentation–targeting–positioning (STP), funnel thinking (e.g. AARRR), product-led vs sales-led motion
- **Digital channels** — organic and paid acquisition, content, email, social, referrals, ASO — with metrics and fit
- **Growth engineering** — experimentation, funnel optimization, retention and cohort analysis, referral and viral mechanics
- **Positioning and messaging** — canvases, value propositions, competitive framing, hierarchy, brand voice
- **Analytics and attribution** — stack design, models, UTM discipline, conversion tracking, marketing mix modeling (MMM)
- **Go-to-market execution** — launches, betas, PR/analyst relations, community
- **Content and developer relations** — pillars, editorial rhythm, docs-as-marketing, DevRel as a channel
- **Pricing and packaging** — models, psychology, tiers, and monetization experiments

Reference bodies of knowledge: **AMA** (American Marketing Association) professional standards; **CIM** (Chartered Institute of Marketing) frameworks; **Google** Digital Marketing & Analytics courses; **HubSpot Academy** (inbound, email, CRM-aligned marketing); **Reforge** Growth Series (retention, monetization, growth loops).

---

*Keep project-specific marketing plans in `docs/product/marketing/` and GTM documents in `docs/product/`, not in this file.*
