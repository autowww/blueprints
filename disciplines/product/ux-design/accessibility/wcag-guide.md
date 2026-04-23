---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# WCAG 2.2 comprehensive guide

**Purpose:** Project-agnostic orientation to **Web Content Accessibility Guidelines (WCAG) 2.2** — the global standard for perceivable, operable, understandable, and robust web content — plus testing approaches and documentation expectations.

---

## Overview

WCAG defines **success criteria** testable statements for accessibility. Version **2.2** adds criteria for pointer gestures, target size, authentication, and redundant entry, among others. Conformance is claimed at **A**, **AA**, or **AAA** for a defined **scope** (pages, flows, or product). Legal and procurement contexts often target **AA**.

---

## POUR principles

| Principle | Meaning | Example success criteria themes |
|-----------|---------|--------------------------------|
| **Perceivable** | Information and UI components must be presentable in ways users can perceive | Text alternatives, captions, adaptable structure, distinguishable (contrast, resize) |
| **Operable** | UI and navigation must be operable | Keyboard access, timing, seizures, navigation, pointer inputs |
| **Understandable** | Information and operation must be understandable | Language, predictable behavior, error help |
| **Robust** | Content must work with current and emerging assistive technologies | Valid parsing, name/role/value, status messages |

---

## Conformance levels

| Level | Intent | What it typically adds | Legal / procurement | Coverage |
|-------|--------|------------------------|----------------------|----------|
| **A** | Minimum baseline | Alternatives for non-text, keyboard, no keyboard trap, timing adjustable basics, bypass blocks, focus order, page titles | Often insufficient alone for policy | ~25 criteria (subset) |
| **AA** | **Recommended target** for most orgs | Contrast (4.5:1 text), resize to 200%, reflow, multiple ways, headings, focus visible, labels, error identification, status on input | ADA-style digital cases often reference WCAG 2.x AA; EN 301 549 aligns | Adds many everyday UX/a11y expectations |
| **AAA** | Enhanced | Higher contrast (7:1), sign language, extended audio description, context help everywhere | Rarely required in full — aspirational for critical content | Strictest; not always feasible sitewide |

Always cite **version** (e.g. WCAG 2.2) and **scope** in conformance statements.

---

## WCAG audit workflow

```blueprint-diagram
key: linear
alt: Diagram
```

---

## Perceivable (guideline 1.x) — key themes

| Guideline | Key success criteria (examples) | Common failures | Fixes |
|-----------|--------------------------------|-----------------|-------|
| **1.1 Text alternatives** | Non-text content has text alternative | Decorative images missing `alt=""`; icons without names | Meaningful `alt`; `aria-label` only when native insufficient |
| **1.2 Time-based media** | Captions, audio description, transcripts | Auto-play video without captions | Captions; transcripts for audio-only |
| **1.3 Adaptable** | Structure, headings, labels, orientation | Tables for layout read wrongly; missing headings | Semantic HTML; programmatic headings |
| **1.4 Distinguishable** | Contrast, resize, reflow, text spacing | Gray-on-gray; fixed height clipping text | Design tokens for contrast; responsive text |

---

## Operable (guideline 2.x) — key themes

| Guideline | Key themes | Common failures | Fixes |
|-----------|------------|-----------------|-------|
| **2.1 Keyboard** | All functionality from keyboard | Custom widgets not focusable | Native controls or full keyboard pattern |
| **2.2 Enough time** | Adjustable limits, pauses | Session timeout without warning | Extend time; warn before expiry |
| **2.3 Seizures** | Flash thresholds | Animated hero flashes | Respect thresholds; reduced motion |
| **2.4 Navigable** | Bypass blocks, titles, focus order, link purpose | Missing skip link; “click here” | Skip link; descriptive links |
| **2.5 Input modalities** | Target size, pointer gestures, labels in name | Tiny touch targets; path-only gestures | Min size; alternatives |

---

## Understandable (guideline 3.x) — key themes

| Guideline | Key themes | Common failures | Fixes |
|-----------|------------|-----------------|-------|
| **3.1 Readable** | Language of page | Missing `lang` | `<html lang>` |
| **3.2 Predictable** | On focus/input predictable | Auto-submit on focus | User-initiated changes |
| **3.3 Input assistance** | Labels, errors, suggestions | Errors only in red | Text + association; error summary |

