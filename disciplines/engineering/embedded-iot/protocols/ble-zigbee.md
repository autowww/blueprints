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
alt: Diagram
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
alt: Diagram
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
alt: Diagram
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
