# Embedded / IoT Engineering

Reusable, **project-agnostic** blueprint for **Embedded / IoT Engineering** — the discipline of building reliable, safe software for resource-constrained and hardware-adjacent environments.

Embedded / IoT Engineering answers **"how do we build reliable, safe software for resource-constrained and hardware-adjacent environments?"** — a platform-specific discipline that extends the SDLC with hardware-software co-design, real-time constraints, and safety-critical standards, and connects to PDLC through physical product lifecycle and field operations.

| Document | Purpose |
|----------|---------|
| [**EMBEDDED-IOT.md**](EMBEDDED-IOT.md) | Real-time systems, firmware lifecycle, constrained resource programming, edge computing, OTA updates, digital twins, competencies |
| [**IOT-SDLC-PDLC-BRIDGE.md**](IOT-SDLC-PDLC-BRIDGE.md) | How Embedded/IoT maps across SDLC phases A–F and PDLC phases P1–P6 — emphasis on Design, Build, and Operate |
| [**protocols/**](protocols/README.md) | Communication protocol guidance: MQTT, CoAP, BLE, Zigbee, LoRaWAN, Modbus, OPC UA |
| [**safety/**](safety/README.md) | Safety-critical standards: IEC 61508, ISO 26262, DO-178C, MISRA — compliance and engineering practices |

## Relationship to other packages

| Package | How Embedded/IoT relates |
|---------|--------------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | Embedded delivery follows SDLC phases but adds hardware integration milestones, firmware build pipelines, and field testing. Release (F) involves OTA deployment and hardware manufacturing coordination. |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC P1–P2 include hardware prototyping and physical environment testing. P4 (Launch) involves manufacturing coordination and field deployment. P5 (Grow) includes fleet management and remote diagnostics. P6 (Sunset) must handle devices that cannot be remotely updated. |
| [`blueprints/disciplines/engineering/software-architecture/`](../software-architecture/README.md) | Embedded architecture decisions — RTOS selection, HAL design, edge-cloud partitioning, real-time scheduling — are constrained by hardware capabilities and safety requirements. |
| [`blueprints/disciplines/security/`](../../security/README.md) | IoT security is a distinct challenge — physical access to devices, constrained cryptography, OTA update integrity, device identity, fleet key management. IoT Security Foundation provides specialized guidance. |
| [`blueprints/disciplines/engineering/devops/`](../devops/README.md) | Embedded DevOps includes firmware CI/CD, hardware-in-the-loop (HIL) testing, OTA deployment pipelines, and fleet management. More constrained than cloud DevOps. |
| [`blueprints/disciplines/data/bigdata/`](../../data/bigdata/README.md) | IoT generates telemetry data at scale — time-series storage, stream processing, edge-to-cloud data pipelines, and data governance for sensor data. |
| [`blueprints/disciplines/engineering/testing/`](../testing/README.md) | Embedded testing includes hardware-in-the-loop, simulation, field testing, conformance testing, and safety certification testing — beyond standard software test levels. |

## Scope

This package covers **Embedded / IoT Engineering as a discipline** — not just microcontroller tutorials. It includes:

- **Real-time systems** — RTOS (FreeRTOS, Zephyr, VxWorks), scheduling, priority inversion, determinism, jitter
- **Firmware development** — boot process, memory management (no heap / static allocation), watchdog timers, power management
- **Constrained resource programming** — limited RAM/flash, no dynamic allocation, energy harvesting, duty cycling
- **Communication protocols** — MQTT, CoAP, BLE, Zigbee, LoRaWAN, Modbus, OPC UA, CAN bus
- **Edge computing** — edge inference (TinyML), fog architectures, edge-cloud data partitioning
- **Hardware-software interface** — drivers, HAL (Hardware Abstraction Layer), BSP (Board Support Package), GPIO, I2C, SPI, UART
- **OTA updates** — secure firmware update mechanisms, A/B partitioning, rollback, delta updates
- **Safety-critical systems** — IEC 61508, ISO 26262, DO-178C, MISRA C/C++, safety integrity levels (SIL/ASIL)
- **IoT platform architecture** — device provisioning, fleet management, telemetry ingestion, command/control, digital twins
- **Field operations** — remote diagnostics, predictive maintenance, field firmware recovery

Reference bodies of knowledge: IEC 61508, MISRA C/C++, IoT Security Foundation, Eclipse IoT, Barr Group Embedded C Coding Standard.

---

*Keep project-specific embedded documentation in `docs/development/embedded/`, hardware specs in `docs/hardware/`, and architecture decisions in `docs/adr/`, not in this file.*
