# User onboarding design and optimization

## Overview

**Onboarding** is the bridge between **acquisition** (someone becomes a customer or trialist) and **activation** (they experience meaningful value). Poor onboarding inflates support cost, delays revenue recognition, and seeds churn. Strong onboarding aligns product guidance, human touch where it pays off, and messaging so users reach their **first value moment** quickly and form habits around capabilities that matter.

This guide is **project-agnostic**: adapt models, patterns, and metrics to your segment, motion, and data maturity.

---

## Onboarding models

| Model | Target segment | Cost per user | Time-to-value (typical) | Scalability |
|-------|----------------|---------------|-------------------------|-------------|
| **Self-serve (low-touch)** | PLG, SMB, prosumer | Low (mostly product + docs) | Fast when product is simple; slower if setup is heavy | High — automation-first |
| **Guided (mid-touch)** | SMB–mid-market, mixed PLG/sales | Medium (digital + light CSM/check-ins) | Moderate — balances speed with setup quality | Medium — cohorts and playbooks |
| **High-touch (concierge)** | Enterprise, regulated, complex integrations | High (CSM, PS, workshops) | Often longer wall-clock but higher completion for hard setups | Low — people-constrained |
| **Hybrid** | Land-and-expand, tiered plans | Variable by tier | Optimized per segment (e.g. digital + kickoff for key accounts) | High for long tail + selective human depth |

Choose the model by **setup complexity**, **contract value**, **risk** (security, compliance), and **what “activated” means** for each segment.

---

## Onboarding funnel (conceptual)

```blueprint-diagram
key: linear
alt: Diagram
```

**First value moment** is the smallest observable outcome that proves the product works for their job. **Habit formation** is repeated use of the capabilities tied to retention and expansion — not merely completing a checklist once.

---

## Onboarding patterns

| Pattern | Role in the journey | Notes |
|---------|---------------------|--------|
| **Product tours** | Orient; surface IA and primary workflows | Short, skippable; avoid feature dumps |
| **Checklists / progress bars** | Structure multi-step setup across sessions | Persist state; tie items to clear “done” criteria |
| **Tooltips / hotspots** | Just-in-time help in context | Prefer over modal walls; respect power users |
| **Interactive tutorials** | Teach by doing (sandbox, sample task) | Strong for abstract or empty products |
| **Empty-state guidance** | First landing — what to do next | Role- and tenant-aware CTAs |
| **Template libraries** | Accelerate first output | Reduces blank-page paralysis |
| **Sample data** | Safe exploration before production config | Critical for analytics, dev tools, complex domains |
| **Setup wizards** | Ordered steps with dependencies | Use when order matters (integrations, compliance) |

Mix patterns by **persona** and **step**; the same product often needs tours for end users and wizards for admins.

---

## Time-to-value optimization

1. **Identify the “aha moment” with data** — Correlate early behaviors with retention, expansion, or support reduction. Validate with interviews; avoid vanity events (e.g. “clicked settings”) unless they predict outcomes.
2. **Reduce steps to first value** — Remove sequential bottlenecks; parallelize; pre-provision defaults; defer advanced config until after activation.
3. **Progressive disclosure** — Show the happy path first; reveal depth (permissions, edge cases, admin tools) after core success.
4. **Contextual onboarding** — Trigger guidance from **state** (empty project, failed integration), not only time since signup.

---

## Onboarding flow with decision points

```blueprint-diagram
key: sequence
alt: Diagram
```

---

## Onboarding segmentation

| Dimension | Personalization strategies |
|-----------|----------------------------|
| **Persona** | Different checklists, empty states, and training (admin vs. contributor vs. executive) |
| **Plan / tier** | Feature gates, depth of integration steps, human touch eligibility |
| **Use case** | Templates, sample data, and success milestones mapped to JTBD |
| **Team size** | Workspace creation, invites, RBAC, and “team activation” as a milestone |

Instrument each segment separately so you do not optimize the funnel for one persona while harming another.

---

## Email onboarding sequences

Design **welcome series** to reinforce in-product progress, not duplicate generic tours.

| Approach | When to use |
|----------|-------------|
| **Time-based** | Predictable drip for simple products; easy to operationalize |
| **Trigger-based** | Strong when behavior varies (integration failed, checklist stalled) — higher relevance |

**Illustrative content themes by day** (adapt length and channel to your motion):

| Timing | Example focus |
|--------|----------------|
| **Day 0** | Welcome, single CTA to first step, set expectations |
| **Day 1** | Complete core setup; link to docs or template |
| **Day 3** | First value moment nudge; social proof or quick win story |
| **Day 7** | Deeper workflow; invite teammates or connect integration |
| **Day 14** | Habit / advanced capability; office hours or webinar (if mid-touch) |
| **Day 30** | Health check, success criteria, upgrade or expansion path (where appropriate) |

Always honor **opt-out**, frequency caps, and **product truth** (do not promise features they cannot access).

---

## Measurement framework

| Metric | What it tells you |
|--------|-------------------|
| **Signup-to-activation rate** | Overall funnel health by segment |
| **Time-to-value (median / P90)** | Friction and urgency of optimization |
| **Onboarding completion rate** | Checklist / wizard effectiveness |
| **Step drop-off** | Specific UX or copy failures |
| **Feature adoption during onboarding** | Whether users engage the right capabilities |
| **Support tickets during onboarding** | Gaps in product guidance or docs |

Pair **quantitative** funnels with **qualitative** session replay or interviews on the worst drop-off steps.

---

## Team onboarding challenges

- **Admin vs. member** — Admins bear integrations, SSO, billing, and invites; members need role-specific “first task.” Split journeys.
- **Workspace / org setup** — Multi-step: create space, naming, defaults, invite policy. Make “invite and first active member” a visible milestone.
- **SSO / SCIM** — Often async with IT; provide status, retries, and clear IdP documentation. Human escalation path for enterprise.
- **Team invitations** — Track pending invites, reminders, and permission errors; failed invites are a top silent failure mode.

---

## Onboarding for enterprise

- **Custom onboarding plans** — Mutual milestones, owners, dates, and evidence (artifacts or system events).
- **Implementation managers** — Coordinate product, customer IT, and partners; single threaded accountability.
- **Training sessions** — Role-based enablement; recorded for late joiners.
- **Success milestones in contract** — Tie commercial outcomes to observable delivery (where appropriate and ethical).

---

## Re-onboarding

| Trigger | Aim |
|---------|-----|
| **Major new features** | Targeted in-product education; avoid full reset for everyone |
| **Returning users** | Short “what changed” path; restore context |
| **Plan upgrades** | Unlock workflows and admin tasks relevant to new tier |
| **Role changes** | New permissions and responsibilities without repeating full tenant setup |

---

## Anti-patterns

| Anti-pattern | Why it hurts |
|--------------|--------------|
| **Feature dump** | Overwhelms; delays first value |
| **Forced tours** | Frustrates experts; increases abandonment |
| **No skip option** | Blocks urgent users |
| **One-size-fits-all** | Wrong tasks for persona or use case |
| **Ignoring mobile onboarding** | Broken first session on common devices |

---

## External references

- **Intercom on Onboarding** — Product-led onboarding and messaging patterns.
- **Product-Led Onboarding** (Ramli John) — Systematic onboarding for PLG motions.
- **Appcues** — Guides, checklists, and resources on in-product onboarding.
- **useronboard.com** — Teardown-style examples and UX critique.

---

*Keep project-specific customer success documentation in `docs/product/customer-success/` and support playbooks in `docs/operations/`, not in this file.*
