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
alt: Diagram
```

---

## Clean Architecture: layers and dependency rule

Dependencies point **inward**: outer layers depend on inner abstractions, never the reverse.

```blueprint-diagram
key: swimlane
alt: Diagram
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
alt: Diagram
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
