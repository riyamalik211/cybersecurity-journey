# CCNA Notes

## Network Devices

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

---

## OSI Model & TCP/IP Model

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

---

## Cisco CLI Modes

| Mode | Prompt | How to Enter |
|------|--------|--------------|
| User EXEC | `Router>` | Default on login |
| Privileged EXEC | `Router#` | `enable` |
| Global Config | `Router(config)#` | `configure terminal` |
| Interface Config | `Router(config-if)#` | `interface fastEthernet 0/0` |
| Line Config | `Router(config-line)#` | `line vty 0 4` |
| Router Config | `Router(config-router)#` | `router rip` |
| Sub-Interface Config | `Router(config-subif)#` | `interface fastEthernet 0/0.10` |

### Key Takeaways
- `end` takes you from any mode back to Privileged EXEC
- `exit` goes back one level
- `disable` takes you from Privileged to User EXEC

---

## Commands Reference

### General Commands
| Command | Purpose |
|---------|---------|
| `enable` | Enter Privileged EXEC mode |
| `configure terminal` | Enter Global Config mode |
| `hostname` | Set device name |
| `enable secret` | Set privileged password |
| `line console 0` | Configure console line |
| `line vty 0 4` | Configure Telnet/SSH lines |
| `interface vlan 1` | Configure management VLAN |
| `ip default-gateway` | Set default gateway for switch |
| `ip domain-name` | Set domain for SSH |
| `username` | Create local user |
| `crypto key generate rsa` | Generate SSH keys |
| `ip ssh version 2` | Set SSH version |
| `transport input ssh` | Allow only SSH |
| `login local` | Use local username/password |
| `write memory` | Save configuration |
| `copy running-config startup-config` | Save configuration |
| `show running-config` | View current config |
| `show ip interface brief` | View interface status |
| `show ssh` | View SSH sessions |
| `show vlan brief` | View VLAN information |
| `show etherchannel summary` | View EtherChannel status |
| `show port-security address` | View secured MAC addresses |
| `show ip nat translations` | View NAT translations |

---

## Routing Concepts

### Static Routing
| Command | Purpose |
|---------|---------|
| `ip route [network] [mask] [next-hop]` | Add static route |
| `ip route 0.0.0.0 0.0.0.0 [next-hop]` | Add default route |

### RIP (Routing Information Protocol)
| Command | Purpose |
|---------|---------|
| `router rip` | Enable RIP |
| `version 2` | Set RIPv2 |
| `network [network]` | Advertise network |
| `no auto-summary` | Disable auto-summary |
| `passive-interface [interface]` | Stop sending updates on an interface |

### EIGRP (Enhanced Interior Gateway Routing Protocol)
| Command | Purpose |
|---------|---------|
| `router eigrp [AS]` | Enable EIGRP |
| `network [network]` | Advertise network |
| `no auto-summary` | Disable auto-summary |

### OSPF (Open Shortest Path First)
| Command | Purpose |
|---------|---------|
| `router ospf [process-id]` | Enable OSPF |
| `network [network] [wildcard] area [area]` | Advertise network |
| `area [area] range [network] [mask]` | Summarize routes |

---

## VLAN Concepts

### VLAN Commands
| Command | Purpose |
|---------|---------|
| `vlan [id]` | Create VLAN |
| `name [name]` | Name VLAN |
| `switchport mode access` | Set port as access port |
| `switchport access vlan [id]` | Assign port to VLAN |
| `switchport mode trunk` | Set port as trunk |
| `interface vlan [id]` | Configure management VLAN |

### Inter-VLAN Routing (Router-on-a-Stick)
| Command | Purpose |
|---------|---------|
| `interface gig0/0.[vlan]` | Create sub-interface |
| `encapsulation dot1q [vlan]` | Set VLAN encapsulation |
| `ip address [ip] [mask]` | Assign IP to sub-interface |

---

## VTP (VLAN Trunking Protocol)

### What I Learned
- VTP propagates VLANs from a Server to Client switches
- VTP Domain name must match on all switches
- VTP Password must be same on all switches
- VTP Version must be same (Version 2 is recommended)

### Commands
| Command | Purpose |
|---------|---------|
| `vtp domain [name]` | Set VTP domain |
| `vtp mode server/client/transparent` | Set VTP mode |
| `vtp password [password]` | Set VTP password |
| `vtp version 2` | Set VTP version |
| `show vtp status` | Verify VTP status |

