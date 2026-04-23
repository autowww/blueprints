---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Accessibility (blueprint)

**Purpose:** Deep, **project-agnostic** guidance for building accessible digital products. Covers standards, implementation patterns, testing approaches, and organizational practices.

**Accessibility as a right, not a feature:** Inclusive design is a **baseline quality bar**, not an edge-case backlog deferred to “phase two.” Standards like WCAG encode expectations for perceivable, operable, understandable, and robust experiences; keyboard support, semantics, and ARIA complete behaviors for assistive technology. Treat accessibility like security or performance: explicit targets, automated checks, manual verification, and regression discipline.

**Audience:** Teams adopting [`blueprints/disciplines/product/ux-design/`](../README.md); project docs in **`docs/design/accessibility/`**. **Core knowledge:** [`UX-DESIGN.md`](../UX-DESIGN.md). **Bridge:** [`UX-SDLC-PDLC-BRIDGE.md`](../UX-SDLC-PDLC-BRIDGE.md).

---

## Accessibility implementation workflow

```blueprint-diagram
key: linear
alt: Diagram
```

---

## Topic guides

| Topic | Focus | Deep guide |
|-------|-------|------------|
| **WCAG conformance** | POUR, levels A/AA/AAA, criteria by guideline, testing layers, legal overview, VPAT/ACR | [`wcag-guide.md`](wcag-guide.md) |
| **ARIA patterns** | Native-first rule, roles, states, APG widgets, live regions, testing | [`aria-patterns.md`](aria-patterns.md) |
| **Keyboard navigation** | Focus order, skip links, traps, custom widget keys | [`wcag-guide.md`](wcag-guide.md) · [`aria-patterns.md`](aria-patterns.md) |
| **Screen reader compatibility** | Landmarks, names/roles, live regions; NVDA, JAWS, VoiceOver, TalkBack | [`wcag-guide.md`](wcag-guide.md#assistive-technology-testing-matrix) · [`aria-patterns.md`](aria-patterns.md#testing-aria) |
| **Color and contrast** | Ratios, tooling, tokens | [`wcag-guide.md`](wcag-guide.md#color-and-contrast) |
| **Motion and animation** | `prefers-reduced-motion`, seizure safety | [`UX-DESIGN.md`](../UX-DESIGN.md) · [`wcag-guide.md`](wcag-guide.md) |
| **Forms and inputs** | Labels, errors, autocomplete, grouping | [`wcag-guide.md`](wcag-guide.md) |
| **Inclusive design** | Permanent, temporary, situational barriers | [`UX-DESIGN.md`](../UX-DESIGN.md) |
| **Audit and testing** | Scope, automated scan, manual + AT, remediation loop | [`wcag-guide.md`](wcag-guide.md#wcag-audit-workflow) |

**External references:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/), [Microsoft Inclusive Design](https://inclusive.microsoft.design/), [WebAIM](https://webaim.org/), [The A11Y Project](https://www.a11yproject.com/).

*Keep project-specific accessibility audits in docs/product/ and remediation plans in docs/development/, not in this file.*
