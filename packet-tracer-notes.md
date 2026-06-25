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

## Project 2: Two Networks with a Router (Day 10)

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

### What I Learned
- Routers connect different networks
- Default gateway tells PC where to send traffic for other networks
- `no shutdown` enables router interfaces
- Need two cables: one for each network
- Router interfaces must be in the same subnet as the PCs they serve
