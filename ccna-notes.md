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

## Lab 2: Basic Configuration of Router and Switch 

## Packet Tracer Project 2: Two Networks with a Router

### Topology
- PC0 (192.168.1.1) → Switch0 → Router0 → PC1 (192.168.2.1)

### Switch Configuration (DU)
| Setting | Value |
|---------|-------|
| Hostname | DU |
| Enable Secret | cisco123 |
| Console Password | ashish123 |
| Telnet Password | ashish@123# |
| Management IP | 192.168.10.10/24 |
| Default Gateway | 192.168.10.1 |

### Switch Commands Used
en
conf t
hostname DU
enable secret cisco123
banner motd "Unauthorized Users are highly Prohibited to login here"
line console 0
password ashish123
login
exit
line vty 0 4
password ashish@123#
login
exit
interface vlan 1
ip address 192.168.10.10 255.255.255.0
no shutdown
exit
ip default-gateway 192.168.10.1
write memory
### Router Configuration (BUET)
| Setting | Value |
|---------|-------|
| Hostname | BUET |
| Enable Secret | cisco123 |
| Console Password | ashish123 |
| Telnet Password | ashish@123# |
| Interface IP | 192.168.10.1/24 |

### Router Commands Used
en
conf t
hostname BUET
enable secret cisco123
banner motd"Do not try to access here"
line console 0
password ashish123
login
exit
line vty 0 4
password ashish@123#
login
exit
interface gig0/0
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
write memory
### PC Configuration
| Device | IP Address | Subnet Mask | Gateway |
|--------|------------|-------------|---------|
| PC0 | 192.168.10.2 | 255.255.255.0 | 192.168.10.1 |
| PC1 | 192.168.10.3 | 255.255.255.0 | 192.168.10.1 |

### Test Results
| Test | Result |
|------|--------|
| Ping PC0 → PC1 | ✅ Successful |
| Ping PC0 → Router | ✅ Successful |
| Telnet to Switch | ✅ Successful |

---

## Lab 3: Configuring SSH Access (Day 16)

### Topology
PC0(192.168.10.2)-- Switch(ASHISH-SW)--Router(Venus)
### Router Configuration (Venus)
| Setting | Value |
|---------|-------|
| Hostname | Venus |
| Domain Name | cisco.com |
| Username | ashish |
| Password | cisco123 |
| SSH Version | 2 |
| Interface IP | 192.168.10.1/24 |

### Router Commands Used
en
conf t
hostname Venus
interface gig0/0
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
ip domain-name cisco.com
username ashish privilege 15 password
cisco123
crypto key generate rsa
ip ssh version 2
enable secret cisco
line console 0
logging synchronous
login local
exit
line vty
transport input ssh
login local
exit
write memory
### PC Configuration
| Device | IP Address | Subnet Mask | Gateway |
|--------|------------|-------------|---------|
| PC0 | 192.168.10.2 | 255.255.255.0 | 192.168.10.1 |

### Test Results
| Test | Result |
|------|--------|
| SSH from PC0 to Switch | ✅ Successful |
| Command Used | `ssh -l ashish 192.168.10.10` |
| Password | `cisco123` |


## Commands Summary
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
| `show running-config` | View current config |
| `show ip interface brief` | View interface status |
| `show ssh` | View SSH sessions |

### Router Configuration
