# Gang of Four (GoF) design patterns

The *Gang of Four* catalog ([Gamma et al.](https://en.wikipedia.org/wiki/Design_Patterns)) documents **23 object-oriented patterns** grouped by **intent**:

| Category | Count | Question they answer |
|----------|-------|----------------------|
| **Creational** | 5 | *How do we create objects flexibly?* |
| **Structural** | 7 | *How do we compose types and objects?* |
| **Behavioral** | 11 | *How do objects collaborate and delegate responsibility?* |

**Parent context:** Condensed intent tables also appear in [`../SOFTWARE-ENGINEERING.md`](../SOFTWARE-ENGINEERING.md) § **3. Design patterns**.

---

## Creational patterns

| Pattern | Intent | When to use | Trade-off |
|---------|--------|-------------|-----------|
| **Abstract Factory** | Create families of related products without naming concretes | Swappable UI kits, multi-vendor integrations | Factory/interface proliferation |
| **Builder** | Construct a complex object step-by-step | Many optional fields; readable nested configuration | Boilerplate for simple DTOs |
| **Factory Method** | Let subclasses decide which product to instantiate | Framework extension points; plugin hooks | Extra indirection; discovery cost |
| **Prototype** | Clone exemplars instead of subclass-heavy creation | Costly construction; runtime-selected shapes | Deep vs shallow copy hazards |
| **Singleton** | Global single instance | Rarely justified — prefer DI scopes | Hidden deps; testing pain; concurrency |

### Builder (class structure)

```blueprint-diagram
key: network
alt: Diagram
```

### Factory Method (class structure)

```blueprint-diagram
key: network
alt: Diagram
```

---

## Structural patterns

| Pattern | Intent | When to use | Trade-off |
|---------|--------|-------------|-----------|
| **Adapter** | Make one interface usable as another | Legacy SDKs, third-party mismatches | Adapter does too much → leaky layer |
| **Bridge** | Decouple abstraction from implementation | Two orthogonal dimensions (e.g., UI × OS) | Up-front design investment |
| **Composite** | Treat individual and composite nodes uniformly | Trees: UI, AST, org charts | `instanceof` vs type-safe APIs |
| **Decorator** | Attach responsibilities dynamically | Cross-cutting per-instance behavior | Ordering bugs; deep decorator stacks |
| **Facade** | Simplify a subsystem’s surface | Migration slices, onboarding APIs | “God facade” that knows everything |
| **Flyweight** | Share intrinsic state across many instances | Huge counts of similar lightweight objects | Thread safety; identity semantics |
| **Proxy** | Surrogate controls access | Lazy load, caching, access control, remote stub | Latency; stale cache hazards |

---

## Behavioral patterns

| Pattern | Intent | When to use |
|---------|--------|-------------|
| **Chain of Responsibility** | Pass a request along until handled | Middleware, filters, approval chains |
| **Command** | Encapsulate a request as an object | Undo/redo, job queues, transactional scripts |
| **Interpreter** | Grammar + interpretation | Small DSLs; prefer parsers for large grammars |
| **Iterator** | Sequential access without exposing internals | Collections; often replaced by language `for-each` |
| **Mediator** | Centralize many-to-many collaboration | Complex UI dialogs, chat rooms |
| **Memento** | Capture/restore state | Snapshots, undo stacks |
| **Observer** | Notify dependents of changes | MVC, domain events; often → reactive streams |
| **State** | Behavior changes with internal state | Protocols, workflows, game AI modes |
| **Strategy** | Interchangeable algorithms | Pricing rules, parsers, validation policies |
| **Template Method** | Fixed skeleton; subclasses fill steps | Framework extension points |
| **Visitor** | Operations over a stable class hierarchy | AST walkers, document export pipelines |

---

## Behavioral patterns — trade-offs (compact)

| Pattern | Trade-off / watch-out |
|---------|------------------------|
| **Chain of Responsibility** | Hard-to-trace request paths; avoid endless default passes |
| **Command** | Proliferation of small command classes; justify with undo/queue needs |
| **Interpreter** | Performance; use parser generators for large grammars |
| **Iterator** | Concurrent modification unless snapshot or robust iterators |
| **Mediator** | Mediator becomes god object if every rule lives there |
| **Memento** | Storage cost; privacy of captured state |
| **Observer** | Ordering surprises; subscription leaks |
| **State** | Class-per-state sprawl for large machines |
| **Strategy** | Selection logic at call sites; avoid tiny strategies |
| **Template Method** | Inheritance rigidity; consider hooks + composition |
| **Visitor** | Adding new types breaks visitors unless paired with other moves |

---

## Pattern selection flowchart

```blueprint-diagram
key: decision
alt: Diagram
```

Use this as a **first triage**, not a mandate — many issues resolve with a function, a data record, or a module boundary before a named pattern.

---

## YAGNI reminder

Patterns carry **indirection and vocabulary cost**. Reach for a named GoF pattern when:

1. The **force** recurs (multiple clients, change hot-spots, extension points).  
2. The team can **name** it in reviews and onboarding docs.  
3. Simpler options (a function parameter, a module, a data-driven table) are **insufficient**.

If only one caller exists and no second use is on the roadmap, prefer **direct code** and extract the pattern when duplication proves the force.

---

## Compositions that show up together

| Pairing | Story |
|---------|--------|
| **Factory Method + Template Method** | Framework defines skeleton; subclasses supply creation and steps |
| **Composite + Visitor** | Walk trees uniformly; operations separated from node types |
| **Strategy + Context** | Context holds policy; strategies plug in without `switch` growth |
| **Decorator + Component interface** | Transparent wrappers around a stable abstraction |
| **Observer + Mediator** | Notifications fan-in to mediator instead of N² object links |

These are not mandates — they are **frequent collaborations** called out in the original text and in field experience.

---

## GoF thinking beyond classic OO languages

| Pattern spirit | Non-OO expression |
|----------------|-------------------|
| **Strategy** | Higher-order function, registry of handlers, typeclass/instance |
| **Command** | Message structs, Redux actions, job payloads |
| **Adapter** | Thin wrapper module at import boundary |
| **Iterator** | Language iterators, async generators |
| **Observer** | Event emitters, reactive streams, signals |

The **catalog** is OO-shaped; the **forces** are language-agnostic.

---

## Modern relevance

| Pattern | Still vital? | Often replaced / narrowed by |
|---------|--------------|------------------------------|
| **Strategy / Command / Adapter** | Yes | Language modules, first-class functions |
| **Iterator** | Concept vital | Built-in iterators, `for-of`, streams |
| **Observer** | Concept vital | Reactive libraries, event buses, signals |
| **Singleton** | Rarely as pattern | DI containers, explicit application scope |
| **Visitor** | Niche but strong | Still common for ASTs; sum types change trade-offs |
| **Template Method** | Mixed | Hooks vs composition; framework-dependent |
| **Abstract Factory** | Situational | Plugin registries, feature flags |

---

## External references

| Resource | Notes |
|----------|--------|
| Gamma, Helm, Johnson, Vlissides — *Design Patterns: Elements of Reusable Object-Oriented Software* | Original catalog and motivation |
| Refactoring.Guru — Design Patterns | [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns) — diagrams and trade-offs in web form |

---

*Keep project-specific engineering standards in `docs/development/` and architecture decisions in `docs/adr/`, not in this file.*
