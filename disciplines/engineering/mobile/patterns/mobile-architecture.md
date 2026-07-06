---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Mobile application architecture (blueprint)

**Purpose:** Project-agnostic patterns for structuring mobile codebases — separation of concerns, data flow, navigation, dependency injection, modularization, and testing. Use this when choosing or evolving an architecture before codifying decisions in ADRs.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/mobile/`](../README.md). Core mobile concerns are summarized in [`MOBILE.md`](../MOBILE.md).

---

## Overview

Mobile apps benefit from architectures that isolate **UI** from **domain rules** and **data access**. Constraints differ from server or web front ends: tight main-thread budgets, process death, configuration changes, and platform-specific UI lifecycles. Good architectures trade **testability** and **team scalability** against **complexity** — not every app needs VIPER or full Clean Architecture.

---

## Architecture pattern comparison

| Pattern | Layers / roles | Data flow | Testability | Complexity |
|---------|----------------|-----------|-------------|------------|
| **MVC** | Model, View, Controller | View ↔ Controller → Model; often bidirectional | Low–medium (Controller tends to grow) | Low |
| **MVP** | Model, View, Presenter | View → Presenter → Model; Presenter updates View via interface | Medium | Medium |
| **MVVM** | Model, View, ViewModel | View observes ViewModel; ViewModel exposes state/commands | High (ViewModel unit-testable) | Medium |
| **MVI / Redux** | Single state, reducers, intents/actions | Unidirectional: Intent → reduce → new State → View | High (pure reducers) | Medium–high |
| **VIPER** | View, Interactor, Presenter, Entity, Router | Strict boundaries; router owns navigation | High (small types) | High |
| **Clean Architecture** | Presentation, Domain, Data | Inward dependencies; use cases orchestrate | High (domain isolated) | High |
| **TCA** (The Composable Architecture) | State, Action, Reducer, Environment, Effects | Unidirectional; composable reducers (Swift) | High | Medium–high |

---

## MVVM data flow

```blueprint-diagram
key: swimlane
alt: MVVM data flow
title: MVVM View–ViewModel flow
summary: How the View observes ViewModel state and commands while a review lane keeps UI logic testable and bounded.
node: MVVM data flow
detail: Entry framing View, ViewModel, and Model roles from the comparison table.
more: View observes ViewModel; ViewModel exposes state and commands while domain rules stay outside the UI layer.
node: Lane A
detail: Primary path from user intent through ViewModel to updated UI state.
more: View forwards events to ViewModel; ViewModel fetches or transforms data via Model abstractions without platform UI types.
node: handoff
detail: State and commands cross the View–ViewModel boundary through observable contracts.
more: Data binding, publishers, or reactive streams keep the View declarative while ViewModel owns presentation logic.
node: shared outcome
detail: Rendered UI reflects current state with predictable, unit-testable updates.
node: Lane B
detail: Parallel lane inspecting whether presentation logic stays in ViewModel.
node: inspect / adapt
detail: Detect massive controllers, god ViewModels, or leaked networking in UI.
more: Anti-patterns on this page—massive View Controller, god ViewModel—signal when boundaries need tightening before merge.
node: feedback
detail: Refined contracts and slimmer ViewModels feed back into the architecture.
fallback_ascii: |
  MVVM data flow

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

---

## Clean Architecture: layers and dependency rule

Dependencies point **inward**: outer layers depend on inner abstractions, never the reverse.

