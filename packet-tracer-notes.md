# Cisco Packet Tracer Notes

## What is Packet Tracer?
- Network simulation tool by Cisco
- Used to build and test networks virtually
- No physical hardware required

---

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

---

## Project 2: Two Networks with a Router

### Topology
- PC0 (192.168.1.1) → Switch0 → Router0 → PC1 (192.168.2.1)

### Router Configuration
```

enable
configure terminal
interface gig0/0
ip address 192.168.1.254 255.255.255.0
no shutdown
interface gig0/1
ip address 192.168.2.254 255.255.255.0
no shutdown
end

```

### PC Configuration
| Device | IP Address | Gateway |
|--------|------------|---------|
| PC0 | 192.168.1.1 | 192.168.1.254 |
| PC1 | 192.168.2.1 | 192.168.2.254 |

### Test
- Ping from PC0 to PC1: ✅ Successful
- Packets Sent: 4, Received: 3, Lost: 1 (ARP)
- Minimum: 0ms, Maximum: 1ms, Average: 0ms

### What I Learned
- Routers connect different networks
- Default gateway tells PC where to send traffic for other networks
- `no shutdown` enables router interfaces
- Need two cables: one for each network
- Router interfaces must be in the same subnet as the PCs they serve

---

## Project 3: VLAN Configuration (Day 10)

### Topology
- PC0 → Switch0 → PC1

### VLANs Created
| VLAN ID | Name | Ports |
|---------|------|-------|
| 10 | Sales | FastEthernet0/1 |
| 20 | HR | FastEthernet0/2 |

### Switch Commands Used
```

enable
configure terminal
vlan 10
name Sales
vlan 20
name HR
exit
interface fast0/1
switchport mode access
switchport access vlan 10
interface fast0/2
switchport mode access
switchport access vlan 20
end

```

### PC Configuration
| Device | IP | VLAN |
|--------|----|------|
| PC0 | 192.168.1.1 | VLAN 10 |
| PC1 | 192.168.1.2 | VLAN 20 |

### Test
- Ping from PC0 to PC1: ❌ Failed (expected — PCs in different VLANs)

### What I Learned
- VLANs logically separate networks
- PCs in different VLANs cannot communicate without a router
- Access ports assign a single VLAN to a device

---

## Project 4: Inter-VLAN Routing (Router-on-a-Stick) 

### Topology
```

PC0 (VLAN 10) --- Switch0 --- Router0 --- PC1 (VLAN 20)

```

### Router Sub-Interface Configuration
```

enable
configure terminal
interface gig0/0
no shutdown
interface gig0/0.10
encapsulation dot1q 10
ip address 192.168.1.254 255.255.255.0
exit
interface gig0/0.20
encapsulation dot1q 20
ip address 192.168.2.254 255.255.255.0
end

```

### Switch Trunk Configuration
```

enable
configure terminal
interface fast0/3
switchport mode trunk
end

```

### PC Configuration
| Device | IP | Gateway |
|--------|----|---------|
| PC0 | 192.168.1.1 | 192.168.1.254 |
| PC1 | 192.168.2.1 | 192.168.2.254 |

### Test
- Ping from PC0 to PC1: ✅ Successful

### What I Learned
- Router-on-a-stick enables Inter-VLAN routing
- Sub-interfaces are used with 802.1Q encapsulation
- Trunk ports carry multiple VLANs between switch and router

---

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

## Lab 2: Basic Configuration of Router and Switch (Day 15)

### Topology
```

PC0 (192.168.10.2) --- Switch (DU) --- Router (BUET) --- PC1 (192.168.10.3)

```

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
```

enable
configure terminal
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

```

### Router Configuration (BUET)
| Setting | Value |
|---------|-------|
| Hostname | BUET |
| Enable Secret | cisco123 |
| Console Password | ashish123 |
| Telnet Password | ashish@123# |
| Interface IP | 192.168.10.1/24 |

