# Mobile engineering body of knowledge

This document maps the core concerns of **mobile engineering** — platform strategy, architecture, app lifecycle, offline-first patterns, performance, and app store management — to the blueprint ecosystem.

**How mobile engineering relates to PDLC and SDLC:** Mobile is a **platform-specific discipline** that executes within SDLC phases and adds platform-specific concerns to PDLC launch and growth. See [`MOB-SDLC-PDLC-BRIDGE.md`](MOB-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Patterns:** Navigation, offline, push notification, and deep linking patterns are in [`patterns/`](patterns/README.md).

**Platforms:** iOS, Android, and cross-platform framework guidance is in [`platforms/`](platforms/README.md).

---

## 1. Platform strategy

### Decision framework

| Factor | Native | Cross-platform (React Native / Flutter) | KMP (shared logic) | PWA |
|--------|--------|--------------------------------------|---------------------|-----|
| **Performance** | Best — direct platform APIs | Good — bridge/compiled; some overhead | Native UI + shared logic | Limited by browser sandbox |
| **UX fidelity** | Platform-native look and feel | Near-native (framework-specific widgets) | Native UI per platform | Web UX with app shell |
| **Code sharing** | None (separate iOS/Android codebases) | High (80–95% shared UI + logic) | Medium (shared business logic, native UI) | Full (one codebase) |
| **Team skillset** | iOS (Swift) + Android (Kotlin) specialists | JavaScript/TypeScript or Dart generalists | Kotlin specialists + native UI | Web developers |
| **Platform access** | Full — immediate access to new OS features | Delayed — wait for framework bindings | Full for UI, shared for logic | Limited — subset of native APIs |
| **App store** | Required | Required | Required | Optional (installable) |
| **Best fit** | Performance-critical, platform-heavy apps (camera, AR, health) | Feature-heavy business apps, startups needing speed | Large teams with shared backend/domain logic | Content-heavy, low interactivity |

### When to go native vs cross-platform

| Go native when | Go cross-platform when |
|---------------|------------------------|
| Deep OS integration (HealthKit, ARKit, Widgets) | Business logic is the majority of complexity |
| Performance is a differentiator (gaming, video, real-time) | Time-to-market matters more than platform polish |
| Small number of platforms (iOS-first or Android-first) | Team is web-skilled and platforms are web-adjacent |
| App relies on cutting-edge OS features day-one | Feature parity across platforms is a requirement |

---

## 2. Architecture patterns

| Pattern | Description | Best fit |
|---------|-------------|----------|
| **MVVM** (Model-View-ViewModel) | View observes ViewModel; ViewModel transforms Model data | SwiftUI, Jetpack Compose, data-binding scenarios |
| **MVI** (Model-View-Intent) | Unidirectional data flow; state is immutable; intents trigger state transitions | Complex state, predictable behavior, time-travel debugging |
| **Clean Architecture** | Layered — domain (entities, use cases), data (repositories), presentation (UI) | Large apps, team scaling, testability |
| **Modular / feature modules** | Features as independent modules with clear API boundaries | Large teams, independent feature development and testing |
| **Coordinator / Router** | Centralized navigation logic separated from view controllers | Complex navigation flows, deep linking |

### Dependency injection

| Approach | Platform | Examples |
|----------|----------|----------|
| **Constructor injection** | All | Manual DI — pass dependencies through initializers |
| **DI container** | Android (Kotlin) | Hilt/Dagger, Koin |
| **Environment / property wrapper** | iOS (Swift) | SwiftUI `@Environment`, custom property wrappers |
| **Service locator** | Cross-platform | Simple registration/resolution; less compile-time safety |

---

## 3. App lifecycle

### States

| State | iOS | Android | Considerations |
|-------|-----|---------|---------------|
| **Not running** | Terminated | Process killed | Cold start performance; state restoration |
| **Foreground active** | Active | Resumed | Full functionality; user interaction |
| **Foreground inactive** | Inactive | Paused (brief) | Incoming call, notification, app switcher |
| **Background** | Background | Stopped/Background | Limited execution time (iOS ~30s); background tasks, location, audio |
| **Suspended** | Suspended | Cached | No code execution; may be killed for memory |

### State preservation

| Strategy | Description |
|----------|-------------|
| **Instance state** | Save/restore transient UI state across configuration changes (Android `onSaveInstanceState`, iOS state restoration) |
| **Persistent storage** | Core Data, Room, SQLite, encrypted shared preferences for durable data |
| **Navigation state** | Restore navigation stack so users return to where they left off |
| **Deferred deep links** | Handle deep links received while app was not running |

---

## 4. Offline-first patterns

| Pattern | Description | Complexity |
|---------|-------------|------------|
| **Cache first** | Read from local cache; update from network in background | Low |
| **Write-through** | Write to local and remote simultaneously | Medium |
| **Write-behind / queue** | Queue writes locally; sync when network available | Medium–high |
| **Conflict resolution** | Last-write-wins, merge, or manual conflict resolution | High |
| **Sync protocol** | Bidirectional sync with server (CRDTs, operational transform) | High |

### Local storage options

| Technology | Best fit | Platform |
|------------|----------|----------|
| **SQLite / Room / Core Data** | Structured relational data; complex queries | Native |
| **Realm** | Object-oriented data; real-time sync | Cross-platform |
| **MMKV / SharedPreferences / UserDefaults** | Key-value settings, small data | Platform-specific |
| **File system** | Documents, images, cached media | All |
| **Encrypted storage** (Keychain / Keystore) | Tokens, credentials, sensitive data | Platform-specific |

---

## 5. Performance

### Startup time

| Phase | Optimization |
|-------|-------------|
| **Pre-main / process start** | Reduce dylib/dex count; minimize static initializers |
| **Main / application init** | Defer non-essential initialization; lazy services |
| **First frame** | Optimize layout; avoid heavy computation on main thread; use placeholder/skeleton UI |

### Runtime performance

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Frame rate** | 60 fps (16.6 ms/frame) or 120 fps on ProMotion/high-refresh devices | Instruments (iOS), GPU Profiler (Android), React Native Perf Monitor |
| **Memory** | Stay within OS limits; no leaks; release caches on memory warning | Xcode Memory Graph, Android Profiler, LeakCanary |
| **Battery** | Minimize background activity, location usage, wake locks | Battery historian, Xcode Energy Impact |
| **Network efficiency** | Batch requests, compress payloads, cache responses, respect metered connections | Charles Proxy, Network Link Conditioner |

---

## 6. App store lifecycle

| Stage | Activities | Considerations |
|-------|-----------|---------------|
| **Submission** | Build signing, metadata, screenshots, privacy manifest, compliance declarations | Automate with Fastlane; maintain screenshot generation |
| **Review** | Apple/Google review for guidelines compliance | Know rejection patterns; test edge cases; respond promptly |
| **Release** | Immediate, phased (iOS 1–7 days), staged rollout (Android percentage), timed release | Monitor crash rates during rollout; auto-halt on anomalies |
| **Updates** | Forced updates (minimum version), soft prompts, silent updates (CodePush for RN) | Balance user disruption with security/compatibility needs |
| **Hotfixes** | Expedited review (Apple), fast-track rollout (Google), OTA for JS bundles | Have a tested hotfix pipeline ready before you need it |
| **Ratings** | In-app review prompts (SKStoreReviewController, Google In-App Review API) | Prompt at moments of success; respect rate limits; never gate features |

---

## 7. Push notifications

| Concern | Guidance |
|---------|----------|
| **Token management** | Register for remote notifications; store tokens server-side; handle token refresh |
| **Notification channels** (Android) | Categorize notifications; let users control per-channel |
| **Rich notifications** | Images, action buttons, custom UI (Notification Content Extension / BigPictureStyle) |
| **Silent / background push** | Trigger background data sync without user-visible notification |
| **Deep link from notification** | Navigate to correct screen on tap; handle both foreground and cold-start |
| **Permission strategy** | Defer push permission request until value is clear to user; explain before system prompt |

---

## 8. Competencies

| Competency | Description |
|------------|-------------|
| **Platform expertise** | Deep knowledge of iOS (Swift, UIKit/SwiftUI) or Android (Kotlin, Jetpack Compose) or cross-platform framework |
| **Architecture design** | Applying MVVM/MVI/Clean Architecture patterns; modularization; dependency injection |
| **Offline and sync** | Designing offline-first data strategies; conflict resolution; local persistence |
| **Performance engineering** | Startup optimization, frame rate profiling, memory management, battery efficiency |
| **App store management** | Submission automation, review guidelines, rollout strategies, hotfix pipelines |
| **Mobile security** | Secure storage, certificate pinning, biometrics, transport security, reverse engineering protection |
| **Testing** | Unit, integration, UI testing; device farm management; snapshot/screenshot testing |
| **CI/CD for mobile** | Build signing, simulator/device testing in CI, distribution (TestFlight, Firebase App Distribution) |

---

## 9. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | iOS/macOS design and behavior guidelines |
| Material Design | https://m3.material.io/ | Android design system and component guidelines |
| OWASP Mobile Top 10 | https://owasp.org/www-project-mobile-top-10/ | Mobile-specific security risks |
| Fastlane | https://fastlane.tools/ | Mobile CI/CD automation |
| React Native | https://reactnative.dev/ | Cross-platform framework (JavaScript/TypeScript) |
| Flutter | https://flutter.dev/ | Cross-platform framework (Dart) |
| Kotlin Multiplatform | https://kotlinlang.org/docs/multiplatform.html | Shared Kotlin logic across platforms |
| App Store Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ | Apple submission requirements |

---

*Keep project-specific mobile documentation in `docs/development/mobile/` and architecture decisions in `docs/adr/`, not in this file.*
