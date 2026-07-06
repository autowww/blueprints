---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Interaction design patterns and principles

**Purpose:** Project-agnostic guidance for designing **how** users accomplish goals — predictable behavior, clear feedback, and patterns that scale across platforms and design systems.

---

## Overview

Interaction design (IxD) defines the **behavior** of an interface: states, transitions, errors, navigation, and input. It sits between user research (what people need) and visual design (how it looks). Strong IxD reduces **cognitive load**, prevents errors, and makes systems **learnable** and **efficient**.

---

## Interaction design principles

| Principle | Definition | Example | If violated |
|-----------|------------|---------|-------------|
| **Visibility** | Important options and system state are discoverable | Primary actions visible on screen; settings findable | Users miss features or feel “stuck” |
| **Feedback** | The system acknowledges actions and progress | Button pressed state; toast after save | Uncertainty, double submits, distrust |
| **Constraints** | Limits guide valid actions | Disabled submit until form valid; date picker ranges | Errors, frustration |
| **Mapping** | Controls relate clearly to their effects | Vertical slider matches “up = more” | Wrong mental model, mistakes |
| **Consistency** | Similar problems have similar solutions | Same gesture means “back” everywhere | Slower learning, errors |
| **Affordance (Gibson/Norman)** | Perceived possibilities for action | Handle suggests pulling | Users do not try the right action |
| **Signifiers** | Perceptible cues that indicate affordances | Label “Menu”, chevron on expandable | Mystery meat UI |

---

## Interaction design process

```blueprint-diagram
key: decision
alt: Interaction design process
title: Interaction design gate
summary: How interaction work advances only after a reviewable checkpoint against the current design state.
node: Current state
detail: Capture interface behavior, flows, and open questions as they stand.
more: Inventory screens, states, transitions, and known gaps before judging readiness to proceed.
node: Checkpoint / gate
detail: Evaluate whether the design meets visibility, feedback, and consistency criteria.
more: A bounded review against principles on this page; block progression when critical interaction gaps remain.
node: refine or escalate
detail: Return to iteration or raise unresolved conflicts for stakeholder decision.
more: Refinement updates flows and states; escalation brings decision-makers in when constraints block progress.
node: Continue flow
detail: Advance to the next interaction deliverable or implementation handoff.
fallback_ascii: |
  Interaction design process

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

---

## Navigation patterns

| Pattern | Type | When to use | Platform notes |
|---------|------|-------------|----------------|
| **Top bar / app bar** | Global | Few primary sections; branding and key actions | Web + desktop; combine with overflow on small widths |
| **Sidebar / rail** | Global | Many sections; persistent wayfinding | Desktop-first; collapse to drawer on mobile |
| **Breadcrumbs** | Local | Deep hierarchies; “where am I?” | Web; less common in native mobile |
| **Tabs** | Local | Peer views of same object or section | OS conventions for scrollable vs fixed tabs |
| **Steppers / wizard** | Local | Linear multi-step tasks | Mobile: one step per screen; clear back/save |
| **In-page anchors / “related”** | Contextual | Long pages; cross-links within task | Ensure focus management for a11y |

---

## Input patterns

| Pattern | Guidance |
|---------|----------|
| **Forms** | Progressive disclosure; inline validation; smart defaults from context |
| **Search** | Autocomplete; filters and facets for large sets; empty and no-results states |
| **Selection** | Checkbox (multi), radio (single in set), toggle (binary on/off), dropdown (many options, single), date picker (known format + keyboard fallback) |
| **Direct manipulation** | Drag-and-drop with clear handles; gestures documented and consistent |

---

## Feedback patterns

| Pattern | Use when |
|---------|----------|
| **Skeleton** | Layout known; content loading |
| **Spinner** | Short indeterminate waits |
| **Progress bar** | Determinate long operations |
| **Success / error** | Completed or failed actions — pair errors with recovery |
| **Empty states** | No data yet — explain and offer next step |
| **Transitions / micro-interactions** | Orientation (not decoration only); respect reduced motion |

---

## Form submission state diagram

```blueprint-diagram
key: state
alt: Form submission state diagram
title: Form submission flow
summary: How a form moves from user intent through governed steps to a traceable outcome.
node: Start
detail: User begins a form task with fields in an initial editable state.
more: Apply progressive disclosure and smart defaults from the input patterns on this page.
node: Core steps (see walkthrough below)
detail: Validation, submit action, and loading feedback run in sequence.
more: Pair inline validation with visible feedback; constrain submit until required fields pass validation.
node: Outcome
detail: Success confirmation or error with recovery path is shown to the user.
more: Match success and error feedback patterns; errors must offer a clear next step without inviting double submits.
fallback_ascii: |
  Form submission state diagram

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