### Router Commands Used
```

enable
configure terminal
hostname BUET
enable secret cisco123
banner motd "Do not try to access here"
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

```

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

## Lab 3: Configuring SSH Access

### Topology
```

PC0 (192.168.10.2) --- Switch (ASHISH-SW) --- Router (Venus)

```

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
```

enable
configure terminal
hostname Venus
interface gig0/0
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
ip domain-name cisco.com
username ashish privilege 15 password cisco123
crypto key generate rsa

```
(Choose 2048 bits for RSA key)

```

ip ssh version 2
enable secret cisco
line console 0
logging synchronous
login local
exit
line vty 0 4
transport input ssh
login local
exit
write memory

```

### Switch Configuration (ASHISH-SW)
| Setting | Value |
|---------|-------|
| Hostname | ASHISH-SW |
| Domain Name | ashish.com |
| Username | ashish |
| Password | cisco123 |
| SSH Version | 2 |
| Management IP | 192.168.10.10/24 |

### Switch Commands Used
```

enable
configure terminal
hostname ASHISH-SW
interface vlan 1
ip address 192.168.10.10 255.255.255.0
no shutdown
exit
ip default-gateway 192.168.10.1
ip domain-name ashish.com
username ashish privilege 15 password cisco123
crypto key generate rsa

```
(Choose 2048 bits for RSA key)

```

ip ssh version 2
enable secret cisco
line console 0
logging synchronous
login local
exit
line vty 0 4
transport input ssh
login local
exit
write memory

```

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

## Lab 4: Backup & Restore Configuration

### TFTP Server
- IP: 192.168.10.4
- Status: ON

### Backup Files
| Device | Filename | Status |
|--------|----------|--------|
| Switch (DU) | DU-config | ✅ |
| Router (BUET) | BUET-config | ✅ |

### Restore Process
1. Erased startup-config on switch and router
2. Reloaded both devices
3. Restored from TFTP server
4. Saved configurations

### Commands Used
| Command | Purpose |
|---------|---------|
| `copy running-config tftp` | Backup running config to TFTP |
| `erase startup-config` | Delete saved configuration |
| `reload` | Restart device |
| `copy tftp running-config` | Restore from TFTP |
| `write memory` | Save configuration |

### Test Results
- Switch backup: ✅ Successful
- Router backup: ✅ Successful
- Switch restore: ✅ Successful
- Router restore: ✅ Successful

---

## Lab 5: VLAN, Access & Trunk Port Configuration

### Topology
- 2 Switches, 4 PCs
- VLAN 10: cisco (PC0, PC2) — 192.168.10.0/24
- VLAN 20: solaris (PC1, PC3) — 172.16.20.0/24

### Trunk Link
- Switch0 (FastEthernet0/3) --- Switch1 (FastEthernet0/3)

### Commands Used
| Command | Purpose |
|---------|---------|
| `vlan [id]` | Create VLAN |
| `name [name]` | Name VLAN |
| `switchport mode access` | Set access port |
| `switchport access vlan [id]` | Assign port to VLAN |
| `switchport mode trunk` | Set trunk port |

### Test Results
| Test | Result |
|------|--------|
| PC0 → PC2 (same VLAN) | ✅ Successful |
| PC1 → PC3 (same VLAN) | ✅ Successful |
| PC0 → PC1 (different VLAN) | ❌ Failed (expected) |

---

## Lab 6: VTP Configuration

### Topology
- Switch0 (VTP Server) --- Switch1 (VTP Client)

### VTP Settings
| Setting | Server | Client |
|---------|--------|--------|
| VTP Domain | cisco.com | cisco.com |
| VTP Mode | Server | Client |
| VTP Password | cisco | cisco |
| VTP Version | 2 | 2 |

### VLANs Created
| VLAN ID | Name |
|---------|------|
| 100 | cisco |
| 200 | solaris |

