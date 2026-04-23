---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Cross-platform mobile development (blueprint)

**Purpose:** Compare **single-codebase** approaches — React Native, Flutter, Kotlin Multiplatform (KMP), hybrid shells, and PWAs — for sharing logic and UI across iOS and Android (and sometimes web/desktop).

**Audience:** Teams adopting [`blueprints/disciplines/engineering/mobile/`](../README.md). Decision context: [`MOBILE.md`](../MOBILE.md) § platform strategy.

---

## Overview

Cross-platform stacks trade **some platform fidelity and integration latency** for **velocity** and **shared ownership**. The right choice depends on performance needs, team skills, native surface area (camera, Bluetooth, widgets), and long-term maintenance appetite.

---

## Approach taxonomy

| Approach | Code sharing (typical) | Performance | Native access | Team skills |
|----------|-------------------------|-------------|---------------|-------------|
| **Native** (Swift / Kotlin) | 0% UI+logic across platforms | Best | Full | Platform specialists |
| **React Native** | High UI + logic (JS/TS) | Good; bridge cost shrinking (new arch) | Modules + community libs | Web / React |
| **Flutter** | High UI + logic (Dart) | Good; Skia/Impeller | Plugins + FFI | Dart / widget mindset |
| **KMP** | Logic high; UI often native | Native UI perf | expect/actual boundaries | Kotlin + native UI |
| **Hybrid** (Ionic / Capacitor) | Very high (web in WebView) | Variable | Plugins | Web |
| **PWA** | Full (web) | Browser-limited | Web APIs | Web |

---

## Decision flowchart

```blueprint-diagram
key: decision
alt: Diagram
```

---

## React Native deep dive

| Topic | Detail |
|-------|--------|
| **Architecture** | JS thread + native UI; **New Architecture**: Fabric (UI), TurboModules, JSI for tighter native sync |
| **Strengths** | Huge ecosystem; reuse React patterns; OTA-friendly JS bundles (where policy allows) |
| **Limitations** | Native module lag for bleeding-edge APIs; upgrade churn |
| **Ecosystem** | Expo (managed workflow), React Navigation, Redux/Zustand/Jotai |

---

## Flutter deep dive

| Topic | Detail |
|-------|--------|
| **Architecture** | Dart VM; **widget tree** + `Element`/`RenderObject`; **Skia / Impeller** rendering |
| **Strengths** | Consistent UI across platforms; strong tooling; compile to multiple targets |
| **Limitations** | Dart hiring pool smaller in some regions; platform views have integration cost |
| **Ecosystem** | Riverpod / Bloc, GoRouter, freezed / json_serializable |

---

## Kotlin Multiplatform (KMP) deep dive

| Topic | Detail |
|-------|--------|
| **Shared logic** | `commonMain` domain, networking, persistence abstractions |
| **UI** | **Compose Multiplatform** (shared UI experiment) or **native** SwiftUI/Compose per platform |
| **iOS interop** | Kotlin/Native framework; Swift calls into shared Kotlin |
| **Maturity** | Strong for logic sharing; UI sharing evolving |

---

## Comparison matrix: React Native vs Flutter vs KMP

| Dimension | React Native | Flutter | KMP |
|-----------|--------------|---------|-----|
| **Language** | JavaScript / TypeScript | Dart | Kotlin (+ Swift for iOS UI) |
| **Rendering** | Native views via bridge/JSI | Own engine | Native (typical) |
| **Performance** | Good; profile lists/images | Good; large trees need care | Native UI tier |
| **Native access** | Modules | Platform channels / FFI | Direct in platform code |
| **Community** | Very large | Large | Growing |
| **Enterprise** | Wide adoption | Wide adoption | Common in Kotlin shops |
| **Learning curve** | Low if React-familiar | Medium (widgets, immutability) | Medium–high (multi-target) |
| **Hiring** | Easier (web overlap) | Moderate | Kotlin + mobile |

---

## Code sharing strategies

| Share | Often shared | Often platform-specific |
|-------|--------------|-------------------------|
| **Domain / use cases** | Yes | — |
| **API clients / DTO mapping** | Yes (with expect/actual for storage) | Secure enclave access |
| **Navigation** | Sometimes (RN/Flutter) | Deep OS integrations |
| **UI** | RN/Flutter yes; KMP optional | HIG / Material nuances |

---

## Cross-platform architecture layers

```blueprint-diagram
key: swimlane
alt: Diagram
```

---

## Testing cross-platform

| Layer | Approach |
|-------|----------|
| **Shared logic** | Jest / Dart test / Kotlin common tests |
| **Platform** | XCTest, Espresso, Maestro / Detox for E2E |
| **E2E** | One suite per framework; device farms for both OSes |

---

## Migration paths

| Direction | Guidance |
|-----------|----------|
| **Native → cross-platform** | Pilot one feature; shared API boundary; avoid big-bang rewrite |
| **Cross-platform → native** | When OS-specific UX or performance dominates cost of dual teams |

---

## Anti-patterns

| Anti-pattern | Why |
|--------------|-----|
| **“Write once, debug everywhere”** | Ignores real device/OS matrix |
| **Ignoring platform conventions** | Rejection risk and poor reviews |
| **Overusing bridges** | Jank and hard-to-debug threading |
| **Shared UI that ignores HIG/Material** | Feels “wrong” on both platforms |

---

## External references

| Resource | URL |
|----------|-----|
| React Native | https://reactnative.dev/ |
| Flutter | https://flutter.dev/ |
| Kotlin Multiplatform | https://kotlinlang.org/docs/multiplatform.html |
| Expo | https://docs.expo.dev/ |
| *Flutter in Action* | Book (Eric Windmill) — practical Flutter architecture |

---

*Keep project-specific mobile architecture decisions in docs/adr/ and platform documentation in docs/development/, not in this file.*
