---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# BLE, Zigbee & Short-Range Wireless Protocols

**Purpose:** Map **short-range** wireless options — **BLE**, **Zigbee**, **Thread**, **Matter**, and peers — to product constraints (range, power, mesh, IP, coexistence).

**Audience:** Teams using [`protocols/README.md`](README.md) and [`EMBEDDED-IOT.md`](../EMBEDDED-IOT.md).

---

## Overview

Short-range protocols occupy overlapping niches in **2.4 GHz** (and sub-GHz for some profiles). Choice depends on **who talks to whom** (phone vs gateway vs cloud), **topology** (star vs mesh), and **whether you need native IP**.

---

## BLE (Bluetooth Low Energy)

### GATT architecture

BLE exposes data through **GATT**: profiles bundle **services**; services contain **characteristics**; characteristics may have **descriptors** (metadata, CCCD for notifications).

```blueprint-diagram
key: linear
alt: BLE (Bluetooth Low Energy)
title: BLE GATT data path
summary: Maps how BLE exposes structured application data through GATT for low-power, short-range links.
node: BLE (Bluetooth Low Energy)
detail: Short-range 2.4 GHz radio for phones, wearables, and beacons.
more: Range, power, and topology trade-offs on this page depend on who talks to whom and whether native IP is needed.
node: Start
detail: Enter the GATT hierarchy that structures BLE application data.
node: Core steps (see walkthrough below)
detail: Profiles bundle services; services hold characteristics and descriptors.
more: Characteristics carry values; descriptors include CCCD for enabling notifications from sleepy sensors.
node: Outcome
detail: A reviewable model for connectable devices and notification channels.
node: Note: Advertising
detail: Broadcast PDUs advertise service UUIDs, names, and manufacturer data.
more: Advertising can be connectable or non-connectable and precedes pairing, bonding, and GATT access.
fallback_ascii: |
  BLE (Bluetooth Low Energy)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: Advertising
```

### Operational themes

| Topic | Detail |
|-------|--------|
| **Advertising** | Broadcasts connectable or non-connectable PDUs; carries service UUIDs, names, mfg data |
| **Connections** | Connection intervals, slave latency, supervision timeout trade latency vs power |
| **Power** | Deep sleep between connection events; shorten connection window for sensors |
| **BLE 5.x** | **LE Coded PHY** (long range), **extended advertising**, **periodic advertising** with sync |

---

## Zigbee

IEEE **802.15.4**-based stack with application layer from **Connectivity Standards Alliance** (formerly Zigbee Alliance).

### Roles

| Role | Function |
|------|----------|
| **Coordinator** | Forms network; one per PAN; trust center / key distribution |
| **Router** | Relays traffic; mains-powered typically |
| **End device** | Sleepy or reduced function; minimal routing |

```blueprint-diagram
key: linear
alt: Zigbee
title: Zigbee mesh stack path
summary: Traces how an 802.15.4 Zigbee network forms, routes traffic, and exposes application clusters.
node: Zigbee
detail: IEEE 802.15.4 stack with CSA application layer for home and sensor networks.
more: Native mesh and sub-GHz options suit building-wide sensor networks without requiring native IP.
node: Start
detail: A coordinator forms the PAN and distributes trust-center keys.
node: Core steps (see walkthrough below)
detail: Routers relay traffic; end devices join as sleepy or reduced-function nodes.
more: Mains-powered routers extend hop range; sleepy end devices minimize duty cycle at the cost of latency.
node: Outcome
detail: A governed mesh ready for standardized cluster commands and OTA updates.
node: Note: (Zigbee Cluster Library) defines
detail: ZCL clusters specify attributes and commands for domains like On/Off and metering.
more: Zigbee 3.0 unifies application profiles; Zigbee Direct can ease commissioning over BLE where supported.
fallback_ascii: |
  Zigbee

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: (Zigbee Cluster Library) defines
```

### Application layer

**ZCL** (Zigbee Cluster Library) defines **clusters** (attributes/commands) for domains like On/Off, Level Control, metering. **Zigbee 3.0** unifies application profiles. **Zigbee Direct** (where applicable) eases commissioning via BLE.

---

## Thread

- **IPv6** over 802.15.4; **6LoWPAN** compression.
- **Border router** connects mesh to Wi-Fi/Ethernet.
- **Sleepy end devices** (SED) rely on parent for buffering; **minimal end devices** (MED) are lighter.
- Compared to Zigbee: **native IP**, different routing (RPL); both are mesh-capable 802.15.4 stacks with different app layers — **Matter** often rides on Thread + Wi-Fi.

---

## Matter (overview)

