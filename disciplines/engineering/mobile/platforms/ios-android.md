---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Native iOS and Android development (blueprint)

**Purpose:** High-level comparison of **native** mobile stacks — languages, UI frameworks, architecture norms, security, lifecycle, distribution, and profiling. Use for staffing, platform strategy, and onboarding; project setup lives in repo docs.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/mobile/`](../README.md). Strategy context: [`MOBILE.md`](../MOBILE.md).

---

## Overview

Native development targets **one platform** with first-class APIs and tooling. You trade **duplicate codebases** for **maximum performance**, **immediate OS feature access**, and **platform-native UX**. This guide contrasts iOS and Android along dimensions that affect architecture and delivery.

---

## Platform comparison matrix

| Dimension | iOS | Android |
|-----------|-----|---------|
| **Language** | Swift (Objective-C legacy) | Kotlin (Java interop) |
| **Declarative UI** | SwiftUI | Jetpack Compose |
| **Imperative UI** | UIKit | XML Views / View system |
| **Architecture norms** | MVVM, TCA, Coordinator | AAC + MVVM, MVI, Clean |
| **Reactive / async** | Combine, async/await, Swift concurrency | Coroutines, Flow, Rx (legacy) |
| **Unit / UI test** | XCTest, XCUITest | JUnit, Espresso, Compose UI tests |
| **CI/CD** | Xcode Cloud, Fastlane, Bitrise | Gradle, Fastlane, GitHub Actions |
| **Distribution** | App Store | Google Play |
| **Fragmentation** | Few OS versions/devices to target | Wide OEM/OS matrix |

---

## iOS ecosystem (selected)

| Technology | Role |
|------------|------|
| **SwiftUI** | Declarative UI, state, navigation |
| **UIKit** | Mature imperative UI, interop with SwiftUI |
| **Combine** | Reactive streams (bridging to async) |
| **async/await** | Structured concurrency for networking and UI |
| **Core Data / SwiftData** | Persistence frameworks |
| **Keychain** | Secure credential storage |
| **App Clips** | Lightweight on-demand app slice |
| **Widgets / Live Activities** | Home screen and Dynamic Island surfaces |

---

## Android ecosystem (selected)

| Technology | Role |
|------------|------|
| **Jetpack Compose** | Declarative UI |
| **Views** | XML + ViewBinding; interop with Compose |
| **Coroutines / Flow** | Async and cold/hot streams |
| **Room** | SQLite abstraction |
| **DataStore** | Typed preferences replacement |
| **WorkManager** | Deferrable guaranteed background work |
| **App Bundles** | Dynamic delivery, size optimization |
| **Instant Apps** | Try without full install (where supported) |
| **Widgets** | Glance / RemoteViews app surfaces |

---

## Build, sign, distribute lifecycle

```blueprint-diagram
key: linear
alt: Build, sign, distribute lifecycle
title: Native build sign distribute
summary: How native iOS and Android artifacts move from compile through signing to store-ready release packages.
node: Start
detail: Source and dependencies enter the platform-native build pipeline.
more: Xcode builds Swift and Objective-C for iOS; Gradle compiles Kotlin and Java for Android per the CI/CD row on this page.
node: Core steps (see walkthrough below)
detail: Compile, sign with platform credentials, and produce installable release artifacts.
more: iOS uses certificates and provisioning profiles; Android applies signing keys, often via Fastlane, Xcode Cloud, or Gradle CI.
node: Outcome
detail: A reviewable binary ready for App Store or Google Play submission.
more: Distribution tables on this page cover review cadence, phased rollout, and store metadata for each platform.
fallback_ascii: |
  Build, sign, distribute lifecycle

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

---

## UI framework evolution

| Aspect | Imperative (UIKit / Views) | Declarative (SwiftUI / Compose) |
|--------|----------------------------|----------------------------------|
| **State** | Manual sync to views | State drives UI |
| **Reuse** | Inheritance, composition | Composable functions / views |
| **Learning** | Long history, many patterns | Steeper for complex custom UI |
| **Interop** | N/A | `UIViewRepresentable`, `AndroidView` |

---