### Test Results
- VLANs created on Server → Propagated to Client ✅
- `show vlan brief` on Client shows VLANs from Server ✅

---

## EtherChannel

### What I Learned
- Bundles multiple physical links into one logical link (Port-Channel)
- LACP is the open standard protocol
- Active mode initiates negotiation; Passive mode waits
- Increases bandwidth and provides redundancy
- All ports must have the same duplex and speed settings

### Commands
| Command | Purpose |
|---------|---------|
| `interface range fastEthernet 0/1 - 2` | Select multiple ports |
| `channel-group 1 mode active/passive` | Create EtherChannel |
| `interface port-channel 1` | Configure the logical interface |
| `show etherchannel summary` | Verify EtherChannel status |

### Troubleshooting
- Ports must have same duplex/speed ✅
- Ports must have same VLAN/trunk configuration ✅
- LACP must match on both sides ✅

---

## Inter-VLAN Routing on L3 Switch (SVI)

### What I Learned
- L3 switches can route between VLANs without a router
- SVIs (Switched Virtual Interfaces) are virtual interfaces for each VLAN
- Must enable `ip routing` on the switch

### Commands
| Command | Purpose |
|---------|---------|
| `interface vlan [id]` | Create SVI |
| `ip address [ip] [mask]` | Assign IP to SVI |
| `ip routing` | Enable routing on L3 switch |

### Test Results
- PC0 (VLAN 10) → PC1 (VLAN 20): ✅ Successful (routed via L3 switch)

---

## Port Security

### What I Learned
- Prevents unauthorized devices from connecting to a switch port
- Sticky MAC learns MAC address automatically
- Violation modes: Protect, Restrict, Shutdown
- Shutdown mode disables the port on violation

### Commands
| Command | Purpose |
|---------|---------|
| `switchport port-security` | Enable port security |
| `switchport port-security maximum [number]` | Set max MAC addresses |
| `switchport port-security violation [mode]` | Set violation action |
| `switchport port-security mac-address sticky` | Learn MAC address automatically |
| `show port-security address` | View secured MAC addresses |
| `show port-security interface [interface]` | View port security status |

### Test Results
- Unauthorized device plugged in → Port shutdown ✅
- Port recovered with `shutdown` and `no shutdown` ✅

---

## NAT (Network Address Translation)

### Dynamic NAT
**What I Learned:**
- Maps multiple private IPs to a pool of public IPs
- Used when multiple internal users need internet access

**Commands:**
| Command | Purpose |
|---------|---------|
| `access-list [number] permit [network] [wildcard]` | Define inside network |
| `ip nat pool [name] [start-ip] [end-ip] netmask [mask]` | Define public IP pool |
| `ip nat inside source list [acl] pool [name]` | Enable dynamic NAT |
| `ip nat inside` | Define inside interface |
| `ip nat outside` | Define outside interface |
| `show ip nat translations` | Verify NAT mappings |

### Static PAT (Port Forwarding)
**What I Learned:**
- Maps an external port to an internal server
- Also called "port forwarding"
- Used for hosting web servers, game servers, etc.

**Commands:**
| Command | Purpose |
|---------|---------|
| `ip nat inside source static tcp [internal-ip] [internal-port] [public-ip] [public-port]` | Static PAT (port forwarding) |

### Test Results
- Internal PC → Internet: ✅
- External user → http://public-ip: ✅ (Shows internal web server)
- `show ip nat translations`: ✅ Shows mappings

---

## My Personal Notes

### Commands I Want to Remember
- `crypto key generate rsa` — Must have domain name set first
- `transport input ssh` — Only allow SSH (not Telnet)
- `no shutdown` — Enable an interface
- `write memory` — Save configuration
- `ip routing` — Enable routing on L3 switch
- `show ip nat translations` — View NAT mappings

### Troubleshooting Tips
- If SSH fails, check username and password match on both devices
- If ping fails, check IP addresses and gateways
- If VLAN not working, check trunk and access port configurations
- If EtherChannel ports are suspended, check duplex/speed settings
- If NAT not working, verify `ip nat inside` / `ip nat outside`

### NAT Summary
| Type | Mapping | Use Case |
|------|---------|----------|
| Static NAT | One-to-one | Servers |
| Dynamic NAT | Many-to-many | Multiple users |
| Static PAT | Many-to-one (port-based) | Port forwarding |
| PAT (Overload) | Many-to-one | Home/Office internet access |
