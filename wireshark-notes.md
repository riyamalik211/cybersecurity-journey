# Wireshark Notes

## What is Wireshark?
- Network protocol analyzer
- Captures and displays network traffic in real-time
- Used for troubleshooting, analysis, and security monitoring

---

## How to Start a Capture
1. Open Wireshark
2. Select your network interface (Wi-Fi / Ethernet)
3. Click the blue shark fin button to start
4. Click the red square button to stop

---

## Basic Display Filters

| Filter | What It Shows |
|--------|---------------|
| `http` | Web traffic (HTTP requests) |
| `dns` | Domain name queries |
| `tcp` | TCP connections |
| `icmp` | Ping requests |
| `arp` | Address Resolution Protocol |
| `tls` | TLS/SSL encrypted traffic |
| `udp` | UDP traffic |

---

## Advanced Display Filters

| Filter | What It Shows |
|--------|---------------|
| `tcp.port == 443` | HTTPS traffic (port 443) |
| `tcp.port == 80` | HTTP traffic (port 80) |
| `ip.addr == 192.168.0.1` | Traffic to/from a specific IP |
| `ip.src == 192.168.0.121` | Traffic from a specific source IP |
| `ip.dst == 8.8.8.8` | Traffic to a specific destination IP |
| `ip.src == X && ip.dst == Y` | Traffic between two IPs |
| `tcp.analysis.flags` | TCP flags (SYN, ACK, RST, FIN) |
| `tcp.analysis.retransmission` | Retransmitted packets (network issues) |
| `http.request.method == "GET"` | HTTP GET requests |

### Filter to Remove Broadcast Noise

!arp&& !nbns && !stp

## TLS & TCP Observations

### TCP 3-Way Handshake
1. `SYN` → Client requests connection
2. `SYN-ACK` → Server acknowledges
3. `ACK` → Client confirms

### TLS Handshake
1. `Client Hello` → Client sends supported encryption methods
2. `Server Hello` → Server selects encryption method
3. Certificate Exchange → Server sends certificate
4. `Change Cipher Spec` → Both agree to use encryption

### Key Takeaways
- TLSv1.3 is the latest encrypted protocol
- TCP manages the connection (handshakes, acknowledgments, keep-alives)
- TLS provides the encryption layer
- `Client Hello` reveals the domain via SNI (Server Name Indication)

---

## How to Follow a TCP Stream
1. Find a TCP packet
2. Right-click on it
3. Click **Follow** → **TCP Stream**
4. View the entire conversation

---

## How to Add a Custom Column
1. Find a DNS packet (`dns` filter)
2. Right-click on the **Info** column → **Column Preferences**
3. Click **"+"** (Add)
4. Title: `DNS Query`
5. Field: `dns.qry.name`
6. Click **OK**

---

## Packet Details (What Each Section Shows)

| Section | What It Shows |
|---------|---------------|
| **Frame** | Physical packet details (size, capture time) |
| **Ethernet II** | MAC addresses (source/destination) |
| **Internet Protocol Version 4** | IP addresses (source/destination) |
| **User Datagram Protocol (UDP)** | Source/Destination Ports |
| **Transmission Control Protocol (TCP)** | Source/Destination Ports, Sequence/Acknowledgment numbers |
| **Transport Layer Security (TLS)** | Encrypted data, handshake details |
| **Domain Name System (DNS)** | Domain queries and responses |

---

## Insecure Protocols to Avoid

| Protocol | Issue |
|----------|-------|
| **Telnet** | Sends data in clear text (including passwords) |
| **FTP** | Sends data in clear text |
| **TFTP** | No security at all |
| **Use instead** | SSH, SFTP, FTPS, HTTPS |

---

## My Practice Log

### Day 8: First Capture
- Captured traffic from Wi-Fi
- Applied filters: `http`, `dns`, `tcp`, `icmp`
- Observed packet details (Source, Destination, Protocol, Length)

### Day 9: DNS & HTTP Filters
- Saw DNS queries for: `clients4.google.com`, `assets.msn.com`, `www.youtube.com`
- Saw `Client Hello` for `www.linkedin.com`
- TCP handshake observed: `SYN` → `SYN-ACK` → `ACK`

### Day 10: TLS & TCP Analysis
- Applied `tls` filter to see encrypted HTTPS traffic
- Observed `Application Data` packets (encrypted payload)
- Identified `TCP Keep-Alive` packets maintaining connections
- Saw `Server Hello` and `Change Cipher Spec` in TLS handshake

### Day 10: Insecure Protocols
- Learned Telnet, FTP, TFTP send data in clear text
- Learned to use SSH, SFTP, FTPS instead

### IP Addresses Used
| Device | IP Address |
|--------|------------|
| My PC (Windows) | 192.168.0.121 |
| My Router | 192.168.0.1 |
| Google DNS | 8.8.8.8 |
| WSL Ubuntu | 172.18.44.163 |

---

## Key Takeaways

