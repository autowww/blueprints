---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Software engineering body of knowledge

This document maps the core concerns of **software engineering** — the craft foundations that precede specialized engineering disciplines — to the blueprint ecosystem.

**How software engineering relates to PDLC and SDLC:** SE is **embedded in every SDLC phase** and enables PDLC learning loops through prototypes, measurements, and sustainable change. See [`SE-SDLC-PDLC-BRIDGE.md`](SE-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Paradigms:** Deeper paradigm guides are indexed in [`paradigms/`](paradigms/README.md).

**Patterns:** Deeper pattern catalogs are indexed in [`patterns/`](patterns/README.md).

---

## 1. Programming paradigms

| Paradigm | Core principles | Strengths | Best fit |
|----------|-----------------|-----------|----------|
| **Object-oriented (OOP)** | Encapsulation, abstraction, polymorphism, messaging between objects; identity + state + behavior | Rich domain modeling; boundaries around invariants; replaceable implementations behind interfaces | Business domains with stable nouns; UI components; plugin architectures |
| **Functional (FP)** | Pure functions, immutability, explicit effects, composition, referential transparency | Easier reasoning about concurrency; localized testing; algebraic data + transformations | Data pipelines, compilers, financial calculations, parallel maps/reductions |
| **Reactive** | Data flows over time; declarative composition of streams; backpressure and cancellation as first-class | UI and network-driven systems; combining many async sources; resilience to bursty load | Event-heavy services, real-time dashboards, stream processing edges |
| **Procedural** | Sequencing, procedures/subroutines, structured control flow, minimal abstraction ceremony | Low cognitive overhead; predictable resource use; straightforward tooling | Scripts, firmware bring-up, performance kernels, simple batch jobs |

**Composition note:** Production systems are usually **multi-paradigm** — e.g., FP core for transformations with OOP boundaries for IO and frameworks. Prefer **one dominant style per module** for readability.

---

## 2. Data structures and algorithms

### Fundamental data structures

| Structure | Typical operations | Time notes (big-O, typical) | When to choose |
|-----------|-------------------|----------------------------|----------------|
| **Array / vector** | Index access, contiguous memory | O(1) access; O(n) insert/delete in middle | Known size or amortized growth; cache-friendly scans |
| **Linked list** | Insert/delete at iterator | O(1) splice if node known; O(n) search | Frequent middle inserts with stable iterators; avoid for cache-sensitive scans |
| **Stack / queue / deque** | LIFO / FIFO / both ends | O(1) push/pop (amortized for dynamic arrays) | DFS, BFS, schedulers, undo stacks, work queues |
| **Hash map / dictionary** | Key → value | O(1) average lookup; O(n) worst case (poor hash / attack) | Membership, dedup, memoization, indexes |
| **Tree (BST, balanced)** | Ordered keys, range queries | O(log n) search/insert in balanced trees | Ordering + moderate mutation; avoid unguarded BST on adversarial input |
| **Heap (priority queue)** | Min/max retrieval | O(log n) push/pop; O(1) peek | Schedulers, top-K, event ordering |
| **Trie / prefix tree** | Prefix search | O(key length) operations | Autocomplete, IP routing tables, lexical structures |
| **Graph (adjacency list)** | Traverse, shortest paths | O(V+E) BFS/DFS; varies for shortest path algo | Dependencies, networks, state machines |
| **Bloom filter** | Probabilistic membership | O(k) per query; space-efficient | Cache negatives, pre-filters (accept false positives) |
| **Bitmap / bitset** | Dense sets of integers | Very compact; word-parallel ops | Feature flags at scale, inverted indexes |

### Algorithm complexity and selection

| Concern | What to measure | Rule of thumb |
|---------|-----------------|---------------|
| **Asymptotic class** | How cost grows with n | Prefer O(n) or O(n log n) for large n unless constants dominate (small fixed n) |
| **Constants and memory** | Cache lines, allocations, GC pressure | Hot loops: prefer contiguous memory, fewer pointers, less allocation |
| **Stability** | Equal keys keep order | Important for multi-key sorts and reproducible pipelines |
| **Determinism** | Same input → same output path | Needed for tests, replay, and some compliance regimes |
| **Amortized vs worst** | Dynamic arrays, hash tables | Document worst-case hazards (rehash storms, adversarial keys) |

**When complexity dominates:** Profile first for **measured** hotspots; optimize the **inner loop** or **cross-service chatter**, not speculative abstractions.

---

## 3. Design patterns

### GoF — creational

| Pattern | Intent | When to use | Watch-outs |
|---------|--------|-------------|------------|
| **Abstract Factory** | Create families of related objects without concrete classes | Swappable UI/toolkits, multi-vendor integrations | Factory explosion; test doubles multiply |
| **Builder** | Construct complex objects step-by-step | Many optional fields; readable construction for nested configs | Not every POJO needs a builder |
| **Factory Method** | Let subclasses decide which class to instantiate | Framework hooks; plugin points | Indirection cost; discoverability |
| **Prototype** | Clone exemplars instead of subclassing | Expensive construction; runtime variation | Deep copy vs shallow copy bugs |
| **Singleton** | One instance globally | *(Rarely justified)* — prefer DI and explicit scopes | Hidden dependencies; test pain; concurrency |

### GoF — structural

| Pattern | Intent | When to use | Watch-outs |
|---------|--------|-------------|------------|
| **Adapter** | Make an interface usable where another is expected | Legacy/SDK boundaries | Leaky abstractions if adapter does too much |
| **Bridge** | Decouple abstraction from implementation | Multiple dimensions of variation (e.g., renderer × OS) | Upfront design cost |
| **Composite** | Tree structures; uniform treatment of part/whole | UI trees, ASTs, org charts | Type safety vs `instanceof` checks |
| **Decorator** | Add responsibilities dynamically | Cross-cutting per-instance behavior | Ordering bugs; debugging stack depth |
| **Facade** | Simplify a subsystem interface | Onboarding, migration slices | God facade anti-pattern |
| **Flyweight** | Share intrinsic state across many objects | Huge numbers of similar icons/tokens | Thread safety; identity semantics |
| **Proxy** | Surrogate controls access | Lazy load, access control, remote stub | Latency; stale caches |

### GoF — behavioral

| Pattern | Intent | When to use | Watch-outs |
|---------|--------|-------------|------------|
| **Chain of Responsibility** | Pass request along a chain until handled | Middleware, event pipelines | Hard-to-trace flows |
| **Command** | Encapsulate a request as an object | Undo/redo, macros, job queues | Command proliferation |
| **Interpreter** | Grammar + interpretation | Small DSLs | Performance; prefer parser generators for large grammars |
| **Iterator** | Sequential access without exposing internals | Collections, streams | Concurrent modification hazards |
| **Mediator** | Centralize complex many-to-many collaboration | Chat rooms, dialog orchestration | Mediator becomes a god object |
| **Memento** | Capture and restore object state | Snapshots, undo stacks | Memory cost; encapsulation leaks |
| **Observer** | Notify dependents of changes | Model–view, domain events | Ordering; memory leaks from strong refs |
| **State** | Object behavior changes with internal state | Protocols, game AI, workflow steps | State class sprawl |
| **Strategy** | Interchangeable algorithms | Pricing rules, parsers, validators | Selection logic at call sites |
| **Template Method** | Fixed skeleton; subclasses fill steps | Frameworks with extension points | Inheritance rigidity |
| **Visitor** | Operations over a stable class hierarchy | AST walkers, document export | Adding types breaks visitors |

### Enterprise integration (representative)

| Pattern | Intent | When to use |
|---------|--------|-------------|
| **Message Channel** | Decouple producers/consumers | Async handoffs; burst absorption |
| **Message Router** | Route based on content/rules | Multi-tenant pipelines; versioned consumers |
| **Message Translator** | Transform between formats | Legacy + modern service boundaries |
| **Publish-Subscribe** | Broadcast to many subscribers | Event notifications; fan-out |
| **Competing Consumers** | Scale consumption horizontally | Work queues; backpressure with prefetch tuning |
| **Idempotent Receiver** | Safe retries | At-least-once messaging stacks |

---

## 4. Principles

### SOLID

| Principle | Meaning in practice | Typical violation |
|-----------|---------------------|------------------|
| **S — Single Responsibility** | One reason to change per module | “Utils” classes mixing IO, parsing, and business rules |
| **O — Open/Closed** | Extend behavior without modifying stable core | Copy-paste variants instead of strategy/plugin |
| **L — Liskov Substitution** | Subtypes honor supertype contracts | Throwing on “unsupported” overrides; stricter preconditions |
| **I — Interface Segregation** | Small, focused interfaces | Fat interfaces forcing dummy implementations |
| **D — Dependency Inversion** | Depend on abstractions; details plug in | New-ing concrete infrastructure in domain logic |

### Other core principles

| Principle | Essence | Application |
|-----------|---------|---------------|
| **DRY** | Each piece of knowledge has a single authoritative representation | Deduplicate business rules; do not merge **accidental** coincidence |
| **KISS** | Prefer the simplest design that meets forces | Resist framework gravity for toy problems |
| **YAGNI** | Do not build speculative generality | Add hooks when a second real use appears |
| **Separation of concerns** | Partition UI, domain, infrastructure | Boundaries align with change rates and ownership |
| **Composition over inheritance** | Build behavior from parts | Inheritance for **is-a** taxonomies; composition for **has-a** behavior wiring |

---

## 5. Clean code

### Naming

| Practice | Guidance |
|----------|----------|
| **Reveal intent** | Names answer *why* and *what*, not encoding details (`customerId`, not `str1`) |
| **Consistent vocabulary** | One word per concept (`fetch` vs `get` vs `load` — pick one domain lexicon) |
| **Avoid mental mapping** | No `i`, `j`, `k` except tight loops; no gratuitous abbreviations |
| **Searchable names** | Length scales with scope — globals and exports deserve longer names |

### Functions

| Practice | Guidance |
|----------|----------|
| **Small and focused** | One level of abstraction per function; early returns over deep nesting |
| **Few parameters** | Group related args into types/records; default to pure inputs over hidden globals |
| **Command/query** | Prefer functions that either do something *or* answer something — surprises break readers |
| **Errors are part of the API** | Use result types or exceptions consistently; document recoverability |

### Error handling

| Practice | Guidance |
|----------|----------|
| **Fail fast at boundaries** | Validate inputs; convert external errors to domain-meaningful results |
| **Preserve context** | Chain causes; add correlation IDs in distributed systems |
| **No empty catches** | Log or translate — silence hides incidents |
| **Resource safety** | `try/finally`, `using`, RAII — leaks are defects |

### Formatting and structure

| Practice | Guidance |
|----------|----------|
| **Vertical density** | Related lines together; blank lines separate ideas, not every line |
| **File organization** | Public API at top or bottom — **pick team convention** and automate with formatter |
| **Comments** | Explain *why* and invariants — not what the next line obviously does |

### Code review practices

| Practice | Guidance |
|----------|----------|
| **Checklist balance** | Correctness, security, performance (where relevant), readability, tests |
| **Small diffs** | Easier review correlates with fewer defects |
| **Teach in reviews** | Prefer questions and references over tone |
| **Automate the boring** | Linters/formatters own style debates |

---

## 6. Concurrency and parallelism

| Topic | Key ideas | Failure modes |
|-------|-----------|---------------|
| **Threads** | Shared memory; preemptive scheduling | Data races, deadlocks, priority inversion |
| **Async / await** | Cooperative tasks; non-blocking IO | Lost errors, unbounded queues, forgotten cancellation |
| **Actors** | Mailboxes; no shared mutable state by default | Mailbox backlog; distributed failure handling |
| **CSP (channels)** | Synchronous or buffered communication | Deadlock rings; channel leaks |
| **Parallel collections** | Fork-join, SIMD-friendly loops | Split imbalance; false sharing |
| **Race conditions** | Read/write ordering not what intuition says | Heisenbugs; flaky tests |
| **Synchronization primitives** | Locks, semaphores, barriers, RW locks, condition variables | Lock ordering discipline; missed signals |
| **Lock-free / atomic** | Compare-and-swap structures | ABA problem; subtle memory ordering — expert territory |

**Design guidance:** Prefer **immutable data** across threads, **message passing** across services, and **bounded** queues. Measure contention before micro-optimizing locks.

---

## 7. Networking fundamentals

| Topic | Essence | Practical notes |
|-------|---------|-----------------|
| **OSI vs TCP/IP** | Layered responsibility — physical through application | TCP/IP is the de facto stack engineers implement against daily |
| **HTTP/HTTPS** | Request/response, verbs, status codes, headers, caching | Idempotency of GET/PUT vs POST; cache invalidation discipline |
| **DNS** | Name → record resolution | TTLs affect failover; understand CNAME vs A/AAAA |
| **TLS** | Confidentiality + integrity + authentication | Terminate thoughtfully; certificate rotation; minimum protocol/cipher policy |
| **WebSocket** | Bidirectional channel over HTTP upgrade | Heartbeats; backpressure; auth on upgrade |
| **REST basics** | Resources, statelessness, uniform interface | HATEOAS rarely fully adopted; hypermedia when discoverability matters |

---

## 8. Version control (Git)

| Workflow | Branching model | Strengths | Trade-offs |
|----------|-----------------|-----------|--------------|
| **Trunk-based** | Short-lived branches; frequent integration to main | Fast feedback; fewer merge storms | Requires discipline, feature flags, strong CI |
| **GitFlow** | `develop`, `release`, `hotfix`, `feature` branches | Explicit release stabilization lanes | Branch overhead; slower integration for small teams |
| **GitHub Flow** | Feature branches off main; PR + deploy from main | Simple; aligns with PR review culture | Needs strong tests and safe deploys |

| Practice | Guidance |
|----------|----------|
| **Merging vs rebasing** | Merge preserves history graph; rebase linearizes feature work — agree team defaults for shared branches |
| **Commit conventions** | Imperative subject; scope optional; link issues; separate mechanical refactors from behavior change — **Forge SDLC** teams: branching + commit body/trailers for agent/search-friendly history in [`sdlc/methodologies/forge/setup/BRANCHING-STRATEGY.md`](../../../sdlc/methodologies/forge/setup/BRANCHING-STRATEGY.md) |
| **Small commits** | Bisect-friendly history; easier cherry-pick and revert |

---

## 9. Debugging and profiling

| Area | Systematic approach | Tools (examples) |
|------|---------------------|------------------|
| **Reproduction** | Minimize steps; capture data (logs, seeds, versions); binary search the timeline | Record/replay frameworks where available |
| **Hypotheses** | Change one variable; predict outcome; falsify quickly | Scientific method beats random tweaks |
| **Profiling (CPU)** | Sample or instrument hotspots; attribute time by call stack | `perf`, Intel VTune, language profilers |
| **Profiling (alloc)** | Track allocation sites; object lifetimes | Heap snapshots, allocation trackers |
| **Concurrency** | Thread dumps; lock contention views; race detectors | TSan, debuggers, tracer bullets |
| **Performance analysis** | Define SLO-related scenarios; measure p50/p95/p99 | Load drivers, A/B in shadow traffic |
| **Memory analysis** | Leak suspects: growth over time; dominator trees | Heap dumps, sanitizer builds |

---

## 10. Competencies

| Competency | Description |
|------------|-------------|
| **Computational thinking** | Decomposing problems, recognizing patterns, choosing structures and algorithms |
| **Paradigm fluency** | Selecting and mixing OOP/FP/reactive/procedural idioms appropriately |
| **API design** | Clear contracts, versioning discipline, error models, documentation |
| **Quality reflex** | Testing mindset, review discipline, static analysis literacy |
| **Concurrency literacy** | Reasoning about races, deadlocks, backpressure, and failure in parallel work |
| **Operational awareness** | Logging, metrics, tracing hooks that make production diagnosable |
| **Performance judgment** | Knowing when to measure, optimize, or deliberately not optimize |
| **VCS craftsmanship** | Branch hygiene, readable history, conflict resolution, release alignment |

---

## 11. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| SWEBOK v3 (IEEE Computer Society) | https://www.computer.org/education/bodies-of-knowledge/software-engineering | Broad SE knowledge areas aligned to industry practice |
| Clean Code (Robert C. Martin) | https://www.pearson.com/en-us/subject-catalog/p/Clean-Code-A-Handbook-of-Agile-Software-Craftsmanship/P200000003998/9780132350884 | Naming, functions, and refactoring craft |
| Design Patterns (Gamma, Helm, Johnson, Vlissides) | https://www.pearson.com/en-us/subject-catalog/p/Design-Patterns-Elements-of-Reusable-Object-Oriented-Software/P200000003445/9780201633612 | Canonical pattern catalog and vocabulary |
| The Pragmatic Programmer (Hunt & Thomas) | https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/ | Habits, tooling, and trade-off thinking |
| Structure and Interpretation of Computer Programs (SICP) | https://mitpress.mit.edu/9780262020771/structure-and-interpretation-of-computer-programs/ | Foundational CS — abstraction, recursion, state, interpreters |
| Enterprise Integration Patterns (Hohpe & Woolf) | https://www.enterpriseintegrationpatterns.com/ | Messaging and integration design language |

---

*Keep project-specific engineering standards in `docs/development/` and architecture decisions in `docs/adr/`, not in this file.*