### Test Results
- VLANs propagated from Server to Client: ✅
- VTP Status verified: ✅

---

## Lab 7: EtherChannel Configuration

### Topology
- Switch0 (DU) --- Switch1 (ASHISH) — 2 cables

### EtherChannel Settings
| Setting | DU | ASHISH |
|---------|----|--------|
| Channel Group | 1 | 1 |
| Mode | Active | Passive |
| Protocol | LACP | LACP |
| Ports | Fa0/1, Fa0/2 | Fa0/1, Fa0/2 |

### Verification Commands
| Command | Purpose |
|---------|---------|
| `show etherchannel summary` | Show EtherChannel status |
| `show interfaces trunk` | Show trunk status |

### Test Results
- `show etherchannel summary`: ✅ Po1(SU)
- Both ports bundled successfully

### What I Learned
- EtherChannel bundles multiple physical links into one logical link
- LACP is the open standard protocol
- Active mode initiates negotiation; Passive mode waits
- Increases bandwidth and provides redundancy

---

## Lab 8: VLAN, VTP, EtherChannel and Inter-VLAN Routing

### Topology
- DU (VTP Server) --- BUET (VTP Client)
- EtherChannel: Port-Channel 1 (Fa0/3-4)
- Router: DENVER (Inter-VLAN Routing)

### VLANs
| VLAN ID | Name | Subnet |
|---------|------|--------|
| 100 | CISCO | 192.168.100.0/24 |
| 200 | SOLARIS | 172.16.200.0/24 |

### Router Sub-Interfaces
| Interface | VLAN | IP Address |
|-----------|------|------------|
| gig0/0.100 | 100 | 192.168.100.1 |
| gig0/0.200 | 200 | 172.16.200.1 |

### Test Results
| Test | Result |
|------|--------|
| PC0 → PC2 (same VLAN) | ✅ |
| PC1 → PC3 (same VLAN) | ✅ |
| PC0 → PC1 (different VLAN) | ✅ |

---

## Lab 9: Inter-VLAN Routing on L3 Switch 

### Topology
- Switch (L3) — PC0 (VLAN 10) and PC1 (VLAN 20)

### VLANs
| VLAN ID | Name | Subnet |
|---------|------|--------|
| 10 | cisco | 192.168.10.0/24 |
| 20 | solaris | 192.168.20.0/24 |

### SVIs (Switched Virtual Interfaces)
| Interface | VLAN | IP Address |
|-----------|------|------------|
| vlan 10 | 10 | 192.168.10.1 |
| vlan 20 | 20 | 192.168.20.1 |

### Test Results
| Test | Result |
|------|--------|
| PC0 → PC1 (different VLANs) | ✅ |

### Key Command
```

ip routing

```
(Enables routing on L3 switch)

---

## Lab 10: Port Security 

### Topology
- PC0 --- Switch0 --- PC1

### Port Security Configuration
| Setting | Value |
|---------|-------|
| Interface | FastEthernet 0/1 |
| Maximum MAC Addresses | 1 |
| Violation Mode | Shutdown |
| Sticky MAC | Enabled |

### Commands Used
```

switchport port-security
switchport port-security maximum 1
switchport port-security violation shutdown
switchport port-security mac-address sticky

```

### Test Results
| Test | Result |
|------|--------|
| PC0 ping PC1 (initial) | ✅ |
| PC0 MAC address learned | ✅ SecureStatic on Fa0/1 |
| Unauthorized device plugged in | ❌ Port shutdown |

### What I Learned
- Port security prevents unauthorized devices
- Sticky MAC learns MAC address automatically
- Shutdown mode disables the port on violation
- Port can be recovered with `shutdown` and `no shutdown`

---

## Lab 11: Dynamic NAT Configuration 

### Topology
- PC0 --- Switch --- Gateway Router --- ISP Router --- PC2

