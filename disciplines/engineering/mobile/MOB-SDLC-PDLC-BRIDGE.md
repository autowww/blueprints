---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Mobile Engineering ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **Mobile Engineering** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Mobile** — "Does the mobile experience **perform well across platforms and devices**?"

Mobile engineering adds platform-specific constraints to standard SDLC delivery — binary distribution, app store review, device fragmentation — and connects to PDLC through mobile-specific engagement and distribution channels.

**Canonical sources:** [`MOBILE.md`](MOBILE.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Comparison table

| Dimension | Mobile Engineering | SDLC | PDLC |
|-----------|-------------------|------|------|
| **Core question** | Does the mobile experience perform well across platforms and devices? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | Native/cross-platform development, offline-first, push notifications, app store lifecycle, device fragmentation, mobile security | Requirements → design → implementation → verification → release (**A**–**F**) | Problem discovery → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | Mobile / platform engineers | Delivery team | Product manager / product trio |
| **Success metric** | Crash-free rate, app startup time, ANR rate, app store rating, install/uninstall ratio | Velocity, defect escape rate, CI/CD pass rate | Adoption, retention, revenue, NPS |
| **Key artifacts** | Signed binaries, Fastlane config, device test results, app store metadata | Specs, code, tests, release notes | Research, strategy, metrics |
| **Risk focus** | Device fragmentation, OS updates, store rejection, offline data loss, battery/memory | Technical correctness | Market and outcome risk |

---

## Mobile across the lifecycle

| Phase | Mobile role | Key activities | Outputs |
|-------|------------|----------------|---------|
| **P1–P2** | **Platform evaluator** | Assess mobile feasibility; prototype on target devices; evaluate native vs cross-platform | Platform recommendation, device matrix, prototype |
| **P3** | **Technical advisor** | Platform strategy (native/cross-platform), minimum OS version, offline requirements | Platform ADR, device support matrix, offline strategy |
| **A Discover** | **Mobile architect** | Framework selection, architecture pattern (MVVM/MVI/Clean), navigation approach, CI/CD pipeline design | Architecture doc, CI/CD pipeline plan |
| **B Specify** | **Feature specifier** | Map specs to mobile patterns; identify platform-specific behaviors; define deep link schema | Mobile-specific acceptance criteria, deep link contract |
| **C Design** | **Platform builder** | Set up project structure, DI, navigation, local storage, networking layer, design system integration | Project scaffold, core modules, component library |
| **D Build** | **Feature implementer** | Build features per platform; implement offline sync, push notifications, deep linking | Feature code, platform-specific adaptations |
| **E Verify** | **Device tester** | Device farm testing, screenshot/snapshot tests, performance profiling, accessibility, security scan | Device test results, performance baselines, security report |
| **F Release** | **Release engineer** | Code signing, app store submission, staged rollout, feature flags, OTA updates | Signed binaries, store listings, rollout config |
| **P4 Launch** | **Store manager** | App store optimization (ASO), screenshot updates, review responses, initial analytics setup | Store listing, analytics dashboards |
| **P5 Grow** | **Engagement engineer** | Push notification campaigns, deep link attribution, A/B testing, performance optimization | Engagement metrics, experiment results, performance improvements |
| **P6 Sunset** | **Migration manager** | Forced update to migration path, data export, app delisting, support wind-down | Migration guide, delisting plan |

---

## Mobile-specific lifecycle concerns

### Release complexity (vs web)

| Concern | Web | Mobile |
|---------|-----|--------|
| **Distribution** | Deploy to CDN/server | Submit to app stores; review process (1–7 days) |
| **Rollback** | Instant redeploy | Cannot force uninstall; expedited review for hotfix |
| **Update adoption** | Immediate (next page load) | User-controlled (or OS auto-update); installed base fragmentation |
| **Feature flags** | Simple (server-controlled) | Important for decoupling release from rollout; limited by offline |
| **Hotfixes** | Redeploy in minutes | OTA for JS bundles; native hotfixes require new store submission |

### Device fragmentation

| Dimension | Strategy |
|-----------|----------|
| **Screen sizes** | Responsive layouts, adaptive components, device-class detection |
| **OS versions** | Define minimum supported version; use compatibility libraries; test on oldest supported |
| **Hardware capabilities** | Feature detection (camera, NFC, biometrics); graceful degradation for missing hardware |
| **Manufacturer variants** (Android) | Test on popular OEM devices; handle manufacturer-specific behaviors |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Web app in a shell** | Cross-platform app that ignores platform conventions — feels foreign on both platforms | Follow platform HIG; use native navigation patterns; respect platform gestures |
| **Ignoring the installed base** | Assuming all users are on latest version; breaking backward compatibility | API versioning; gradual migration; minimum version enforcement with user communication |
| **Always-online assumption** | App crashes or shows empty screens without network | Offline-first with cached data and queued writes; clear offline state indicators |
| **Permission spam** | Requesting all permissions at install/first launch | Request permissions contextually when the feature that needs them is first used |
| **Manual release** | Code signing, screenshots, metadata updated by hand | Fastlane + CI/CD for automated builds, signing, screenshots, and submission |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`MOBILE.md`](MOBILE.md) | Platform strategy, architecture, app lifecycle, performance, app store management |
| [`patterns/README.md`](patterns/README.md) | Navigation, offline, push notification, deep linking patterns |
| [`platforms/README.md`](platforms/README.md) | iOS, Android, React Native, Flutter, KMP specifics |
| [`UX-DESIGN.md`](../../product/ux-design/UX-DESIGN.md) | Interaction design, design systems — mobile-specific UX patterns |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6 |
| [`SEC-SDLC-PDLC-BRIDGE.md`](../../security/SEC-SDLC-PDLC-BRIDGE.md) | Mobile security — certificate pinning, secure storage, biometrics |
