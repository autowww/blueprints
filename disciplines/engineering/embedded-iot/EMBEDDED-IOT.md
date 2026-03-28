# Embedded / IoT engineering body of knowledge

This document maps the core concerns of **embedded / IoT engineering** — real-time systems, firmware, constrained resources, communication protocols, edge computing, OTA updates, and safety-critical practices — to the blueprint ecosystem.

**How embedded/IoT relates to PDLC and SDLC:** Embedded/IoT is a **platform-specific discipline** that adds hardware-software co-design and safety constraints to SDLC and extends PDLC with physical product lifecycle concerns. See [`IOT-SDLC-PDLC-BRIDGE.md`](IOT-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Protocols:** Communication protocol selection and guidance is in [`protocols/`](protocols/README.md).

**Safety:** Safety-critical standards and engineering practices are in [`safety/`](safety/README.md).

---

## 1. Real-time systems

### RTOS selection factors

| Factor | Considerations |
|--------|---------------|
| **Scheduling** | Preemptive priority-based, round-robin, rate-monotonic; worst-case execution time (WCET) analysis |
| **Memory footprint** | Kernel size in KB; static vs dynamic allocation support; memory protection (MPU) |
| **Certification** | Pre-certified for safety standards (IEC 61508 SIL 3, DO-178C DAL A) |
| **Ecosystem** | Driver support, middleware (networking, file systems, USB), IDE integration |
| **Licensing** | Open source (FreeRTOS, Zephyr) vs commercial (VxWorks, QNX, ThreadX/Azure RTOS) |

### Common RTOS platforms

| RTOS | Strengths | Best fit |
|------|-----------|----------|
| **FreeRTOS** | Lightweight, AWS IoT integration, massive community, MIT license | General-purpose IoT, resource-constrained devices |
| **Zephyr** | Modern build system, extensive driver support, Bluetooth stack, Linux Foundation governance | Connected devices, wearables, industrial IoT |
| **VxWorks** | Deterministic, safety-certifiable, long history | Aerospace, defense, medical devices |
| **QNX** | Microkernel, POSIX-compliant, automotive-grade | Automotive (ADAS, IVI), industrial control |
| **Bare metal** | No OS overhead; full control | Ultra-constrained, single-purpose, timing-critical |

### Real-time design principles

| Principle | Description |
|-----------|-------------|
| **Determinism** | Bounded execution time for all code paths; no unbounded loops or dynamic allocation in real-time tasks |
| **Priority inversion prevention** | Priority inheritance or priority ceiling protocols |
| **Interrupt discipline** | Minimize ISR duration; defer work to tasks; avoid blocking in ISRs |
| **Watchdog timers** | Hardware watchdog to detect and recover from software hangs |
| **Stack analysis** | Static stack usage analysis to prevent overflow in constrained memory |

---

## 2. Firmware development

### Memory management

| Strategy | Description | When to use |
|----------|-------------|-------------|
| **Static allocation** | All memory allocated at compile time; no malloc/free | Safety-critical; ultra-constrained; predictable behavior |
| **Memory pools** | Pre-allocated fixed-size blocks; O(1) alloc/free | Known object sizes; no fragmentation |
| **Region-based** | Allocate from regions; free entire region at once | Request processing with clear lifetime boundaries |
| **Dynamic (guarded)** | malloc/free with guards, leak detection, fragmentation monitoring | Non-safety applications with monitoring |

### Boot process

| Stage | Activities |
|-------|-----------|
| **Bootloader** | Hardware initialization, secure boot verification, firmware image selection (A/B), jump to application |
| **Hardware init** | Clock configuration, peripheral initialization, memory controller setup |
| **RTOS init** | Kernel start, task creation, timer initialization, interrupt configuration |
| **Application init** | Configuration loading, peripheral drivers, network stack, application tasks |
| **Ready** | System operational; watchdog armed; telemetry reporting started |

### Power management

| Technique | Power saving | Wake source |
|-----------|-------------|-------------|
| **Clock gating** | Disable peripheral clocks when idle | Peripheral interrupt |
| **Sleep mode** | CPU halted, RAM retained, some peripherals active | Timer, GPIO, UART |
| **Deep sleep** | Most peripherals off, minimal RAM retained | RTC, external interrupt |
| **Hibernate** | RAM not retained; state saved to flash | External event, timer |
| **Duty cycling** | Periodic wake-measure-transmit-sleep | RTC timer |

---

## 3. Communication protocols

| Protocol | Transport | Range | Power | Data rate | Best fit |
|----------|-----------|-------|-------|-----------|----------|
| **MQTT** | TCP/IP | WAN | Medium | Variable | Cloud connectivity, telemetry, command/control |
| **CoAP** | UDP | WAN/LAN | Low | Low-medium | Constrained devices, request/response over UDP |
| **BLE** | Radio | ~100 m | Very low | 1–2 Mbps | Wearables, beacons, phone-to-device |
| **Zigbee** | Radio (mesh) | ~100 m per hop | Very low | 250 Kbps | Home automation, sensor networks |
| **LoRaWAN** | Radio | 2–15 km | Very low | 0.3–50 Kbps | Agricultural sensors, smart city, asset tracking |
| **Modbus** | Serial/TCP | Local | N/A | Low | Industrial automation, legacy equipment |
| **OPC UA** | TCP/IP | LAN/WAN | N/A | Variable | Industrial IoT, manufacturing, SCADA |
| **CAN bus** | Bus | ~500 m | N/A | 1 Mbps | Automotive, industrial machinery |

---

## 4. Edge computing

### Edge-cloud partitioning

| Processing tier | Location | Latency | Use case |
|----------------|----------|---------|----------|
| **Device edge** | On the microcontroller/SoC | Microseconds | Sensor fusion, anomaly detection, actuator control |
| **Gateway edge** | On a gateway device (Raspberry Pi, industrial PC) | Milliseconds | Protocol translation, local aggregation, TinyML inference |
| **Near edge** (fog) | On-premises server or regional data center | Low milliseconds | Video analytics, complex ML inference, local dashboards |
| **Cloud** | Public/private cloud | Tens of milliseconds+ | Training, historical analytics, fleet management, long-term storage |

### TinyML

| Concern | Guidance |
|---------|----------|
| **Model optimization** | Quantization (INT8), pruning, knowledge distillation to fit in KB–MB of flash |
| **Frameworks** | TensorFlow Lite Micro, Edge Impulse, CMSIS-NN |
| **Inference constraints** | Latency budget, memory ceiling, energy per inference |
| **Use cases** | Keyword spotting, anomaly detection, gesture recognition, predictive maintenance |

---

## 5. OTA updates

| Concern | Guidance |
|---------|----------|
| **Secure boot chain** | Verify firmware signature before flashing; root of trust in hardware |
| **A/B partitioning** | Two firmware slots; write to inactive, verify, swap — guaranteed rollback |
| **Delta updates** | Send binary diff instead of full image; reduces bandwidth for constrained networks |
| **Rollback policy** | Automatic rollback on boot failure (watchdog-triggered); manual rollback via management portal |
| **Update orchestration** | Fleet-wide staged rollout; canary group; automatic halt on elevated error rates |
| **Network resilience** | Resume interrupted downloads; integrity check before flash; handle partial connectivity |

---

## 6. IoT platform architecture

| Component | Purpose |
|-----------|---------|
| **Device provisioning** | Secure onboarding — device identity, certificate enrollment, initial configuration |
| **Device registry** | Inventory of devices, metadata, firmware version, group membership |
| **Telemetry ingestion** | High-throughput data pipeline for sensor readings, events, logs |
| **Command / control** | Send commands and configuration updates to devices; handle acknowledgments |
| **Digital twin** | Virtual representation of physical device — current state, desired state, simulation |
| **Fleet management** | Group management, OTA orchestration, monitoring dashboards, alerting |
| **Rules engine** | Event-driven automation — trigger actions based on telemetry conditions |

### Digital twins

| Aspect | Description |
|--------|-------------|
| **Reported state** | Device reports its actual state (sensor values, firmware version, health) |
| **Desired state** | Cloud sets desired configuration; device converges toward it |
| **Simulation** | Model device behavior for testing, capacity planning, "what-if" analysis |
| **Offline reconciliation** | When device reconnects, sync desired vs reported state; resolve conflicts |

---

## 7. Competencies

| Competency | Description |
|------------|-------------|
| **Embedded C/C++** | Low-level programming, memory management, bit manipulation, compiler intrinsics |
| **RTOS expertise** | Task design, synchronization primitives, priority management, timing analysis |
| **Hardware interfacing** | Reading datasheets, writing drivers, debugging with oscilloscope/logic analyzer |
| **Communication protocols** | Implementing and debugging MQTT, BLE, Zigbee, Modbus, CAN |
| **Power optimization** | Measuring current draw, duty cycle design, sleep mode selection |
| **Safety engineering** | Applying IEC 61508 / ISO 26262 processes, FMEA, fault tree analysis |
| **Edge/cloud integration** | Device-to-cloud data pipelines, OTA infrastructure, fleet management |
| **Testing and validation** | HIL testing, simulation, conformance testing, field testing |

---

## 8. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| IEC 61508 | https://www.iec.ch/functional-safety | Functional safety standard for programmable electronic systems |
| ISO 26262 | https://www.iso.org/standard/68383.html | Automotive functional safety |
| MISRA C | https://www.misra.org.uk/ | Safe C/C++ coding guidelines for embedded systems |
| IoT Security Foundation | https://www.iotsecurityfoundation.org/ | IoT security best practices and compliance frameworks |
| FreeRTOS | https://www.freertos.org/ | Open-source RTOS for microcontrollers |
| Zephyr Project | https://zephyrproject.org/ | Modern RTOS with extensive driver and protocol support |
| Eclipse IoT | https://iot.eclipse.org/ | Open-source IoT frameworks and tools |
| Edge Impulse | https://www.edgeimpulse.com/ | TinyML development platform |
| SLSA | https://slsa.dev/ | Supply chain security for firmware artifacts |

---

*Keep project-specific embedded documentation in `docs/development/embedded/`, hardware specifications in `docs/hardware/`, and architecture decisions in `docs/adr/`, not in this file.*
