---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Mobile platforms (blueprint)

**Purpose:** Platform-specific guidance for mobile development. Each platform guide covers setup, architecture conventions, tooling, and ecosystem-specific best practices.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/mobile/`](../README.md); project-specific platform configuration stays in **`docs/development/mobile/`**.

**Platform strategy** is a product and staffing decision, not only a technical one: native stacks optimize **fidelity and OS access**; cross-platform stacks optimize **shared velocity** at the cost of integration depth and occasional framework lag. Use the guides below to align engineering leads, mobile chapter leads, and architects before locking choices in ADRs.

```blueprint-diagram
key: decision
alt: Process flow
title: Platform strategy decision gate
summary: How teams review mobile platform choices against current constraints before committing to a stack in ADRs.
node: Process flow
detail: The governed path for evaluating and locking a mobile platform strategy.
more: Frames platform choice as a product and staffing decision, not only a technical one, before guides and ADRs are applied.
node: Current state
detail: Capture existing stacks, team skills, and product constraints.
more: Inventory native fidelity needs, cross-platform velocity goals, and integration depth against the platform guides in this index.
node: Checkpoint / gate
detail: Verify alignment among engineering leads, mobile chapter, and architects.
more: The gate confirms tradeoffs—OS access, shared velocity, framework lag—are understood before locking choices in ADRs.
node: refine or escalate
detail: Rework options or raise the decision when the gate is not met.
more: Unresolved tradeoffs return to the native or cross-platform guides, or escalate for broader staffing and product input.
node: Continue flow
detail: Proceed with the chosen platform path into project documentation.
more: Record the decision in docs/adr/ and keep platform-specific configuration under docs/development/mobile/, not in this blueprint.
fallback_ascii: |
  Process flow

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

## Platform guides

| Guide | Focus |
|-------|-------|
| [**Native iOS and Android**](ios-android.md) | Swift/Kotlin, SwiftUI/Compose vs UIKit/Views, security, lifecycle state diagrams, distribution, HIG vs Material, profiling |
| [**Cross-platform mobile**](cross-platform.md) | RN / Flutter / KMP / hybrid / PWA taxonomy, decision flowchart, framework deep dives, comparison matrix, testing and migration |

## Platform stacks (topic index)

| Platform | Focus | See |
|----------|-------|-----|
| **iOS / Swift** | SwiftUI vs UIKit, Combine/async-await, Swift Package Manager, Xcode configuration, App Clips, Widgets | [Native iOS & Android](ios-android.md) |
| **Android / Kotlin** | Jetpack Compose vs XML Views, Kotlin coroutines/Flow, Gradle, Android App Bundle, Instant Apps | [Native iOS & Android](ios-android.md) |
| **React Native** | New Architecture (Fabric, TurboModules), Metro bundler, native module bridging, Expo, CodePush | [Cross-platform](cross-platform.md) |
| **Flutter** | Widget tree, Dart isolates, platform channels, Impeller renderer, Dart packages | [Cross-platform](cross-platform.md) |
| **Kotlin Multiplatform (KMP)** | Shared module structure, expect/actual, Compose Multiplatform, Kotlin/Native interop | [Cross-platform](cross-platform.md) |

Native and cross-platform dimensions are expanded in the two guides above; this table remains a **quick map** of ecosystem topics.

**Core knowledge:** [`MOBILE.md`](../MOBILE.md) — platform strategy decision framework, architecture patterns, lifecycle, and performance.

**Bridge:** [`MOB-SDLC-PDLC-BRIDGE.md`](../MOB-SDLC-PDLC-BRIDGE.md) — how platform choices affect the lifecycle.

---

*Keep project-specific mobile architecture decisions in docs/adr/ and platform documentation in docs/development/, not in this file.*
