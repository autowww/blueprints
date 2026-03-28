# WCAG, ADA & Accessibility Compliance

**Purpose:** Project-agnostic guide to **digital accessibility** — WCAG conformance, common legal hooks (US, EU, Canada, Australia), engineering mappings, testing, VPAT, and procurement. **Not legal advice**; ADA circuit splits and national laws evolve — verify with counsel.

**Audience:** Product, design, and engineering teams shipping web and mobile experiences. Cross-ref: [`../COMPLIANCE.md`](../COMPLIANCE.md), [`README.md`](README.md).

---

## Overview

Accessibility is both a **legal obligation** in many jurisdictions and an **ethical and commercial** imperative: broader usable products, lower litigation/procurement friction, and better UX for everyone (including temporary and situational disabilities). **WCAG** is the technical backbone referenced by laws and procurement standards worldwide; **conformance claims** must name **version**, **level**, and **scope** (which pages/flows).

---

## Legal landscape (summary)

| Framework | Scope | Applies to | Conformance target | Enforcement / notes |
|-----------|-------|------------|--------------------|---------------------|
| **ADA Title III (US)** | Places of **public accommodation** — digital applicability debated by circuit; **DOJ** rulemaking moving toward WCAG 2.1 AA for state/local **Title II** (distinct but influential). | Businesses open to the public (interpretation varies). | Often **WCAG 2.x AA** cited in settlements. | Private suits, DOJ matters; damages/injunctive relief. |
| **Section 508 (US federal)** | Federal agencies’ ICT; **vendor** products sold to federal government. | Agencies + contractors under specified procurements. | **WCAG 2.0 AA** via **Rev 508**; **VPAT** common in sales. | Procurement gate; agency enforcement. |
| **European Accessibility Act (EAA)** | Products/services in scope (e.g. e-commerce, banking, transport, media devices — phased). | EU market actors from **June 2025** (enforcement timelines vary by Member State). | **EN 301 549** (references **WCAG** for web). | Market surveillance; penalties per national law. |
| **EN 301 549 (EU)** | Harmonized standard for accessibility of ICT in public procurement and policy contexts. | Public sector procurement; referenced by EAA implementation. | Includes WCAG-based criteria for web content. | Supports conformity assessment. |
| **AODA (Ontario)** | Organizations in Ontario; **WCAG 2.0 AA** commonly referenced for web. | Public and private sector per size thresholds. | **WCAG 2.0 AA** (verify current regulation). | Administrative penalties. |
| **DDA (Australia)** | Disability discrimination law; standards adopted under it (e.g. **AS EN 301 549** in federal procurement). | Service providers; government ICT. | Often **WCAG 2.x**-aligned in practice. | Complaints and legal action. |

---

## WCAG 2.2 conformance levels

| Level | What it adds | Legal / practical notes |
|-------|--------------|-------------------------|
| **A** | Baseline (e.g. alt text for non-decorative images, keyboard operability foundations, no keyboard traps). | Rarely sufficient alone for enterprise or public-sector claims. |
| **AA** | **Contrast** (e.g. **4.5:1** normal text), **resize** to 200%, **focus visible**, more form/error guidance, additional nav requirements. | **Most cited** level in law, settlement, and RFP. |
| **AAA** | Stricter contrast, sign language, extended audio description, etc. | **Whole-site AAA** is often impractical; sometimes partial AAA for critical flows. |

---

## WCAG compliance workflow

```blueprint-diagram
key: linear
alt: Diagram
```

---

## WCAG-to-engineering mapping (selected)

| Success criterion | Technical implementation |
|-------------------|-------------------------|
| **1.1.1** Non-text content | Meaningful **`alt`**; `aria-label` where appropriate; decorative images `alt=""` / `role="presentation"`. |
| **1.4.3** Contrast (minimum) | Design tokens at **4.5:1** normal text / **3:1** large; check graphical objects and UI components (related SCs). |
| **2.1.1** Keyboard | All interactive controls **focusable** and operable without pointer; no traps; custom widgets with keyboard model + ARIA. |
| **2.4.x** Nav / focus | **Skip links**, logical focus order, **visible focus** indicators, descriptive headings. |
| **3.3.x** Input assistance | Labels associated with inputs; clear error messages; suggestions where known. |
| **4.1.2** Name, role, value | **Semantic HTML** first; **ARIA** only when necessary; live regions for dynamic updates. |