```blueprint-diagram
key: swimlane
alt: Clean Architecture: layers and dependency rule
title: Clean Architecture dependency rule
summary: How presentation and data layers depend inward on domain use cases without reversing the dependency direction.
node: Clean Architecture: layers and dependency rule
detail: Entry framing Presentation, Domain, and Data layers from the comparison table.
more: Dependencies point inward: outer layers depend on inner abstractions, never the reverse.
node: Lane A
detail: Primary path from UI through use cases to repositories and entities.
more: Presentation calls domain use cases; use cases orchestrate repositories while entities hold core business rules.
node: handoff
detail: Layer boundaries exchange data through interfaces, not concrete platform types.
more: DTO mapping and repository facades keep transport and persistence details outside domain logic.
node: shared outcome
detail: Testable domain isolated from UI lifecycles and data-source specifics.
node: Lane B
detail: Parallel lane verifying dependency direction as features grow.
node: inspect / adapt
detail: Detect platform coupling, skipped use cases, or repositories leaking into UI.
more: Anti-patterns—tight platform coupling in domain, no separation of concerns—surface when inner layers import outer ones.
node: feedback
detail: Adjusted module boundaries and ports feed back into layer design.
fallback_ascii: |
  Clean Architecture: layers and dependency rule

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

---

## Navigation patterns

| Pattern | Description | iOS | Android |
|---------|-------------|-----|---------|
| **Stack** | Hierarchical push/pop | `UINavigationController`, SwiftUI `NavigationStack` | Fragment/Compose back stack, `NavController` |
| **Tab** | Parallel top-level sections | `UITabBarController`, `TabView` | `BottomNavigation`, `TabRow` |
| **Drawer** | Side menu for global nav | Custom / third-party | `NavigationDrawer`, modal sheet patterns |
| **Modal** | Interruptive flows | `sheet`, `fullScreenCover`, `present` | `Dialog`, bottom sheet, `ModalBottomSheet` |
| **Deep linking** | URL → screen | Universal Links, `onOpenURL` | App Links, intent filters, Compose deep links |
| **Universal / app links** | HTTPS opens app | Associated Domains, AASA file | Digital Asset Links, `assetlinks.json` |

---

## Dependency injection on mobile

| Approach | Platform | Strengths | Trade-offs |
|----------|----------|-----------|------------|
| **Dagger / Hilt** | Android | Compile-time graph, scopes, test modules | Learning curve, codegen |
| **Swinject** | iOS | Lightweight container, storyboard-free | Runtime resolution; less compile safety |
| **GetIt** | Flutter | Simple service locator, fast to adopt | Locator anti-pattern if abused |
| **Manual DI** | All | No magic, explicit constructors | Verbose in large apps; easy to forget wiring |

Prefer **constructor injection** at feature boundaries; use containers for app-wide graphs and test doubles.

---

## Modularization strategies

| Strategy | Description | When to use |
|----------|-------------|-------------|
| **Feature modules** | Vertical slices (auth, checkout) with public APIs | Scaling teams, feature flags |
| **Layer modules** | `domain`, `data`, `ui` libraries | Enforcing Clean boundaries |
| **Dynamic feature modules** | On-demand delivery (Play Feature Delivery) | Large APK size, optional features |

```blueprint-diagram
key: linear
alt: Modularization strategies
title: Mobile modularization lifecycle
summary: How teams choose feature, layer, or dynamic modules and align public APIs before scaling delivery.
node: Modularization strategies
detail: Entry to feature slices, layer libraries, and on-demand delivery options above.
more: Feature modules isolate vertical slices; layer modules enforce domain, data, and ui boundaries; dynamic modules defer optional APK content.
node: Start
detail: Assess team scale, APK size, and boundary enforcement needs before splitting.
more: Feature modules suit scaling teams and flags; layer modules enforce Clean boundaries; Play Feature Delivery addresses large optional features.
node: Core steps (see walkthrough below)
detail: Define module public APIs, dependency direction, and build graph wiring.
more: Vertical slices expose narrow interfaces; layer libraries prevent UI from reaching data sources directly across module edges.
node: Outcome
detail: Reviewable modules that scale teams without unbounded coupling across features.
fallback_ascii: |
  Modularization strategies

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

---

## API layer patterns

| Concern | Pattern | Notes |
|---------|---------|-------|
| **Data access** | Repository | Single facade over remote + local; hides sync details |
| **Business rules** | Use cases / interactors | One responsibility; orchestrate repositories |
| **Transport** | DTO mapping | Map API DTOs ↔ domain entities at boundaries |
| **Errors** | Sealed / typed errors, `Result` types | Map HTTP and parsing failures to domain errors |
| **Retries** | Exponential backoff, idempotency keys | Respect `Retry-After`; avoid retry storms |

---

## Data layer patterns

| Concern | Typical choices |
|---------|-----------------|
| **Structured persistence** | Room (Android), Core Data / SwiftData (iOS), Realm |
| **Key-value / preferences** | DataStore, UserDefaults, MMKV |
| **In-memory cache** | LRU by key; tie to lifecycle or scope |
| **Sync** | Outbox table, version vectors, ETag / cursor pagination |

---

## Testing architecture

| Layer | Approach |
|-------|----------|
| **ViewModel / Presenter** | Unit tests with fake repositories and schedulers |
| **Integration** | In-memory DB, mock server (e.g. WireMock, MockWebServer), fakes implementing ports |
| **UI** | Page Object / Robot pattern; stable accessibility IDs; hermetic where possible |

---

## Anti-patterns

| Anti-pattern | Why it hurts |
|--------------|--------------|
| **Massive View Controller / Activity** | Untestable, merge conflicts, hidden side effects |
| **Tight platform coupling in domain** | Blocks reuse, testing, and future platform moves |
| **God ViewModel** | Hundreds of properties and methods; same as god class |
| **No separation of concerns** | UI, networking, and persistence interleaved |

---

## External references

| Resource | URL | Notes |
|----------|-----|-------|
| Android Architecture Guide | https://developer.android.com/topic/architecture | Official guidance for layers, UI state, navigation |
| iOS App Architecture (objc.io) | https://www.objc.io/books/app-architecture/ | Patterns in Swift context |
| *Clean Architecture* | Robert C. Martin — book | Dependency rule, entities, use cases |

---

*Keep project-specific mobile architecture decisions in docs/adr/ and platform documentation in docs/development/, not in this file.*