### IP Addressing
| Device | Interface | IP Address |
|--------|-----------|------------|
| Gateway Router | Gig0/0 | 103.13.148.1 |
| Gateway Router | Gig0/1 | 192.168.10.1 |
| ISP Router | Gig0/0 | 103.13.148.2 |
| ISP Router | Gig0/1 | 10.10.10.1 |

### NAT Configuration
| Setting | Value |
|---------|-------|
| Inside Network | 192.168.10.0/24 |
| Public IP Pool | 103.13.148.10 - 103.13.148.20 |
| ACL | 1 (permits 192.168.10.0/24) |

### Commands Used
```

access-list 1 permit 192.168.10.0 0.0.0.255
ip nat pool NATPOOL 103.13.148.10 103.13.148.20 netmask 255.255.255.0
ip nat inside source list 1 pool NATPOOL

```

### Test Results
| Test | Result |
|------|--------|
| PC0 → PC2 | ✅ |
| `show ip nat translations` | ✅ Shows mappings |

---

## Lab 12: Static PAT (Port Forwarding) 

### Topology
- Server (192.168.10.10) --- Gateway Router --- ISP Router --- PC2 (Internet)

### Static PAT Configuration
| Setting | Value |
|---------|-------|
| Inside Server IP | 192.168.10.10 |
| Inside Port | 80 (HTTP) |
| Outside Public IP | 103.13.148.1 |
| Outside Port | 80 (HTTP) |

### Commands Used
```

access-list 1 permit 192.168.10.0 0.0.0.255
ip nat inside source list 1 interface gig0/0 overload
ip nat inside source static tcp 192.168.10.10 80 103.13.148.1 80

```

### Test Results
| Test | Result |
|------|--------|
| PC0 (Internal) → PC2 (Internet) | ✅ |
| PC2 (External) → http://103.13.148.1 | ✅ (Shows internal web server) |
| `show ip nat translations` | ✅ (Shows static PAT entry) |

### What I Learned
- Static PAT maps an external port to an internal server
- Useful for hosting web servers, game servers, etc.
- Also called "port forwarding"

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
| `copy running-config startup-config` | Save configuration |
| `show running-config` | View current config |
| `show ip interface brief` | View interface status |
| `show ssh` | View SSH sessions |
| `show vlan brief` | View VLAN information |
| `show etherchannel summary` | View EtherChannel status |
| `show port-security address` | View secured MAC addresses |
| `show ip nat translations` | View NAT translations |

---

## Troubleshooting Notes

| Issue | Solution |
|-------|----------|
| Ping fails | Check IP addresses and gateways |
| Interface shows "down" | Use `no shutdown` to enable it |
| PC can't reach other network | Set default gateway on PC |
| Router interface "down down" | Check cable connections |
| No connectivity | Use `show ip interface brief` to check status |
| SSH fails | Check username/password match on both devices |
| VLAN not working | Check trunk and access port configurations |
| EtherChannel ports suspended | Set same duplex/speed on all ports |
| NAT not working | Verify `ip nat inside` / `ip nat outside` |

---

## My Network Topologies

### Simple Network (Project 1)
```

PC0 (192.168.1.1) --- Switch0 --- PC1 (192.168.1.2)

```

### Two Networks (Project 2)
```

PC0 (192.168.1.1) --- Switch0 --- Router0 --- PC1 (192.168.2.1)

```

### Inter-VLAN Routing (Project 4)
```

PC0 (VLAN 10) --- Switch0 --- Router0 --- PC1 (VLAN 20)

```

### VTP + EtherChannel (Lab 8)
```

DU (VTP Server) --- EtherChannel --- BUET (VTP Client)

```

### NAT (Lab 11-12)
```

PC0 --- Switch --- Gateway Router --- ISP Router --- PC2 (Internet)

```

---

## Next Steps
- Continue with CCNA labs from the guide
- Practice daily in Packet Tracer
- Combine with Wireshark for traffic analysis
```
