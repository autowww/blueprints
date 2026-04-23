---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Marketing body of knowledge

This document maps the core concerns of **Marketing** for **digital products** — strategy, channels, growth systems, positioning, analytics, GTM, content, and monetization — to the blueprint ecosystem.

**How Marketing relates to PDLC and SDLC:** Marketing is **outcome- and lifecycle-driven** — strongest in P3–P5, with recurring SDLC dependencies for implementation of tracking, SEO, and experiments. See [`MKT-SDLC-PDLC-BRIDGE.md`](MKT-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Channels:** Channel deep-dives are indexed in [`channels/`](channels/README.md).

**Growth:** Growth engineering topics are indexed in [`growth/`](growth/README.md).

---

## 1. Marketing principles

| Principle | Description | Implications for digital products |
|-----------|-------------|-----------------------------------|
| **Product–market fit (PMF) prerequisite** | Sustainable acquisition and retention require that a defined segment repeatedly chooses the product and receives enough value that churn and CAC dynamics work | Premature scale wastes spend; PMF signals (retention plateaus, organic pull, NPS/PMF surveys) should precede aggressive paid growth |
| **Segmentation → Targeting → Positioning (STP)** | Divide the market into addressable segments, choose which to serve first, then occupy a clear position in the buyer’s mind | ICP (ideal customer profile) and personas inform channel mix, creative, and pricing; “everyone” is not a segment |
| **Marketing funnel** | Classic AIDA (awareness → interest → desire → action) maps to digital **AARRR** (Acquisition, Activation, Retention, Referral, Revenue) — “pirate metrics” | Teams assign owners per stage; leakage analysis drives backlog priorities across Product, Marketing, and Success |
| **Product-led growth (PLG)** | The product itself is the primary acquisition and expansion vehicle — freemium, self-serve signup, in-product upsell | Low-touch sales, strong onboarding, usage-based packaging, and in-app upgrade moments; marketing amplifies loops |
| **Sales-led growth (SLG)** | Marketing generates qualified demand; sales closes and expands — common in enterprise ACV models | Content, events, ABM, and SDR/BDR workflows; marketing focuses on pipeline and win-rate support |

### AARRR stage — typical focus

| Stage | User / business question | Typical levers |
|-------|--------------------------|----------------|
| **Acquisition** | How do users find us? | Channels, creative, landing pages, ASO, partnerships |
| **Activation** | Did they experience core value? | Onboarding, time-to-value, templates, guided setup |
| **Retention** | Do they come back / stay subscribed? | Habit loops, notifications, roadmap delivery, customer success |
| **Referral** | Do they invite others? | Referral programs, viral loops, advocacy, community |
| **Revenue** | Do we monetize fairly and durably? | Pricing, packaging, expansion triggers, payment UX |

---

## 2. Digital marketing channels

| Channel | Description | Primary metrics (examples) | Best fit |
|---------|-------------|----------------------------|----------|
| **SEO** | Earned visibility in organic search via technical health, content, authority, and intent-aligned pages | Organic sessions, impressions, CTR, keyword rankings, assisted conversions, Core Web Vitals | Durable demand, high-intent topics, products with searchable problems |
| **SEM / PPC** | Paid listings on search engines — intent capture via keywords, ads, and landing relevance | CPC, CPA, ROAS, quality score, impression share, conversion rate | High-intent categories, time-bound launches, competitive conquest (where allowed) |
| **Content marketing** | Owned media (blog, guides, video, tools) that attracts, educates, and nurtures | Engagement time, subscribers, assisted conversions, backlinks, branded search lift | Consideration-heavy buys, developer/educational audiences, thought leadership |
| **Email** | Direct, permissioned communication — newsletters, lifecycle drips, transactional triggers | Open/click (use cautiously), conversion per campaign, list growth, deliverability, unsubscribe rate | Retention, activation nudges, cross-sell, win-back (with compliance discipline) |
| **Social media** | Organic and hybrid presence on platforms where ICP spends time | Reach, engagement rate, follower quality, traffic referrals, share of voice | Brand-heavy categories, community products, visual or cultural brands |
| **Affiliate / referral** | Third-party or peer incentives to drive signups or purchases | CPA, activation rate of referred users, fraud rate, partner ROI | Consumer, prosumer, and partner-ecosystem products with clear attribution |
| **Paid social** | Sponsored posts and lead forms on social networks | CPM, CPC, CPA, creative fatigue rate, incrementality (where measured) | Awareness, retargeting, lookalike acquisition when creative + targeting iterate fast |
| **App store optimization (ASO)** | On-store discovery — metadata, creatives, ratings/reviews, localization | Impressions → product page view → install rate, category rank, review sentiment | Mobile-first products; complements paid UA |

---

## 3. Growth engineering

| Topic | Description | Practice notes |
|-------|-------------|----------------|
| **Funnel optimization** | Systematic improvement of stage conversion using data and qualitative insight | Define stages with mutually exclusive rules; watch guardrails (support volume, refund rate) |
| **A/B testing at scale** | Controlled experiments on UX, pricing presentation, messaging, and campaigns | Agree on unit of randomization (user vs session vs account); pre-register metrics; watch sample ratio mismatch |
| **Referral loops** | Product flows that encourage invites or shares | Measure viral coefficient with caution — saturation and incentive skew distort “K” |
| **Virality coefficient (K)** | Average invites × conversion per invite | Useful as a sketch; real programs need cohort-based invite modeling and de-duplication |
| **Retention curves** | % of cohort active over time (D1/D7/D30 or subscription renewal) | Compare curves after product changes; segment by channel and persona |
| **Cohort analysis** | Group users by signup period or campaign; compare behavior over time | Essential for judging channel quality beyond last-click CPA |
| **Activation optimization** | Shorten path to the “aha” moment | Instrument key events; run onboarding experiments; align with UX and Support |

---

## 4. Positioning and messaging

| Artifact / concept | Purpose |
|--------------------|---------|
| **Positioning canvas** | Clarify competitive alternatives, unique attributes, value, target segments, and category — aligns sales, product, and marketing |
| **Value proposition design** | Jobs, pains, and gains (e.g. Value Proposition Canvas) — ensures messaging maps to customer reality |
| **Competitive positioning** | Explicit map of who you replace, why switching wins, and honest differentiation (not feature laundry lists) |
| **Messaging hierarchy** | Company → product → feature messages; proof points and objections at each level |
| **Brand voice** | Tone, vocabulary, and editorial standards for consistent expression across channels and product UI |

---

## 5. Analytics and attribution

| Topic | Description |
|-------|-------------|
| **Marketing analytics stack** | Typically: event collection (product + web), warehouse, BI, experimentation, and ad platform data — integrated with identity resolution where appropriate |
| **Multi-touch attribution (MTA)** | Rules or algorithmic models assigning credit across touches (last-click, linear, time-decay, position-based, Shapley-style approximations). **Limitations:** privacy changes, cross-device gaps, correlation vs causation |
| **UTM conventions** | Standardized `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` — enforced naming so reports stay comparable |
| **Conversion tracking** | Pixels, server-side CAPI/conversions API, offline imports — prioritize durable, consent-aware methods |
| **Marketing mix modeling (MMM)** | Statistical model of channel spend vs outcomes — useful for macro budget allocation where experiments are hard |

### UTM — minimal convention (example pattern)

| Parameter | Role | Example values |
|-----------|------|----------------|
| `utm_source` | Who sent the traffic | `newsletter`, `google`, `linkedin`, `partner_acme` |
| `utm_medium` | Type of marketing | `email`, `cpc`, `organic`, `social`, `referral` |
| `utm_campaign` | Named initiative | `launch_winter_2026`, `webinar_api_security` |
| `utm_content` | Creative or variant | `hero_blue`, `sponsor_logo_link` |
| `utm_term` | Paid keyword (optional) | `project_management_software` |

---

## 6. Go-to-market execution

| Activity | Description |
|----------|-------------|
| **Launch planning** | Coordinated timeline: positioning, pricing, enablement, press/analyst, ads, email, product flags, support readiness, success criteria |
| **Beta programs** | Closed or open betas for feedback, case studies, and reference customers — with clear success metrics and feedback loops |
| **Early adopter strategy** | Target segment, incentives, success management, and feedback cadence — often overlaps with DevRel or design partners |
| **PR / analyst relations** | Narrative, proof points, briefing decks, embargoes, and measurement (share of voice, pipeline influence where tracked) |
| **Community building** | Forums, champions programs, events, and ambassador models — long-term retention and advocacy engine |

---

## 7. Content strategy

| Element | Description |
|---------|-------------|
| **Content pillars** | 3–5 recurring themes aligned to strategy — simplifies planning and SEO topical authority |
| **Editorial calendar** | Cadence, owners, formats, and funnel mapping — balances always-on and campaign spikes |
| **SEO content** | Intent-mapped pages, internal links, refresh cycles — avoids thin or duplicate content |
| **Thought leadership** | Point of view, research, and frameworks — builds trust in crowded categories |
| **Documentation as marketing** | Great docs reduce friction, improve activation, and rank for long-tail technical queries |
| **Developer relations (DevRel)** | Education, samples, and community — **credibility-first**; metrics differ from consumer social (see [`channels/README.md`](channels/README.md)) |

---

## 8. Pricing and monetization

| Model | Description | Marketing / GTM notes |
|-------|-------------|-------------------------|
| **Freemium** | Free tier with upgrade path | Clear limits, transparent upgrade value, in-product paywalls; avoid bait-and-switch perception |
| **Subscription** | Recurring fee for access | Annual vs monthly framing, expansion seats, renewal campaigns |
| **Usage-based** | Charge aligned to consumption | Predictability messaging, calculators, “shock bill” prevention in UX |
| **One-time / perpetual** | Single purchase | Often paired with maintenance or support upsell; different content and channel mix |
| **Pricing psychology** | Anchoring, decoys, charm pricing, tier naming | Test ethically; align with brand; disclose terms clearly |
| **Packaging and tiers** | Feature bundles mapped to segments | Good-better-best simplifies choice; enterprise “call us” when needed |

---

## 9. Competencies table

| Competency cluster | Capabilities |
|--------------------|--------------|
| **Strategy** | STP, positioning, competitive analysis, ICP definition, GTM motion design (PLG vs SLG) |
| **Channel execution** | SEO/SEM, paid social, email, content operations, partnerships, ASO |
| **Creative and copy** | Messaging hierarchy, storytelling, CRO for landing pages, ad creative iteration |
| **Analytics** | Funnel instrumentation, experimentation stats literacy, attribution limitations, dashboard design |
| **Marketing technology** | Tag management, CDP/CRM alignment, consent platforms, integrations with product data |
| **Growth and lifecycle** | Activation/retention experiments, referral program design, cohort interpretation |
| **Stakeholder management** | Sales enablement, exec reporting, budget defense, agency/partner governance |
| **Legal / ethical literacy** | Privacy, consent, claims substantiation, dark-pattern avoidance |

---

## 10. External references table

| Source | Focus |
|--------|--------|
| **AMA (American Marketing Association)** | Professional standards, ethics, and contemporary marketing practice |
| **CIM (Chartered Institute of Marketing)** | Strategic marketing, brand, and organizational marketing capability |
| **Google Digital Marketing & Analytics** | Ads, Analytics (GA4), measurement, and platform-specific certification paths |
| **HubSpot Academy** | Inbound marketing, email, CRM-aligned marketing operations |
| **Reforge (Growth Series)** | Retention, monetization, growth loops, and advanced growth strategy |
| **W. Chan Kim & Renée Mauborgne — *Blue Ocean Strategy*** | Creating uncontested market space; differentiation framing |
| **Al Ries & Jack Trout — *Positioning*** | Competitive mindshare and category thinking |
| **April Dunford — *Obviously Awesome*** | Practical positioning for technology products |
| **Sean Ellis — PMF / growth** | Product–market fit metrics and early-stage growth discipline |
| **Dave McClure — AARRR** | Pirate metrics framework for startup funnels |

---

*Keep project-specific marketing plans in `docs/product/marketing/` and GTM documents in `docs/product/`, not in this file.*
