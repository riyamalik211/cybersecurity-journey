# Packet Tracer Notes

## Project 1: Two PCs Talking

### Topology
- 2 PCs connected to 1 Switch

### IP Configuration
| Device | IP Address | Subnet Mask |
|--------|------------|-------------|
| PC0 | 192.168.1.1 | 255.255.255.0 |
| PC1 | 192.168.1.2 | 255.255.255.0 |

### Test
- Ping from PC0 to PC1: ✅ Successful
- Packets Sent: 4, Received: 4, Lost: 0 (0% loss)
- Minimum: 0ms, Maximum: 6ms, Average: 1ms

### What I Learned
- How to assign IP addresses in Packet Tracer
- How to test connectivity with ping
- How devices communicate through a switch
- A switch uses MAC addresses to forward traffic

## Project 2: Two Networks with a Router

### Topology
- PC0 (192.168.1.1) → Switch0 → Router0 → PC1 (192.168.2.1)

### Router Configuration
en
conf t
int gig0/0
ip add 192.168.1.254 255.255.255.0
no shutdown
int gig0/1
ip add 192.168.2.254 255.255.255.0
no shutdown
end

### PC Configuration
| Device | IP Address | Gateway |
|--------|------------|---------|
| PC0 | 192.168.1.1 | 192.168.1.254 |
| PC1 | 192.168.2.1 | 192.168.2.254 |

### Test
- Ping from PC0 to PC1: ✅ Successful
- Packets Sent: 4, Received: 3, Lost: 1 (ARP)
- Minimum: 0ms, Maximum: 1ms, Average: 0ms

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

### Troubleshooting Notes
- Username mismatch fixed: switched from `shish` to `ashish`
- Both router and switch must use same username/password
- SSH version must be set to 2 on both devices

---

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

### What I Learned
- Routers connect different networks
- Default gateway tells PC where to send traffic for other networks
- `no shutdown` enables router interfaces
- Need two cables: one for each network
- Router interfaces must be in the same subnet as the PCs they serve
