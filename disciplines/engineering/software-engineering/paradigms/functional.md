# Functional Programming (FP)

Functional programming treats computation as **evaluation of expressions** built from **pure functions** and **immutable data**, with **explicit** effect boundaries. It excels when correctness under concurrency and local reasoning matter more than modeling rich object lifecycles.

**Parent context:** Paradigm placement and typical strengths appear in [`../SOFTWARE-ENGINEERING.md`](../SOFTWARE-ENGINEERING.md) § **1. Programming paradigms**.

---

## Core concepts

| Concept | Practical meaning | Payoff | Pitfall |
|---------|-----------------|--------|---------|
| **Pure functions** | Same inputs → same output; no hidden IO or mutation | Easy tests; safe parallel maps | Pushing all IO to the edges requires discipline |
| **Immutability** | New values instead of in-place updates | Fewer races; simpler snapshots | Allocation/GC pressure if abused |
| **First-class functions** | Functions as values (stored, passed) | Callbacks, strategies without classes | Indirection; harder stack traces |
| **Higher-order functions** | Functions that take/return functions | `map` / `filter` / `reduce` pipelines | “Callback soup” without types |
| **Closures** | Function captures lexical bindings | Stateful iterators without objects | Accidental long-lived captures (memory) |
| **Currying** | Partial application of multi-arg functions | API specialization, reuse | Unfamiliar call sites for newcomers |
| **Pattern matching** | Branch on structure (sum types) | Exhaustive handling; readable dispatch | Language support varies |
| **Algebraic data types** | Sum + product types model domains | Compiler-checked states (`Option`, `Either`) | Ceremony if language lacks native support |

---

## Data transformation pipeline

```blueprint-diagram
key: linear
alt: Diagram
```

This shape appears in batch jobs, stream transforms, and UI state reducers: each stage is a **small pure step** with a clear type contract.

---

## FP vs OOP — comparison matrix

| Dimension | Functional emphasis | Object-oriented emphasis |
|-----------|---------------------|---------------------------|
| **State management** | Immutable values; explicit reducers | Encapsulated mutable state behind methods |
| **Composition** | Function composition, pipelines | Object graphs, interfaces, inheritance |
| **Testability** | Pure units; mock at IO boundary | Mock collaborators; fake interfaces |
| **Concurrency** | Fewer shared writes; easier reasoning | Locks, actors, or message passing around shared state |
| **Learning curve** | Types + higher-order functions upfront | Classes + frameworks; patterns catalog |

Most production systems are **multi-paradigm**: FP-style core with OOP at framework boundaries is a common split.

---

## Category theory — practitioner’s cheat sheet

Use these as **names for recurring composition patterns**, not as a mandate to prove theorems.

| Idea | Practical explanation | Typical code smell it names |
|------|------------------------|-----------------------------|
| **Functor** | “Mappable” context: apply a function inside a wrapper (`map`) | Manual unwrapping before every transform |
| **Applicative** | Combine multiple wrapped values with a function (`liftA2`, `zip`) | Nested `map` hell when combining independent options |
| **Monad** | Sequential computation where each step needs the previous result (`flatMap`, `bind`) | Error handling that throws away context; deeply nested callbacks |

Monads chain **dependent** steps; applicatives combine **independent** wrapped values. Knowing the word helps you pick the right combinator library — not to category-theorize every `if`.

---

## Language and ecosystem landscape

| Language / stack | FP strengths | Typical use |
|------------------|--------------|-------------|
| **Haskell** | Purity, lazy evaluation, rich type system | Research, compilers, high-assurance tools |
| **Scala** | FP + OOP on JVM; implicits / given | Data platforms, large enterprises |
| **Clojure** | Immutability by default; Lisp macros | Services, data scripting, DSLs |
| **Elixir** | Immutable data; actor model (OTP) | Telephony-scale, soft real-time services |
| **F#** | Succinct FP on .NET; type providers | Line-of-business, data science glue |
| **Rust** | Ownership + iterators; `Option`/`Result` | Systems with memory safety and algebraic errors |
| **TypeScript / JS** | `fp-ts`, Ramda, Lodash/fp | Frontends, Node services with typed pipelines |
| **OCaml / Reason** | Algebraic types, modules as boundaries | Compilers, tooling, some trading stacks |
| **Erlang** | Immutable processes; pattern matching | Soft real-time telecom-style systems |

---

## Referential transparency and reasoning

| Idea | Definition | Engineering payoff |
|------|------------|-------------------|
| **Referential transparency** | An expression can be replaced by its value without changing program meaning | Safe inlining, memoization, parallel evaluation |
| **Substitution model** | Imagine rewriting function bodies by replacing parameters | Finds accidental hidden state quickly |
| **Totality (when enforced)** | Functions cover all inputs without silent divergence | Fewer “impossible” states at runtime |

You do not need a purely functional **language** to harvest these benefits — a **functional slice** (immutable records + pure helpers) inside a larger codebase already tightens tests.

---

## Parallelism and FP

| Approach | Fits when | Watch-out |
|----------|-----------|-----------|
| **`map` / `pmap` over partitions** | Embarrassingly parallel transforms | Chunk size; thread-pool saturation |
| **Reduce / fold with associativity** | Divide-and-conquer reductions | Non-associative ops need different strategy |
| **Futures / tasks composed functionally** | Async pipelines with explicit combinators | Cancellation and error aggregation |
| **STM / actors (hybrid)** | Shared mutable world unavoidable | Still keep hot paths as small as possible |

Immutability reduces but does not remove coordination costs — you still design **bounded queues** and **backpressure** at system edges.

---

## Common FP patterns (beyond map/filter)

| Pattern | What it solves |
|---------|----------------|
| **Railway-Oriented Programming** | `Result`/`Either` chains for success/failure paths without nested try/catch |
| **Lens / optics** | Focused updates on nested immutable structures without manual copying |
| **Effect systems** | Track IO, async, and errors in the type system (language/library dependent) |

---

## When FP fits

- **Data pipelines** and ETL where transforms compose linearly  
- **Concurrent** or parallel maps over immutable partitions  
- **Compilers**, query planners, and rule engines  
- **Financial** and actuarial kernels where auditability and determinism matter  

---

## FP ↔ OOP collaboration (module-level)

| Layer | Typical FP shape | Typical OO shape |
|-------|------------------|------------------|
| **Domain transforms** | Pure functions over data | Entities with invariants |
| **Application services** | Pipelines orchestrating steps | Use-cases calling repositories |
| **Infrastructure** | Effectful interpreters | Adapters implementing ports |

Pick **one dominant style per module** so readers are not forced to context-switch every file — see [`../SOFTWARE-ENGINEERING.md`](../SOFTWARE-ENGINEERING.md) § **1** composition note.

---

## Anti-patterns

| Anti-pattern | Why it hurts |
|--------------|--------------|
| **Monad abuse** | Everything in one stack; unreadable `flatMap` towers |
| **Over-abstraction** | Type-class ceremony for one-off scripts |
| **Premature pointfree** | Tacit style that hides data flow for readers |

---

## External references

| Resource | Notes |
|----------|--------|
| Chiusano & Bjarnason — *Functional Programming in Scala* | Teaches FP patterns on a mainstream JVM language |
| Frisby — *Professor Frisby’s Mostly Adequate Guide to Functional Programming* | Free, JS-oriented intuition for functors/monads |
| Allen & Moronuki — *Haskell Programming from First Principles* | Deep foundations if you want rigor from the ground up |

---

*Keep project-specific engineering standards in `docs/development/` and architecture decisions in `docs/adr/`, not in this file.*