---

## Robust (guideline 4.1)

| Topic | Intent | Common failures | Fixes |
|-------|--------|-----------------|-------|
| **Parsing (legacy in 4.1.1)** | Valid DOM in older WCAG | Duplicate IDs | Fix duplicates; valid HTML |
| **Name, role, value** | AT gets correct semantics | Div “buttons” | `<button>` or ARIA + keyboard |
| **Status messages** | Important updates perceivable | Toast not announced | `role="status"` or `aria-live` |

---

## Testing methodology — what each layer catches

| Approach | Strengths | Blind spots |
|----------|-----------|-------------|
| **Automated** (axe, Lighthouse, WAVE) | Fast regression; obvious bugs | ~30–40% of issues; context, meaning, full keyboard |
| **Manual** | Contrast judgment, reading order, logical focus | Time-consuming |
| **Assistive technology** | Real screen reader / voice experience | Setup skill; environment variance |

Use **all three** for meaningful release gates.

---

## Assistive technology testing matrix

| AT type | Examples | What to verify |
|---------|----------|----------------|
| **Screen readers** | NVDA (Win), JAWS (Win), VoiceOver (macOS/iOS), TalkBack (Android) | Landmarks, headings, forms, live regions, custom widgets |
| **Magnification** | OS zoom, browser zoom | Reflow, clipping, horizontal scroll traps |
| **Switch / keyboard only** | Tab, arrow patterns | Focus order, no traps, visible focus |
| **Voice control** | Dragon, platform voice | Visible labels match speakable names |

---

## Legal landscape (high level)

| Framework | Scope (typical) | Conformance target | Enforcement notes |
|-----------|-----------------|-------------------|-------------------|
| **ADA (US)** | Public accommodations; courts split on websites/apps | Often WCAG 2.x **AA** cited | DOJ rulemaking; litigation risk |
| **EAA (EU)** | Products and services in scope by member state law | EN 301 549 → WCAG-based | Market surveillance |
| **EN 301 549** | ICT procurement EU | WCAG 2.1 AA (check revision) | Specified in tenders |
| **Section 508 (US)** | Federal ICT | WCAG 2.0 AA baseline in refresh | Agency procurement |
| **AODA (Ontario)** | Ontario public / large orgs | WCAG 2.0 AA (verify updates) | Penalties |
| **DDA / UK** | UK services | WCAG-like reasonable adjustment | EHRC, complaints |

This table is **not legal advice** — verify with counsel for your jurisdiction and contract.

---

## VPAT / ACR

- **VPAT** (Voluntary Product Accessibility Template) — vendor self-disclosure of product accessibility against standards.
- **ACR** (Accessibility Conformance Report) — completed VPAT for a specific product/version.
- **Who needs it:** Enterprise buyers, regulated sectors, federal supply schedules.
- **Structure:** Product info, evaluation methods, tables per criterion (supports / partially / does not).
- **Maintenance:** Update per major release; tie to tested build identifiers.

---

## Color and contrast

- **WCAG 2.2 contrast:** **4.5:1** for normal text; **3:1** for large text (and UI components / graphical objects where criteria apply).
- **Tools:** Colour Contrast Analyser (TPGi), browser extensions (e.g. Stark), design-plugin checks.
- **Design systems:** Tokenize foreground/background pairs; fail builds on regression.

---

## Anti-patterns

- **Overlay widgets** marketed as “instant compliance” — do not replace remediation; often harm users.
- **Images of text** — avoid when text can be live (except logos etc.).
- **Custom controls without names/roles/keyboard** — breaks AT.
- **Focus traps** without escape — fails operable.

---

## External references

- [W3C WAI](https://www.w3.org/WAI/) — fundamentals and tutorials.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — normative spec.
- [WebAIM](https://webaim.org/) — articles and checklists.
- [Deque University](https://dequeuniversity.com/) — deep curriculum.
- [The A11Y Project](https://www.a11yproject.com/) — practical guides.

*Keep project-specific accessibility audits in docs/product/ and remediation plans in docs/development/, not in this file.*