[Matter](https://buildwithmatter.com/) unifies smart-home **interoperability**: **Thread** and **Wi-Fi** as primary transports; **BLE** used for **commissioning** (setup). Defines **device types** (lights, locks, sensors), **data model**, and **multi-admin** (multiple ecosystems). Controllers (apps, hubs) commission devices and issue standard cluster commands.

---

## Protocol comparison matrix

| Dimension | BLE | Zigbee | Thread | Z-Wave | Wi-Fi (HaLow) | LoRa | NB-IoT |
|-----------|-----|--------|--------|--------|---------------|------|--------|
| **Typical range** | ~10–100 m | ~10–100 m/hop | ~10–100 m/hop | Sub-GHz mesh | Sub-GHz / km-scale | km+ | Cellular wide |
| **Data rate** | ~1–2 Mbps | ~250 Kbps | ~250 Kbps | Low (~100 kbps class) | Low–mid | Very low | Low (100s kbps) |
| **Power** | Very low | Very low | Very low | Very low | Higher | Very low | Moderate |
| **Mesh** | Mesh optional (BLE Mesh) | Native | Native | Native | BSS not mesh | Star to gateway | Star (RAN) |
| **IP native** | No (L2WCAP) | No | Yes (IPv6) | No | Yes | No | Yes |
| **Relative module cost** | Low | Low–mid | Low–mid | Mid | Higher | Low | Module + SIM |
| **Typical max nodes** | Small (mesh tens–hundreds) | Hundreds+ | Hundreds+ | Hundreds | Many (AP-limited) | Very large (WAN) | Carrier scale |
| **Typical apps** | Phones, wearables, beacons | HA, sensors | HA + IP (Matter) | HA (regional) | Cameras, HaLow IoT | Agri, tracking | Meters, alarms |

*Figures are order-of-magnitude; product and region vary.*

---

## Decision flowchart

```blueprint-diagram
key: decision
alt: Decision flowchart
title: Short-range protocol selection
summary: A gated review of product constraints before committing to BLE, Zigbee, Thread, or peers.
node: Decision flowchart
detail: Frames protocol choice against range, power, mesh, and IP requirements on this page.
node: Current state
detail: Capture who talks to whom, topology needs, and 2.4 GHz coexistence constraints.
node: Checkpoint / gate
detail: Verify the candidate protocol meets range, throughput, and power budgets.
more: Use the comparison matrix to bound expectations for mesh depth, module cost, and typical node counts.
node: refine or escalate
detail: Revisit assumptions or escalate when the gate fails on a hard constraint.
more: Common misses include BLE for building-wide mesh without design and ignoring Wi-Fi coexistence on 2.4 GHz.
node: Continue flow
detail: Proceed with commissioning, security, and OTA patterns aligned to the chosen stack.
fallback_ascii: |
  Decision flowchart

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

---

## Commissioning and provisioning

| Pattern | BLE | Zigbee / Thread / Matter |
|---------|-----|---------------------------|
| **Out-of-band** | NFC/QR + BLE GATT for secrets | Install codes, QR, manual PIN |
| **Network join** | Pairing/bonding, LTK | Network key, link keys, CASE (Matter) |
| **Firmware trust** | Secure boot + signed OTA | Vendor-specific + standard OTA clusters |

Document **factory provisioning** vs **field commissioning** separately; align with threat model in [`../EMBEDDED-IOT.md`](../EMBEDDED-IOT.md).

---

## Coexistence (2.4 GHz)

| Issue | Mitigation |
|-------|------------|
| **Wi-Fi vs 802.15.4** | Channel planning, antenna placement, duty cycle limits |
| **Multi-radio SoCs** | **Nordic nRF**, **Silicon Labs EFR32**, etc. — time-sliced RF, coexistence APIs |
| **Testing** | Radiated tests with Wi-Fi traffic on representative channels |

---

## Security comparison (simplified)

| Protocol | Key mechanism (high level) |
|----------|-----------------------------|
| **BLE** | Pairing models (LE Secure Connections), bonding, LTK |
| **Zigbee** | Network key, link keys, trust center policies |
| **Thread** | Network key, link-layer security (802.15.4), secured commissioning (e.g. PSK/J-PAKE per stack) |
| **Matter** | Device attestation, CASE, ACLs on clusters |

---

## Anti-patterns

| Anti-pattern | Risk |
|--------------|------|
| **BLE for multi-hop building-wide mesh without design** | Range and throughput surprises |
| **Ignoring 2.4 GHz coexistence** | Random disconnects in dense Wi-Fi |
| **No OTA / no rollback** | Unpatchable vulnerabilities in field |

---

## External references

| Organization | URL |
|--------------|-----|
| Bluetooth specifications | https://www.bluetooth.com/specifications/ |
| Connectivity Standards Alliance (Zigbee) | https://csa-iot.org/ |
| Thread Group | https://www.threadgroup.org/ |
| Matter | https://buildwithmatter.com/ |

---

*Keep project-specific safety documentation in docs/safety/ and hazard analyses in docs/security/, not in this file.*
