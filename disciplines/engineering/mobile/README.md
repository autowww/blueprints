# Mobile Engineering

Reusable, **project-agnostic** blueprint for **Mobile Engineering** — the discipline of building performant, reliable mobile experiences across platforms and devices.

Mobile Engineering answers **"how do we build performant, reliable mobile experiences across platforms and devices?"** — a platform-specific discipline that spans the entire SDLC and connects to PDLC through app store lifecycle, user engagement, and mobile-specific metrics.

| Document | Purpose |
|----------|---------|
| [**MOBILE.md**](MOBILE.md) | Platform strategy (native/cross-platform), architecture patterns, app lifecycle, performance, offline-first, deep linking, competencies |
| [**MOB-SDLC-PDLC-BRIDGE.md**](MOB-SDLC-PDLC-BRIDGE.md) | How Mobile Engineering maps across SDLC phases A–F and PDLC phases P1–P6 — emphasis on Build, Release, and Grow |
| [**patterns/**](patterns/README.md) | Deep guides: navigation patterns, offline-first, push notifications, deep linking, background processing |
| [**platforms/**](platforms/README.md) | Platform-specific guidance: iOS/Swift, Android/Kotlin, React Native, Flutter, KMP |

## Relationship to other packages

| Package | How Mobile Engineering relates |
|---------|-------------------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | Mobile delivery follows SDLC phases but adds platform-specific gates — app store review, staged rollouts, hotfix constraints. Release (F) is more complex than web due to binary distribution. |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC P4 (Launch) includes app store submission and review. P5 (Grow) involves mobile-specific engagement (push notifications, deep links, in-app messaging). P6 (Sunset) must handle installed base with no forced updates. |
| [`blueprints/disciplines/product/ux-design/`](../../product/ux-design/README.md) | Mobile UX has distinct patterns (gestures, bottom sheets, haptics, edge swipes). Apple HIG and Material Design provide platform-specific design guidance. |
| [`blueprints/disciplines/engineering/frontend/`](../frontend/README.md) | Cross-platform frameworks (React Native) share concepts with web frontend. PWAs bridge web and mobile. Code sharing strategies connect the two disciplines. |
| [`blueprints/disciplines/engineering/software-architecture/`](../software-architecture/README.md) | Architecture decisions (monolith vs modular app, BFF for mobile, API versioning) shape mobile implementation. Offline-first architecture is a mobile-specific concern. |
| [`blueprints/disciplines/engineering/testing/`](../testing/README.md) | Mobile testing adds device fragmentation, screenshot testing, app store compliance testing, and device farm management. |
| [`blueprints/disciplines/security/`](../../security/README.md) | Mobile security includes certificate pinning, secure storage (Keychain/Keystore), biometric authentication, jailbreak/root detection, and app transport security. |
| [`blueprints/disciplines/engineering/devops/`](../devops/README.md) | Mobile CI/CD includes build signing, device farm integration, app store deployment automation (Fastlane), OTA updates (CodePush). |

## Scope

This package covers **Mobile Engineering as a discipline** — not just framework tutorials. It includes:

- **Platform strategy** — native (iOS/Android) vs cross-platform (React Native, Flutter, KMP) decision framework
- **Architecture** — MVVM, MVI, Clean Architecture, modular apps, feature modules, dependency injection
- **App lifecycle** — launch, backgrounding, termination, state restoration, memory warnings
- **Offline-first** — local storage, data sync, conflict resolution, optimistic updates
- **Navigation** — stack, tab, drawer, deep linking, universal links, deferred deep links
- **Push notifications** — APNs/FCM, notification channels, rich notifications, silent pushes
- **App store lifecycle** — submission, review guidelines, staged rollouts, phased releases, hotfixes
- **Performance** — startup time, frame rate, memory, battery, network efficiency
- **Device fragmentation** — screen sizes, OS versions, hardware capabilities, manufacturer skins
- **Mobile security** — certificate pinning, secure storage, biometrics, app transport security
- **Mobile testing** — device farms, screenshot/snapshot testing, UI testing, performance profiling

Reference bodies of knowledge: Apple Human Interface Guidelines, Material Design for Android, OWASP Mobile Top 10, mobile-specific DORA metrics.

---

*Keep project-specific mobile configuration in `docs/development/mobile/` and architecture decisions in `docs/adr/`, not in this file.*