---

## Testing methodology comparison

| Layer | Examples | Catches well | Coverage (indicative) |
|-------|----------|--------------|------------------------|
| **Automated** | axe-core, Lighthouse, WAVE, pa11y | Obvious violations, missing labels, some contrast | Often **~30–40%** of issues — tool-dependent |
| **Manual** | Keyboard-only pass, 200% zoom, reflow at 320px, forms | Focus order, custom widgets, logical structure | High for expert review |
| **Assistive technology** | NVDA, JAWS, VoiceOver, magnifiers | Screen reader announcements, live regions, real-world friction | Critical for complex apps |

---

## VPAT (Voluntary Product Accessibility Template)

- **Purpose:** Disclose how product meets **Section 508** / **WCAG** / **EN 301 549** criteria for **procurement**.
- **Structure:** Tables per standard with **criteria**, **Conformance level**, **remarks**.
- **Conformance levels per row:** **Supports**, **Partially Supports**, **Does Not Support**, **Not Applicable** — must be **evidence-based**.
- **Update frequency:** Major releases or annual refresh for active sales cycles.
- **Public disclosure:** Many vendors publish ACRs; accuracy matters for **false claims** risk.

---

## Accessibility audit process

1. **Scope:** URLs, states (auth, errors), components, design system.
2. **Sampling:** Representative templates + high-risk flows (checkout, auth, data entry).
3. **AT testing** on agreed browser/SR combinations.
4. **Findings report** with WCAG refs, severity, repro steps.
5. **Remediation priority:** **P1** blocks access; **P2** significant difficulty; **P3** minor.

---

## Design system accessibility

- **Component library** with documented keyboard and ARIA patterns.
- **Color tokens** with contrast pairs; no color-only status.
- **Focus styles** that meet **2.4.7** / **2.4.11** expectations.
- **`prefers-reduced-motion`** for animation.
- **Responsive typography** and reflow-friendly layouts.

---

## Procurement

- **Section 508** — **VPAT/ACR** and sometimes **Accessibility Conformance Report** in RFP responses.
- **Accessibility clause** in RFPs: WCAG 2.1/2.2 AA, remediation SLAs, VPAT updates.

---

## Is WCAG AA legally required? (decision tree)

```blueprint-diagram
key: linear
alt: Diagram
```

---

## Common fixes

| Issue | Fix |
|-------|-----|
| Missing alt | Descriptive alt; `alt=""` if decorative. |
| Color-only information | Add text, pattern, or icon + text. |
| Missing labels | `<label for>` or `aria-labelledby`. |
| Keyboard traps | Focus management in modals/menus; `inert` / focus trap libs done right. |
| No skip link | “Skip to main content” as first focusable element. |
| Autoplay | No unexpected audio; user control. |
| Low contrast | Token updates; avoid text on busy images without overlay. |

---

## Accessibility statement

**Elements:** Commitment; **standard** (e.g. WCAG 2.2 AA); **scope**; known limitations; **feedback** channel and response time; date of last review.

---

## Monitoring and regression prevention

- **CI:** axe-core (e.g. Cypress/Playwright), linting (eslint-plugin-jsx-a11y).
- **Design review** gates for new components.
- **Periodic audits** (annual or per major redesign).

---

## Anti-patterns

- **Overlay widgets** marketed as “instant compliance” — often fail real AT use and draw enforcement scrutiny.
- **Accessibility as a single phase** at launch — without CI and design discipline.
- **VPAT without testing** — procurement and legal exposure.
- **PDF neglect** — tagged PDFs or HTML-first alternatives.

---

## External references

- [W3C WAI](https://www.w3.org/WAI/)
- [WebAIM](https://webaim.org/)
- [Deque University](https://dequeuniversity.com/)
- [ITI VPAT](https://www.itic.org/policy/accessibility/vpat) template
- [Section508.gov](https://www.section508.gov/)
- [European Accessibility Act](https://single-market-economy.ec.europa.eu/sectors/retail/ecommerce/european-accessibility-act_en) (EU Commission overview)

---

*Keep project-specific compliance documentation in docs/security/compliance/, DPIAs in docs/security/, and compliance decisions in docs/adr/, not in this file.*
