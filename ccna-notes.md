# CCNA Notes

## Day 1: Network Devices

### Types of Network Devices
| Device | Purpose | OSI Layer |
|--------|---------|-----------|
| Hub | Connects devices in a network segment | Layer 1 |
| Switch | Connects devices within a LAN | Layer 2 |
| Router | Connects different networks | Layer 3 |
| Firewall | Filters traffic for security | Layers 3 & 4 |
| Access Point | Connects wireless devices | Layer 2 |

### Key Terms
- **Collision Domain:** Where data packets can collide. Hubs have one collision domain; switches have a separate collision domain per port.
- **Broadcast Domain:** Where a broadcast frame is sent to all devices. Routers break up broadcast domains; switches do not.

### Packet Tracer Practice
- **Built:** 2 PCs + 1 Switch
- **IPs:** PC0 - 192.168.1.1, PC1 - 192.168.1.2
- **Ping:** ✅ Successful

---

## Day 2: OSI Model & TCP/IP Model

### OSI Model (7 Layers)
| Layer | Name | Function |
|-------|------|----------|
| 7 | Application | User interface (HTTP, DNS, FTP) |
| 6 | Presentation | Data formatting, encryption, compression |
| 5 | Session | Connection management, session setup |
| 4 | Transport | End-to-end communication (TCP, UDP) |
| 3 | Network | Routing, IP addressing, packet forwarding |
| 2 | Data Link | Framing, MAC addresses, error detection |
| 1 | Physical | Cables, signals, hubs, electrical pulses |

### TCP/IP Model (4 Layers)
| Layer | Name | Function |
|-------|------|----------|
| 4 | Application | Combines OSI Layers 5-7 |
| 3 | Transport | Same as OSI Layer 4 |
| 2 | Internet | Similar to OSI Layer 3 |
| 1 | Network Access | Combines OSI Layers 1-2 |

### Key Difference
- **OSI** is a theoretical model (7 layers)
- **TCP/IP** is practical, used on the internet (4 layers)

### Mnemonic to Remember OSI Layers
- **Please Do Not Throw Sausage Pizza Away**
  - Physical (1)
  - Data Link (2)
  - Network (3)
  - Transport (4)
  - Session (5)
  - Presentation (6)
  - Application (7)

## Lab 1: Cisco CLI Modes

### Modes Practiced
| Mode | Prompt | Command to Enter |
|------|--------|------------------|
| User EXEC | `Router>` | (default on login) |
| Privileged EXEC | `Router#` | `enable` |
| Global Config | `Router(config)#` | `configure terminal` |
| Interface Config | `Router(config-if)#` | `interface fastEthernet 0/0` |
| Line Config | `Router(config-line)#` | `line vty 0 4` |
| Router Config | `Router(config-router)#` | `router rip` |

### Key Takeaways
- `end` takes you from any mode back to Privileged EXEC
- `exit` goes back one level
- `disable` takes you from Privileged to User EXEC

---

c
