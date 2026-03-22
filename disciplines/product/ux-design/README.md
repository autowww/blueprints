# UX / UI Design

Reusable, **project-agnostic** blueprint for **UX / UI Design** — the discipline of making digital products usable, desirable, and accessible through user research, interaction design, visual design, and systematic evaluation.

UX / UI Design answers **"is the product usable, desirable, and accessible?"** — a question that spans the entire PDLC (especially P1 Discover and P2 Validate) and shapes every SDLC phase from requirements through release.

| Document | Purpose |
|----------|---------|
| [**UX-DESIGN.md**](UX-DESIGN.md) | Design thinking, interaction design principles, visual design systems, information architecture, research methods, competencies |
| [**UX-SDLC-PDLC-BRIDGE.md**](UX-SDLC-PDLC-BRIDGE.md) | How UX / UI Design maps across SDLC phases A–F and PDLC phases P1–P6 — emphasis on Discovery, Validation, Specify, and Verify |
| [**techniques/**](techniques/README.md) | Deep guides: user research methods, usability testing, prototyping, A/B experimentation, design critique |
| [**accessibility/**](accessibility/README.md) | WCAG compliance, ARIA patterns, assistive technology, inclusive design, audit checklists |

## Relationship to other packages

| Package | How UX / UI Design relates |
|---------|---------------------------|
| [`blueprints/pdlc/`](../../../pdlc/README.md) | UX Design is the primary execution arm of PDLC P1 (Discover Problem) and P2 (Validate Solution). The PDLC defines UX Researcher and Designer as product trio roles; this discipline package provides the **body of knowledge** those roles draw on. |
| [`blueprints/sdlc/`](../../../sdlc/README.md) | UX deliverables (wireframes, prototypes, specs, design tokens) feed SDLC phases A (Discover) and B (Specify). Usability validation runs parallel to SDLC phase E (Verify). |
| [`blueprints/disciplines/product/ba/`](../ba/README.md) | BA elicits *what* stakeholders need; UX discovers *how* users experience and interact with solutions. Requirements analysis (BA) and interaction design (UX) converge during SDLC phase B. |
| [`blueprints/disciplines/engineering/testing/`](../../engineering/testing/README.md) | Usability testing is a UX concern; functional and accessibility testing overlap with QA. Accessibility automated checks integrate into CI/CD quality gates. |
| [`blueprints/disciplines/engineering/software-architecture/`](../../engineering/software-architecture/README.md) | Architecture decisions (component boundaries, API design, performance budgets) constrain or enable UX. Design systems bridge architecture and visual design. |
| [`blueprints/disciplines/security/`](../../security/README.md) | Security controls (authentication flows, consent dialogs, error messaging) have direct UX implications. Secure-by-default patterns must remain usable. |

## Scope

This package covers **UX / UI Design as a discipline** — not just wireframing tools. It includes:

- **Design thinking** — double diamond, human-centered design, divergent/convergent cycles
- **User research** — interviews, surveys, contextual inquiry, diary studies, analytics interpretation
- **Interaction design** — affordances, feedback, consistency, mental models, navigation patterns
- **Visual design** — typography, color theory, spacing, layout grids, component libraries
- **Information architecture** — content taxonomy, navigation structure, labeling systems, search
- **Design systems** — design tokens, component APIs, theming, design-dev handoff, Storybook
- **Accessibility** — WCAG 2.x/3.0, ARIA patterns, assistive technology, inclusive design
- **Prototyping and validation** — low-fidelity sketches through high-fidelity interactive prototypes
- **Usability testing** — moderated/unmoderated testing, heuristic evaluation, cognitive walkthroughs

Reference bodies of knowledge: Nielsen Norman Group, Interaction Design Foundation, UXPA Body of Knowledge, WCAG (W3C), Material Design, Apple Human Interface Guidelines.

---

*Keep project-specific design assets in `docs/design/` and design decisions in `docs/adr/`, not in this file.*