---

## Responsive design patterns

- **Fluid grids** and relative units — reduce fixed-pixel fragility.
- **Breakpoints** — align to content and tasks, not only device brands.
- **Container queries** — component-level responsiveness where supported.
- **Responsive images** — `srcset`, sizes, art direction when needed.
- **Mobile-first vs desktop-first** — mobile-first forces priority; desktop-first suits dense pro tools — document the choice.

---

## Gesture design (expectations)

| Gesture | iOS | Android | Web |
|---------|-----|---------|-----|
| **Tap** | Primary activation | Primary activation | Click equivalent |
| **Swipe** | Back (edge), lists | Back, dismiss | Often custom — document |
| **Pinch** | Zoom | Zoom | Maps/media — browser defaults |
| **Long press** | Context menus, peek | Context, selection | Right-click parity limited |
| **Drag** | Reorder, drop | Reorder, drop | HTML5 DnD + fallbacks |

Prefer **platform HIG** defaults; when diverging, teach in UI.

---

## Optimistic UI (sequence)

```blueprint-diagram
key: sequence
alt: Optimistic UI (sequence)
title: Optimistic UI sequence
summary: How an action updates the interface immediately while a server request completes in parallel.
node: Actor / trigger
detail: The user performs an action that expects a persistent state change.
node: System step
detail: The UI reflects the expected outcome before the server confirms.
more: Show immediate feedback per feedback patterns; keep a reversible path if the request fails.
node: Outcome / handoff
detail: Confirmed success or rollback restores a truthful interface state.
more: On failure, revert optimistic changes and surface an error with recovery options.
fallback_ascii: |
  Optimistic UI (sequence)

  Actor / trigger
      |
      v
  System step
      |
      v
  Outcome / handoff
```

---

## Design system component patterns

| Component | Role |
|-----------|------|
| **Button hierarchy** | Primary / secondary / tertiary / destructive — one primary per view |
| **Modal / dialog** | Focused decisions; escape and focus trap |
| **Toast / snackbar** | Lightweight confirmation; do not block critical path |
| **Drawer / side sheet** | Filters, secondary tasks |
| **Bottom sheet** | Mobile actions and short forms |
| **Command palette** | Power users; searchable actions |

---

## Accessibility in interaction design

- **Focus management** — visible focus, logical order, return focus after modal close.
- **Keyboard navigation** — all actions reachable; no keyboard traps.
- **Screen readers** — names, roles, states; live regions for async updates.
- **Motion** — `prefers-reduced-motion` alternatives.

---

## Anti-patterns

- **Mystery meat navigation** — icons or regions without labels.
- **Modal abuse** — blocking dialogs for non-critical messages.
- **Infinite scroll** without search, filters, or “back to top” / pagination fallback.
- **Breaking the browser back button** — SPA routes must match user expectations.

---

## External references

- *About Face* — Cooper et al. (goal-directed design).
- *Don’t Make Me Think* — Steve Krug (usability and clarity).
- [Material Design](https://m3.material.io/) — patterns and motion.
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) — platform conventions.
- [Laws of UX](https://lawsofux.com/) — psychological principles in concise form.

*Keep project-specific accessibility audits in docs/product/ and remediation plans in docs/development/, not in this file.*
