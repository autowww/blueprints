# Embedded / IoT ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **Embedded / IoT Engineering** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Embedded/IoT** — "Is the firmware/device **reliable, safe, and field-ready**?"

Embedded/IoT engineering extends standard SDLC with hardware-software co-design, safety certification, and field deployment constraints, and connects to PDLC through physical product manufacturing, fleet operations, and long-lived device lifecycle.

**Canonical sources:** [`EMBEDDED-IOT.md`](EMBEDDED-IOT.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Comparison table

| Dimension | Embedded/IoT Engineering | SDLC | PDLC |
|-----------|--------------------------|------|------|
| **Core question** | Is the firmware/device reliable, safe, and field-ready? | How do we build this correctly? | Should we build this; does it create the right outcomes? |
| **Scope** | Real-time systems, firmware, constrained resources, protocols, edge computing, OTA, safety certification, field ops | Requirements → design → implementation → verification → release (**A**–**F**) | Problem discovery → strategy → launch → growth → sunset (**P1**–**P6**) |
| **Primary owner** | Embedded / firmware engineers; safety engineers for SIL/ASIL | Delivery team | Product manager / product trio |
| **Success metric** | Uptime, OTA success rate, field failure rate, WCET compliance, safety certification status | Velocity, defect escape rate, CI/CD pass rate | Adoption, revenue, fleet size, field reliability |
| **Key artifacts** | Firmware binaries, HAL/BSP, device provisioning config, safety case, test harness | Specs, code, tests, release notes | Research, strategy, metrics |
| **Risk focus** | Hardware failures, real-time violations, safety hazards, field inaccessibility, constrained resources | Technical correctness | Market and outcome risk |

---

## Embedded/IoT across the lifecycle

| Phase | Embedded role | Key activities | Outputs |
|-------|--------------|----------------|---------|
| **P1 Discover** | **Feasibility assessor** | Evaluate hardware constraints, sensor availability, connectivity options, power budget | Feasibility report, component shortlist |
| **P2 Validate** | **Prototype builder** | Hardware prototype (dev board), proof-of-concept firmware, sensor integration test | Working prototype, power measurements |
| **P3 Strategize** | **Platform architect** | RTOS selection, SoC/MCU selection, connectivity stack, safety certification scope, BOM cost | Platform ADR, BOM estimate, certification plan |
| **A Discover** | **System designer** | Hardware-software interface definition; partition responsibilities between edge and cloud | System architecture, HW/SW interface spec |
| **B Specify** | **Firmware specifier** | Real-time requirements (WCET, jitter), memory budget, power budget, protocol selection | Firmware requirements, timing spec, memory map |
| **C Design** | **HAL/BSP designer** | Hardware Abstraction Layer, Board Support Package, driver architecture, RTOS task design | HAL API, task graph, interrupt map |
| **D Build** | **Firmware implementer** | Driver implementation, application logic, protocol stack integration, OTA client | Firmware binary, unit tests, simulation results |
| **E Verify** | **Integration tester** | Hardware-in-the-loop (HIL) testing, EMC pre-compliance, safety analysis (FMEA), field pilot | HIL results, safety analysis, field test report |
| **F Release** | **Firmware release engineer** | Binary signing, OTA deployment, manufacturing image, production programming | Signed firmware, manufacturing script, OTA rollout |
| **P4 Launch** | **Fleet deployer** | Device provisioning, initial fleet deployment, monitoring setup, field support readiness | Provisioned fleet, monitoring dashboards |
| **P5 Grow** | **Fleet operator** | OTA updates, remote diagnostics, predictive maintenance, telemetry analysis | Fleet health reports, OTA campaign results |
| **P6 Sunset** | **Decommission planner** | End-of-life firmware (security-only patches), device recall/recycling, data deletion | EOL firmware, decommission plan |

---

## Embedded-specific lifecycle concerns

### Hardware-software co-design

| SDLC phase | Hardware activity | Software activity | Coordination point |
|------------|-------------------|--------------------|--------------------|
| **A–B** | Component selection, schematic design | HAL requirements, memory/timing constraints | Interface specification (pin assignments, register maps) |
| **C** | PCB layout, prototype fabrication | HAL/BSP design, RTOS configuration | Hardware review with firmware team |
| **D** | Prototype boards available | Driver development on real hardware | Daily integration on prototype boards |
| **E** | EMC/safety testing, design-for-manufacturing | HIL testing, field pilot, conformance testing | Combined hardware-software test campaigns |
| **F** | Manufacturing pilot run | Production firmware, programming scripts | Manufacturing test integration |

### Safety certification impact on SDLC

| SDLC phase | Additional safety activities |
|------------|------------------------------|
| **A** | Hazard analysis, safety requirements derivation |
| **B** | Safety requirements specification, SIL/ASIL allocation |
| **C** | Safety architecture, redundancy design, fault detection |
| **D** | MISRA-compliant coding, static analysis, traceability |
| **E** | Safety validation, fault injection, independent verification |
| **F** | Safety case documentation, certification authority review |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Cloud-first thinking** | Designing IoT system as if devices always have fast, reliable connectivity | Offline-first; local autonomy; sync when possible; degrade gracefully |
| **Ignoring the field** | Building firmware that is only testable on the bench | HIL testing, field pilot, remote diagnostics, OTA from day one |
| **One firmware fits all** | Same binary for all hardware variants, controlled by runtime config | Compile-time configuration for hardware variants; BSP abstraction |
| **Security as an afterthought** | Shipping devices with default credentials, no secure boot, no OTA signing | Secure boot chain, device identity, encrypted OTA, certificate rotation |
| **Unbounded dynamic allocation** | Using malloc/free in real-time paths on constrained devices | Static allocation or memory pools for real-time tasks; monitor heap in non-real-time |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`EMBEDDED-IOT.md`](EMBEDDED-IOT.md) | Real-time systems, firmware, protocols, edge computing, OTA, digital twins |
| [`protocols/README.md`](protocols/README.md) | MQTT, CoAP, BLE, Zigbee, LoRaWAN, Modbus, OPC UA |
| [`safety/README.md`](safety/README.md) | IEC 61508, ISO 26262, DO-178C, MISRA |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6 |
| [`SEC-SDLC-PDLC-BRIDGE.md`](../../security/SEC-SDLC-PDLC-BRIDGE.md) | IoT security — device identity, OTA integrity, fleet key management |
| [`DEVOPS-SDLC-PDLC-BRIDGE.md`](../devops/DEVOPS-SDLC-PDLC-BRIDGE.md) | Embedded DevOps — firmware CI/CD, HIL testing, OTA pipelines |
