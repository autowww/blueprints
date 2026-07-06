---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# IoT communication protocols (blueprint)

**Purpose:** Protocol selection guidance and implementation considerations for IoT device communication. Each protocol entry covers its architecture, message format, QoS, security, power profile, and best-fit scenarios.

**Why protocol selection matters:** The application protocol (and its transport) constrains **latency**, **duty cycle**, **security posture**, **NAT behavior**, and **operational cost**. Committing late often forces gateways, duplicate stacks, or non-interoperable silos. Treat protocol choice as an **architecture decision** tied to power budgets, update strategy, and cloud or on-prem integrations — see [`EMBEDDED-IOT.md`](../EMBEDDED-IOT.md) for the embedded/IoT map and [`IOT-SDLC-PDLC-BRIDGE.md`](../IOT-SDLC-PDLC-BRIDGE.md) for lifecycle impact.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/embedded-iot/`](../README.md); project-specific protocol configuration stays in **`docs/development/embedded/protocols/`**.

### Protocol stack (reference layers)

```blueprint-diagram
key: swimlane
alt: Process flow
title: Protocol stack reference flow
summary: How layer and protocol choices converge on shared connectivity with reviewable inspect-and-adapt feedback.
node: Process flow
detail: Entry for mapping application needs to reference protocol layers.
more: Framing starts from latency, duty cycle, security posture, and cloud or on-prem integration constraints on this page.
node: Lane A
detail: Primary path from requirement to a bounded protocol selection.
more: Each protocol entry covers architecture, message format, QoS, security, power profile, and best-fit scenarios in the table below.
node: handoff
detail: Traceable transfer between stack layer responsibilities.
more: Application protocols such as MQTT or CoAP sit above link and network transports; each handoff fixes constraints for the next layer.
node: shared outcome
detail: Interoperable device connectivity aligned to product constraints.
more: Committing late often forces gateways, duplicate stacks, or non-interoperable silos tied to power and update strategy.
node: Lane B
detail: Parallel path for operational inspection and adaptation.
more: NAT behavior, duty cycle, and operational cost remain visible after the initial architecture decision.
node: inspect / adapt
detail: Review field behavior against power and latency budgets.
more: Teams adjust QoS, polling versus event models, spreading factors, and broker or gateway placement as deployment evidence accumulates.
node: feedback
detail: Governed input back into protocol and architecture decisions.
more: Lifecycle impact is documented in IOT-SDLC-PDLC-BRIDGE; project-specific configuration stays in docs/development/embedded/protocols.
fallback_ascii: |
  Process flow

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

| Protocol | Layer | Focus | Deep dive |
|----------|-------|-------|-----------|
| **MQTT** & **CoAP** | Application | Pub/sub vs REST-like constrained apps — QoS, observe, brokers | [`mqtt-coap.md`](mqtt-coap.md) |
| **BLE** & **Zigbee** | Link + network / app | GATT, mesh, Thread/Matter context, coexistence | [`ble-zigbee.md`](ble-zigbee.md) |
| **LoRaWAN** | Network | LPWAN — spreading factors, ADR, class A/B/C, join procedures, fair-use policy | [EMBEDDED-IOT.md §3](../EMBEDDED-IOT.md#3-communication-protocols) |
| **Modbus** | Application (Serial/TCP) | Industrial — RTU vs TCP, function codes, register mapping, polling vs event | [EMBEDDED-IOT.md §3](../EMBEDDED-IOT.md#3-communication-protocols) |
| **OPC UA** | Application (TCP) | Industrial interoperability — information model, security, pub/sub, companion specifications | [EMBEDDED-IOT.md §3](../EMBEDDED-IOT.md#3-communication-protocols) |
| **CAN bus** | Data link | Automotive/industrial — message arbitration, error handling, CANopen, J1939 | [EMBEDDED-IOT.md §3](../EMBEDDED-IOT.md#3-communication-protocols) |
| **Matter** | Application | Smart home — Thread/Wi-Fi transport, device types, commissioning, multi-admin | (see [`ble-zigbee.md`](ble-zigbee.md)) |

**Core knowledge:** [`EMBEDDED-IOT.md`](../EMBEDDED-IOT.md) — communication protocol overview and selection criteria.

**Bridge:** [`IOT-SDLC-PDLC-BRIDGE.md`](../IOT-SDLC-PDLC-BRIDGE.md) — protocol choices across the lifecycle.

---

*Keep project-specific safety documentation in docs/safety/ and hazard analyses in docs/security/, not in this file.*
