---
slug: discipline-ux
tier: 201
lens: discipline
nav_section: "Disciplines"
---

# UX / UI design body of knowledge

This document maps the core concerns of **UX / UI Design** — user research, interaction design, visual design, information architecture, design systems, and accessibility — to the blueprint ecosystem.

**How UX design relates to PDLC and SDLC:** UX Design is a **cross-cutting discipline** that drives discovery and validation in PDLC and shapes deliverables across SDLC. See [`UX-SDLC-PDLC-BRIDGE.md`](UX-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Techniques:** Research and design methods are cataloged in [`techniques/`](techniques/README.md).

**Accessibility:** WCAG compliance, ARIA, and inclusive design guidance is in [`accessibility/`](accessibility/README.md).

---

## 1. Design thinking

Design thinking is a human-centered approach to innovation that integrates human needs, technological possibilities, and business viability.

### Double diamond model

| Phase | Mode | Activities | Outputs |
|-------|------|-----------|---------|
| **Discover** | Divergent | User interviews, contextual inquiry, diary studies, competitive analysis, analytics review | Research synthesis, empathy maps, journey maps |
| **Define** | Convergent | Affinity mapping, insight statements, "how might we" framing, problem prioritization | Problem statements, design principles, opportunity areas |
| **Develop** | Divergent | Ideation workshops, sketching, concept generation, design sprints | Concepts, wireframes, low-fidelity prototypes |
| **Deliver** | Convergent | Prototyping, usability testing, iteration, specification, design-dev handoff | Validated designs, interaction specs, design tokens |

### Design principles (universal)

| Principle | Description |
|-----------|-------------|
| **User-centered** | Ground every decision in evidence about real users — observed behavior, not assumptions |
| **Inclusive** | Design for the widest range of abilities, contexts, and devices from the start |
| **Iterative** | Ship, measure, learn, and refine — no design survives first contact unchanged |
| **Systematic** | Build and maintain design systems so that consistency scales beyond any single designer |
| **Collaborative** | Design is a team sport — involve engineering, product, and users throughout |

---

## 2. Interaction design

### Core concepts

| Concept | Definition | Design implication |
|---------|-----------|-------------------|
| **Affordance** | A perceived property that suggests how an object can be used | Buttons should look clickable; draggable items should look grabbable |
| **Signifier** | A signal that communicates where and how to act | Labels, icons, placeholder text, cursor changes |
| **Feedback** | System response to user action | Loading states, success/error messages, animations, haptics |
| **Mapping** | Relationship between controls and their effects | Spatial layout matching conceptual model; slider direction matching value direction |
| **Constraint** | Limiting possible actions to prevent errors | Disabled states, input validation, confirmation dialogs for destructive actions |
| **Consistency** | Similar elements behave similarly across the system | Reusable components, shared interaction patterns, predictable navigation |

### Navigation patterns

| Pattern | Best fit | Trade-off |
|---------|----------|-----------|
| **Tab bar / bottom nav** | Mobile apps with 3–5 top-level sections | Limited to few items; not suitable for deep hierarchies |
| **Sidebar / drawer** | Desktop apps, admin panels, deep navigation trees | Can hide important items; hamburger menus reduce discoverability |
| **Breadcrumbs** | Content-heavy sites with clear hierarchies | Not useful for flat structures or task-based flows |
| **Wizard / stepper** | Multi-step forms, onboarding flows | Forces linear progression; branching is hard to communicate |
| **Search + browse** | Large content catalogs, documentation, marketplaces | Requires good search infrastructure; cold-start problem for new users |
| **Command palette** | Power-user tools, IDEs, productivity apps | Invisible to novice users; requires keyboard fluency |

### Responsive design tiers

| Tier | Breakpoint range | Layout strategy |
|------|-----------------|-----------------|
| **Mobile** | < 768 px | Single column, stacked cards, bottom-sheet actions, touch targets >= 44 px |
| **Tablet** | 768–1024 px | Two-column or split-view, collapsible panels |
| **Desktop** | > 1024 px | Multi-column, persistent sidebar, hover states, keyboard shortcuts |

---

## 3. Visual design

### Typography

| Guideline | Rationale |
|-----------|-----------|
| Limit to 2–3 typefaces (display, body, mono) | Cognitive consistency; faster loading |
| Body text >= 16 px, line height 1.4–1.6 | Readability on screens; WCAG compliance |
| Establish a modular scale (e.g. 1.25 or 1.333) | Harmonious size progression |
| Ensure contrast ratio >= 4.5:1 (AA) or >= 7:1 (AAA) for text | WCAG 2.x Success Criterion 1.4.3 / 1.4.6 |

### Color

| Guideline | Rationale |
|-----------|-----------|
| Define semantic palette (primary, secondary, success, warning, error, neutral) | Consistent meaning across the product |
| Use color tokens, not raw hex values | Theming support (light/dark mode); single source of truth |
| Never rely on color alone to convey information | Accessibility — colorblind users need shape, text, or icon reinforcement |
| Test with contrast checkers and color-blindness simulators | Catch issues before users do |

### Spacing and layout

| Guideline | Rationale |
|-----------|-----------|
| Use a spacing scale (e.g. 4 px base: 4, 8, 12, 16, 24, 32, 48, 64) | Visual rhythm; predictable alignment |
| Apply consistent padding within components, margin between them | Separation of internal and external spacing concerns |
| Grid systems (8-column mobile, 12-column desktop) | Alignment and responsive reflow |

---

## 4. Information architecture

| Concept | Description |
|---------|-------------|
| **Content inventory** | Catalog of all content types, their purpose, and ownership |
| **Card sorting** | User research technique to discover mental models for categorization |
| **Tree testing** | Validates navigation structure by asking users to find items in a proposed hierarchy |
| **Taxonomy** | Controlled vocabulary and hierarchical categorization of content |
| **Labeling** | Clear, consistent, user-centric names for navigation items and categories |
| **Search schema** | Facets, filters, autocomplete, synonyms that support findability |

---

## 5. Design systems

A design system is a collection of reusable components, guided by clear standards, that can be assembled to build any number of applications.

### Anatomy

| Layer | Contents | Owned by |
|-------|----------|----------|
| **Design tokens** | Color, typography, spacing, breakpoint, shadow values expressed as platform-agnostic variables | Design + engineering jointly |
| **Core components** | Buttons, inputs, modals, cards, tables — with defined states, variants, and accessibility annotations | Design system team or guild |
| **Patterns** | Compositions of components for common use cases (forms, data tables, search, navigation) | Product teams contribute; system team curates |
| **Documentation** | Usage guidelines, do/don't examples, code snippets, Storybook / Figma references | Design system team |
| **Governance** | Contribution model (open/federated/centralized), versioning, deprecation, breaking-change policy | Architecture + design leads |

### Design-dev handoff

| Practice | Description |
|----------|-------------|
| **Design tokens in code** | Export tokens from design tool (Figma, Tokens Studio) to CSS custom properties / JS constants |
| **Component API contracts** | Props, variants, states, and accessibility requirements specified before implementation |
| **Interactive documentation** | Storybook or equivalent — live components with controls, accessibility checks, visual regression |
| **Visual regression testing** | Automated screenshot comparison (Chromatic, Percy, Playwright) to catch unintended changes |
| **Annotation layers** | Redlines, spacing callouts, and interaction notes attached to design frames |

---

## 6. User research methods

| Method | Type | When | Output |
|--------|------|------|--------|
| **User interview** | Qualitative | Discovery, validation | Transcripts, insight themes, quotes |
| **Contextual inquiry** | Qualitative | Discovery | Workflow observations, environment constraints |
| **Survey** | Quantitative | Validation, satisfaction measurement | Statistical distributions, NPS/CSAT/SUS scores |
| **Usability test** | Mixed | Validation, iteration | Task success rate, time on task, severity-rated findings |
| **A/B experiment** | Quantitative | Growth, optimization | Statistically significant lift/drop in target metric |
| **Card sort** | Mixed | Information architecture | Category groupings, similarity matrices |
| **Tree test** | Quantitative | Information architecture | Findability score, path analysis |
| **Diary study** | Qualitative | Longitudinal behavior | Patterns over time, context shifts |
| **Analytics review** | Quantitative | Continuous | Funnels, drop-off points, feature usage frequency |
| **Heuristic evaluation** | Expert review | Any time | Severity-rated usability issues against established heuristics |

---

## 7. Prototyping spectrum

| Fidelity | Tools | Purpose | Effort |
|----------|-------|---------|--------|
| **Sketch / whiteboard** | Paper, whiteboard, tablet | Explore ideas quickly; disposable | Minutes |
| **Wireframe** | Figma, Balsamiq, Whimsical | Structure and layout; no visual polish | Hours |
| **Interactive prototype** | Figma prototyping, Framer, ProtoPie | Click-through flows for usability testing | Hours–days |
| **High-fidelity mockup** | Figma, Sketch | Pixel-perfect visual design for handoff | Days |
| **Code prototype** | HTML/CSS/JS, Storybook, framework components | Test real interactions, performance, accessibility | Days–weeks |

---

## 8. Competencies

| Competency | Description |
|------------|-------------|
| **Research craft** | Planning studies, recruiting participants, moderating sessions, synthesizing findings, avoiding bias |
| **Interaction design** | Translating user needs into flows, wireframes, and interaction specifications |
| **Visual design** | Applying typography, color, layout, and motion to create coherent, polished interfaces |
| **Systems thinking** | Building and maintaining design systems that scale across products and teams |
| **Accessibility expertise** | Designing and auditing for WCAG compliance; understanding assistive technology |
| **Facilitation** | Leading design sprints, workshops, and critique sessions |
| **Data literacy** | Interpreting analytics, designing experiments, and using quantitative evidence to inform design decisions |
| **Communication** | Presenting design rationale to stakeholders; writing clear specifications for engineering |

---

## 9. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| Nielsen Norman Group | https://www.nngroup.com/ | Foundational UX research and guidelines |
| Interaction Design Foundation | https://www.interaction-design.org/ | Comprehensive UX education and encyclopedia |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | Web accessibility standard |
| Material Design | https://m3.material.io/ | Google's design system and guidelines |
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | Apple platform design guidance |
| Laws of UX | https://lawsofux.com/ | Psychology-based UX principles |
| Design Thinking (IDEO) | https://designthinking.ideo.com/ | Human-centered design methodology |
| Inclusive Design (Microsoft) | https://inclusive.microsoft.design/ | Inclusive design toolkit and principles |

---

*Keep project-specific design documentation in `docs/design/`, design tokens in `docs/design/tokens/`, and design decisions in `docs/adr/`, not in this file.*
