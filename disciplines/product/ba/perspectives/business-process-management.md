# Business Process Management perspective

How business analysis adapts when the initiative centers on **process improvement**, **workflow automation**, or **operational efficiency**. BPM initiatives require BA to model, analyze, and optimize processes — often before (or instead of) specifying software features.

**BABOK alignment:** BABOK v3 Business Process Management perspective.

**Related blueprints:** [`blueprints/pdlc/PDLC.md`](../../../../pdlc/PDLC.md) (process-related product changes) · [`blueprints/sdlc/methodologies/lean.md`](../../../../sdlc/methodologies/lean.md) (lean thinking, waste elimination).

---

## 1. How BPM changes the BA focus

| Traditional BA Focus | BPM BA Focus |
|---------------------|--------------|
| What the software system does | What the business process does (system may be one component) |
| Functional requirements for a solution | Process requirements — steps, decisions, handoffs, SLAs |
| User stories and acceptance criteria | Process models and performance metrics |
| Solution evaluation (does the software work?) | Process evaluation (is the process efficient, effective, compliant?) |

---

## 2. Knowledge area shifts

| Knowledge Area | BPM Adaptation |
|----------------|----------------|
| **BA Planning & Monitoring** | Plan BA around process boundaries, not system boundaries. Stakeholders include process owners, process participants, and process customers. |
| **Strategy Analysis** | Current state analysis focuses on process performance — cycle time, throughput, error rates, cost per transaction. Future state defines target process performance. |
| **Elicitation & Collaboration** | Observation and process mining are primary techniques. Interview process participants about actual behavior, not just stated procedures. |
| **Requirements Life Cycle Management** | Requirements include process requirements (steps, decisions, SLAs) alongside solution requirements. Process models need version control. |
| **Requirements Analysis & Design Definition** | BPMN process models, decision tables (DMN), and workflow specifications are the primary artifacts. Solution requirements emerge from process design. |
| **Solution Evaluation** | Evaluate process performance — cycle time improvement, error rate reduction, cost savings, compliance achievement — not just solution functionality. |

---

## 3. BPM lifecycle

Process improvement follows its own lifecycle that integrates with PDLC and SDLC:

```blueprint-diagram
key: linear
alt: Diagram
```

| BPM Phase | BA Activities | PDLC Mapping | SDLC Mapping |
|-----------|---------------|--------------|--------------|
| **Discover** | Identify process boundaries, stakeholders, inputs/outputs | P1 Discover | — |
| **Model As-Is** | Document current process in BPMN; capture metrics | P1 Discover | A Discover |
| **Analyze** | Identify bottlenecks, waste, errors, compliance gaps | P1–P2 | — |
| **Redesign** | Design target process; evaluate automation opportunities | P2 Validate, P3 Plan & Commit | B Specify, C Design |
| **Implement** | Execute process changes (may include software, training, org change) | SDLC A–F | A–F |
| **Monitor** | Track process performance against targets; identify further improvements | P5 Grow | — |

---

## 4. BPM-specific techniques

| Technique | BPM Usage |
|-----------|-----------|
| **Process modeling (BPMN)** | Document current and target processes using Business Process Model and Notation |
| **Value stream mapping** | Identify value-adding vs non-value-adding steps; quantify waste |
| **Process mining** | Analyze system event logs to discover actual process behavior (vs documented procedures) |
| **Simulation** | Model process behavior under different scenarios (volume, staffing, rule changes) |
| **Decision modeling (DMN)** | Define business decisions as tables — inputs, rules, outputs; supports automation |
| **SIPOC diagram** | Summarize process: Suppliers, Inputs, Process steps, Outputs, Customers |
| **Root cause analysis** | Investigate why process bottlenecks or errors occur |
| **Lean analysis** | Identify the eight wastes (transportation, inventory, motion, waiting, overproduction, overprocessing, defects, skills) |
| **Cycle time analysis** | Measure elapsed time for each process step; identify longest delays |
| **SLA definition** | Define Service Level Agreements for process performance targets |
| **RACI matrix** | Clarify process roles: who performs, who approves, who is consulted, who is informed |

---

## 5. BPM BA artifacts

| Artifact | Purpose | Where It Lives |
|----------|---------|----------------|
| **As-Is process model (BPMN)** | Documents current state process | `docs/product/` or process-specific documentation |
| **To-Be process model (BPMN)** | Documents target state process | `docs/product/` or process-specific documentation |
| **Process performance metrics** | Current and target KPIs for the process | `docs/product/metrics/` |
| **Decision tables (DMN)** | Formalized business rules for process decisions | `docs/requirements/` |
| **Process improvement recommendations** | Analysis results and proposed changes | `docs/product/discovery/` |
| **SIPOC diagram** | High-level process summary | `docs/product/` |
| **SLA definitions** | Performance targets for process steps | `docs/requirements/` |

---

## 6. Process automation spectrum

BPM initiatives often lead to automation. The BA helps determine the right level:

| Automation Level | Description | BA Focus |
|------------------|-------------|----------|
| **Manual** | Process performed entirely by people | Document procedures, train participants, monitor compliance |
| **Supported** | System provides information; humans make decisions and take actions | Specify information requirements, decision support needs |
| **Partially automated** | System handles routine steps; humans handle exceptions | Specify automation rules, exception handling, handoff points |
| **Highly automated** | System handles most steps; humans monitor and intervene rarely | Specify all business rules, exception escalation, monitoring dashboards |
| **Fully automated** | System handles everything including exceptions (straight-through processing) | Specify all decision logic, error recovery, compliance validation |

**Decision criteria for automation level:**
- Volume: high volume favors automation
- Complexity: high decision complexity may require human judgment
- Variability: high variability makes automation harder
- Compliance: regulatory requirements may mandate human review
- Cost: compare automation cost vs labor cost

---

## 7. Common pitfalls in BPM BA

| Pitfall | Description | Remedy |
|---------|-------------|--------|
| **Automating a bad process** | Implementing technology on a broken process — making it faster to do the wrong thing | Always analyze and redesign the process before automating; eliminate waste first |
| **As-Is only** | Documenting the current process in detail but never proposing improvements | Set a time limit on as-is modeling; focus energy on to-be design |
| **Process on paper only** | Beautiful BPMN diagrams that do not reflect actual behavior | Use observation and process mining to discover actual processes; validate models with participants |
| **Missing metrics** | Process improvement with no baseline or target metrics — "better" is undefined | Define quantitative targets (cycle time, error rate, cost) before starting redesign |
| **Technology-first** | Selecting a BPM tool before understanding the process | Understand the process first; select technology based on process requirements |
