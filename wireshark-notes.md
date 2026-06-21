# Wireshark Notes

## What is Wireshark?
- Network protocol analyzer
- Captures and displays network traffic in real-time
- Used for troubleshooting, analysis, and security monitoring

## How to Start Capture
1. Open Wireshark
2. Select your network interface (Wi-Fi / Ethernet)
3. Click the blue shark fin button to start
4. Click the red square button to stop

## Basic Display Filters
| Filter | What It Shows |
|--------|---------------|
| `http` | Web traffic (HTTP requests) |
| `dns` | Domain name queries |
| `tcp` | TCP connections |
| `icmp` | Ping requests |
| `arp` | Address Resolution Protocol |

## My Practice
- Captured traffic from my own Wi-Fi
- Applied filters: `http`, `dns`, `tcp`, `icmp`
- Observed packet details (Source, Destination, Protocol, Length)

## Tools I Used
- Wireshark (installed on Windows)
- Cisco Packet Tracer (simulated network)

## Why This Matters for Blue Team
- Helps detect malicious traffic
- Identifies suspicious IPs and domains
- Essential for network security analysis