1. **Always start with a filter** — don't look at all traffic
2. **DNS resolves domain names to IP addresses**
3. **Most web traffic is encrypted** (HTTPS / TLS)
4. **Telnet, FTP, TFTP are insecure** — never use them
5. **TCP uses a 3-way handshake** to establish connections
6. **SNI reveals domain names** even in encrypted traffic
7. **Routers connect different networks** and route traffic
8. **Default gateway** tells a PC where to send traffic for other networks
9. **Follow TCP Stream** shows entire conversation between two devices
10. **Custom columns** make important info easy to see

---

## Tools I Used
- Wireshark (installed on Windows)
- Cisco Packet Tracer (simulated network)
- WSL Ubuntu (Linux terminal)

## Advanced Wireshark Practice

### TCP SYN Analysis
tcp.flags.syn == 1 && tcp.flags.ack == 0
**What It Shows:** SYN packets — the start of new TCP connections.

**Why It Matters (SOC Analyst Skill):**
- Detects new connection attempts
- Helps identify network scanning
- Can reveal malware communication patterns
- Unusual spikes in SYN packets may indicate an attack

**My Practice:**
- Captured traffic while browsing websites
- Applied the SYN filter
- Saw [X] SYN packets = [X] new connections opened
- Destination ports: 53 (DNS), 443 (HTTPS), 80 (HTTP)

---

### Detection Filters

| Filter | What It Detects |
|--------|-----------------|
| `tcp.port == 445` | SMB traffic (file sharing/malware) |
| `dns && dns.qry.name contains "windows"` | Windows-related DNS queries |
| `http.request.method == "POST"` | Data being sent to a website |
| `tcp.analysis.retransmission` | Network issues or possible scanning |
| `tls.handshake.type == 1` | Client Hello (start of encrypted connection) |

---

### My Observations from SYN Filter Practice

| Observation | Count |
|-------------|-------|
| Total SYN packets | 14 |
| To port 53 (DNS) | 5 |
| To port 443 (HTTPS) | 6 |
| To port 80 (HTTP) | 1 |

**What This Means:**
- My PC initiated 14 new connections during the capture
- Most connections were for secure web traffic (HTTPS)
- Some connections were for DNS lookups
- All traffic went through my router (192.168.1.1)

---

### Why This is a SOC Analyst Skill

| What I Did | What a SOC Analyst Does |
|--------------|-------------------------|
| Applied a filter for SYN packets | Detect scanning or connection attempts |
| Counted new connections | Monitor for unusual traffic spikes |
| Observed patterns | Identify malicious activity |

---

### Key Takeaways from Advanced Practice

1. **SYN packets = new connection attempts**
2. **Monitoring SYN packets helps detect scanning**
3. **Port numbers reveal the type of traffic** (53=DNS, 443=HTTPS, 80=HTTP)
4. **Encrypted traffic (HTTPS) is normal for web browsing**
5. **Unusual destination ports may indicate suspicious activity**

---

## TCP Deep Dive Practice (Day 14)

### TCP 3-Way Handshake
1. **SYN** → Client requests connection
2. **SYN-ACK** → Server acknowledges
3. **ACK** → Client confirms

### TCP Flags
| Flag | Purpose |
|------|---------|
| SYN | Start a connection |
| ACK | Acknowledge data |
| FIN | End a connection |
| RST | Reset a connection |

### My Practice
- Captured TCP handshake to google.com
- Applied `tcp.flags.syn == 1` to see SYN packets
- Applied `tcp.stream eq 0` to see full handshake
- Followed TCP Stream to see the conversation

---

## Wireshark Tips

### Display Filters vs Capture Filters
| Type | Purpose | Example |
|------|---------|---------|
| **Display Filter** | Filter already captured packets | `dns` |
| **Capture Filter** | Filter before capture starts | `host 192.168.1.1` |

### Useful Display Filters
| Filter | What It Shows |
|--------|---------------|
| `dns` | DNS traffic only |
| `http` | HTTP traffic only |
| `tcp` | TCP traffic only |
| `tcp.port == 443` | HTTPS traffic |
| `tcp.flags.syn == 1` | SYN packets |
| `tcp.analysis.retransmission` | Retransmissions |
| `tls.handshake.type == 1` | Client Hello |
| `ip.addr == 192.168.1.1` | Traffic to/from an IP |


## My Progress Summary

### Protocols I Can Analyze
- ✅ DNS
- ✅ HTTP/HTTPS
- ✅ TCP
- ✅ TLS/SSL
- ✅ ICMP
- ✅ ARP
- ✅ NTP
- ✅ QUIC

### Filters I Can Use
- ✅ Basic: `dns`, `http`, `tcp`, `icmp`, `arp`
- ✅ Port-based: `tcp.port == 443`, `tcp.port == 80`
- ✅ IP-based: `ip.addr == X`, `ip.src == X`, `ip.dst == X`
- ✅ Analysis: `tcp.analysis.retransmission`, `tcp.analysis.flags`
- ✅ Advanced: `tcp.flags.syn == 1 && tcp.flags.ack == 0`
- ✅ TLS: `tls.handshake.type == 1`
- ✅ Custom columns for DNS, SNI

### Tools I Can Use
- ✅ Wireshark GUI
- ✅ tshark (command-line)
- ✅ Termshark (terminal-based)