## Platform-specific security

| Concern | iOS | Android |
|---------|-----|---------|
| **Secure storage** | Keychain | Keystore / EncryptedSharedPreferences |
| **Biometrics** | Face ID / Touch ID (`LocalAuthentication`) | `BiometricPrompt` |
| **TLS pinning** | `URLSession` delegate / Alamofire | OkHttp `CertificatePinner` |
| **Obfuscation** | Bitcode deprecated; strip symbols | R8 / ProGuard |

---

## App lifecycle (conceptual)

**iOS — scene / app states:**

```blueprint-diagram
key: state
alt: App lifecycle (conceptual)
title: iOS scene lifecycle
summary: How iOS scene and app states govern foreground work, background limits, and state restoration.
node: Start
detail: Launch or resume brings the app into the scene state model.
more: iOS coordinates scenes and app delegates; transitions follow the conceptual states referenced in this section.
node: Core steps (see walkthrough below)
detail: Active, inactive, background, and suspended states bound work and resource use.
more: Background execution is time-limited; persist navigation and form state before suspension per guidance below.
node: Outcome
detail: A bounded lifecycle state that determines what the app may run or display.
node: Note: Android — activity / process:
detail: Cross-reference to the companion Android lifecycle diagram on this page.
more: Android uses activity and process semantics; see the following diagram for process death handling.
fallback_ascii: |
  App lifecycle (conceptual)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: Android — activity / process:
```

**Android — activity / process:**

```blueprint-diagram
key: state
alt: App lifecycle (conceptual)
title: Android activity lifecycle
summary: How Android activity and process states govern UI survival, background limits, and recovery after process death.
node: Start
detail: Launch or task resume enters the activity and process state model.
more: Activities transition through created, started, resumed, paused, stopped, and destroyed states managed by the system.
node: Core steps (see walkthrough below)
detail: Foreground, background, and low-memory callbacks reshape what the process may retain.
more: The system may reclaim background processes; navigation and form state must survive recreation without user data loss.
node: Outcome
detail: A bounded state determining whether UI and in-memory work remain available.
node: Note: process death
detail: Low-memory termination can destroy the process while the task stack survives.
more: Persist navigation and form state so users recover gracefully after the system recreates the activity.
fallback_ascii: |
  App lifecycle (conceptual)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: process death
```

Handle **process death** on Android and **suspension** on iOS — persist navigation and form state.

---

## Distribution comparison

| Topic | App Store | Google Play |
|-------|-----------|-------------|
| **Review** | Human review; variable time | Automated + policy; generally faster |
| **Guidelines** | Strict on payments, metadata, privacy | Policy on permissions, deceptive behavior |
| **Rollout** | Phased release (7-day typical) | Staged rollout by percentage |
| **Metadata** | Screenshots per device class | Similar; localized listings |

---

## Design guidelines

| Topic | Apple | Google |
|-------|-------|--------|
| **System** | Human Interface Guidelines | Material Design 3 |
| **Navigation** | Tab bar, large titles, back swipe | Predictive back, bottom bar |
| **Motion** | Subtle, purposeful | Emphasis on shared axis transitions |
| **Theming** | Semantic colors, Dynamic Type | Material color roles, shape |

---

## Performance profiling

| Goal | iOS | Android |
|------|-----|---------|
| **CPU / time** | Instruments (Time Profiler) | Android Studio Profiler (CPU) |
| **Memory** | Leaks, allocations | Memory Profiler, Heap Dump |
| **GPU / UI** | Core Animation, SwiftUI instruments | GPU rendering, Layout Inspector |
| **Energy** | Energy Impact gauge | Battery Profiler |

Measure **startup**, **frame time**, **memory peaks**, and **network** on **low-end reference devices**.

---

## External references

| Resource | URL |
|----------|-----|
| Apple Developer | https://developer.apple.com/ |
| Android Developers | https://developer.android.com/ |
| Swift | https://www.swift.org/ |
| Kotlin | https://kotlinlang.org/ |

---

*Keep project-specific mobile architecture decisions in docs/adr/ and platform documentation in docs/development/, not in this file.*
