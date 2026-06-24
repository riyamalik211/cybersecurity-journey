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

---

## Next Steps
- Practice more filters daily
- Analyze traffic in different scenarios
- Combine Wireshark with Packet Tracer
- Learn more about TLS and encryption
