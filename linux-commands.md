# Linux Commands I Learned

## Navigation & Files

| Command | What It Does | Example |
|---------|--------------|---------|
| `ls` | List files | `ls` |
| `ls -la` | List all files (including hidden) | `ls -la` |
| `cd` | Change directory | `cd inhere` |
| `cd ~` | Go to home directory | `cd ~` |
| `pwd` | Show current directory | `pwd` |
| `mkdir` | Create a folder | `mkdir test` |
| `cp` | Copy a file | `cp file1 file2` |
| `mv` | Move or rename a file | `mv file1 file2` |
| `rm` | Delete a file | `rm file.txt` |
| `cat` | Read a file | `cat readme` |
| `exit` | Log out | `exit` |
| `cat ./-` | Read a file named `-` | `cat ./-` |
| `cat "file with spaces"` | Read a file with spaces | `cat "spaces in filename"` |

---

## Reading & Searching

| Command | What It Does | Example |
|---------|--------------|---------|
| `file` | Check file type | `file data.txt` |
| `strings` | Extract readable text from binary | `strings data.txt` |
| `grep` | Search inside files | `grep "password" data.txt` |
| `find` | Find files | `find / -name "*.txt"` |
| `sort` | Sort lines | `sort data.txt` |
| `uniq -u` | Show only unique lines | `sort data.txt \| uniq -u` |
| `head` | Show first few lines | `head data.txt` |
| `tail` | Show last few lines | `tail data.txt` |
| `less` | Read long files page by page | `less data.txt` |
| `wc` | Count lines, words, characters | `wc -l data.txt` |
| `2>/dev/null` | Hide error messages | `find / -name file 2>/dev/null` |

---

## Compression & Encoding

| Command | What It Does | Example |
|---------|--------------|---------|
| `xxd -r` | Convert hex dump to binary | `xxd -r data.txt > file` |
| `gunzip` | Decompress `.gz` files | `gunzip file.gz` |
| `bunzip2` | Decompress `.bz2` files | `bunzip2 file.bz2` |
| `tar -xf` | Extract `.tar` files | `tar -xf file.tar` |
| `base64 -d` | Decode Base64 | `base64 -d data.txt` |
| `tr 'A-Za-z' 'N-ZA-Mn-za-m'` | Decode ROT13 | `cat data.txt \| tr 'A-Za-z' 'N-ZA-Mn-za-m'` |
| `cd /tmp` | Go to temporary directory | `cd /tmp` |
| `cp ~/file .` | Copy file to current directory | `cp ~/data.txt .` |
| `mv` | Rename a file | `mv file file.gz` |

---

## SSH, Networking & SSL

| Command | What It Does | Example |
|---------|--------------|---------|
| `ssh user@host -p port` | Connect to remote server | `ssh bandit0@... -p 2220` |
| `ssh -i keyfile user@host -p port` | Connect using SSH private key | `ssh -i sshkey.private bandit14@localhost -p 2220` |
| `su user` | Switch to another user | `su bandit14` |
| `nc host port` | Connect to a service on a port | `nc localhost 30000` |
| `openssl s_client -connect host:port` | Connect using SSL/TLS | `openssl s_client -connect localhost:30001` |
| `echo "text" \| command` | Send text as input to a command | `echo "password" \| openssl s_client -connect localhost:31790 -quiet` |
| `nano filename` | Create/edit a file | `nano key.txt` |
| `chmod 600 file` | Set file permissions | `chmod 600 key.txt` |

---

## Package Management & System Commands

| Command | What It Does | Example |
|---------|--------------|---------|
| `sudo apt update` | Update package list | `sudo apt update` |
| `sudo apt upgrade` | Upgrade installed packages | `sudo apt upgrade` |
| `sudo apt install <package>` | Install a new package | `sudo apt install net-tools` |
| `sudo apt remove <package>` | Remove a package | `sudo apt remove net-tools` |
| `sudo apt autoremove` | Remove unused packages | `sudo apt autoremove` |
| `sudo apt search <package>` | Search for a package | `sudo apt search wireshark` |
| `apt show <package>` | Show package info | `apt show wireshark` |
| `dpkg -i <file.deb>` | Install a .deb file | `sudo dpkg -i file.deb` |
| `dpkg -l` | List installed packages | `dpkg -l` |
| `uname -a` | Show system information | `uname -a` |
| `whoami` | Show current username | `whoami` |
| `groups` | Show user groups | `groups` |
| `sudo -l` | List available sudo commands | `sudo -l` |
| `ifconfig` | Show network interfaces | `ifconfig` |
| `ping` | Test network connectivity | `ping google.com` |
| `clear` | Clear the terminal screen | `clear` |

---

## Process Management

| Command | What It Does | Example |
|---------|--------------|---------|
| `ps` | Show running processes | `ps aux` |
| `ps aux` | Show all processes in detail | `ps aux` |
| `ps aux \| grep <name>` | Find a specific process | `ps aux \| grep firefox` |
| `top` | Show live system processes | `top` (Press `q` to quit) |
| `htop` | Interactive process viewer | `htop` |
| `kill <PID>` | Kill a process by ID | `kill 1234` |
| `kill -9 <PID>` | Force kill a process | `kill -9 1234` |
| `jobs` | Show background jobs | `jobs` |
| `bg` | Resume a job in background | `bg %1` |
| `fg` | Bring a job to foreground | `fg %1` |

### My Practice Notes
- `ps aux` shows all processes from all users
- `top` is great for monitoring system performance
- `kill -9` is a last resort for stuck processes
- `jobs` shows background tasks in the current shell

---

## Linux Terminal Shortcuts

### Shortcuts
| Shortcut | What It Does |
|----------|--------------|
| `Tab` | Auto-completes commands and file names |
| `↑ (Up Arrow)` | Shows previous command |
| `↓ (Down Arrow)` | Shows next command |
| `Ctrl + A` | Moves cursor to start of line |
| `Ctrl + E` | Moves cursor to end of line |
| `Ctrl + U` | Clears everything before cursor |
| `Ctrl + K` | Clears everything after cursor |
| `Ctrl + R` | Search command history |
| `Ctrl + C` | Stop/kill current command |
| `Ctrl + D` | Exit terminal |
| `Ctrl + Z` | Suspend current process |
| `history` | Show all previous commands |

### Aliases I Created
| Command | What It Does |
|---------|--------------|
| `alias ll='ls -la'` | Shortcut for `ls -la` |
| `alias gs='git status'` | Shortcut for `git status` |
| `alias c='clear'` | Shortcut for `clear` |
| `alias ..='cd ..'` | Shortcut to go up one directory |

### How to Make Aliases Permanent
```bash
nano ~/.bashrc
```

Add your aliases at the bottom, then:

```bash
source ~/.bashrc
```

---

Cisco Commands (From Packet Tracer Labs)

Switch Commands

Command Purpose
enable Enter Privileged EXEC mode
configure terminal Enter Global Config mode
hostname Set device name
enable secret Set privileged password
line console 0 Configure console line
line vty 0 4 Configure Telnet/SSH lines
interface vlan 1 Configure management VLAN
ip default-gateway Set default gateway for switch
ip domain-name Set domain for SSH
username Create local user
crypto key generate rsa Generate SSH keys
ip ssh version 2 Set SSH version
transport input ssh Allow only SSH
login local Use local username/password
write memory Save configuration
show running-config View current config
show ip interface brief View interface status
show ssh View SSH sessions

Router Commands

Command Purpose
interface gig0/0 Enter interface configuration
ip address [ip] [mask] Assign IP to interface
no shutdown Enable interface
exit Exit current mode
end Exit to Privileged EXEC

SSH Troubleshooting

· Username must match on both devices
· Password must match on both devices
· SSH version must be set to 2 on both devices
· RSA key modulus should be 2048

---

Nmap Commands 

Installation

Command Purpose
sudo apt install nmap -y Install Nmap

Basic Scans

Command Purpose
nmap -sn 192.168.1.0/24 Ping scan (host discovery)
nmap -sS 192.168.1.1 SYN scan (stealth)
nmap -sV 192.168.1.1 Version scan
nmap -O 192.168.1.1 OS detection
nmap -p 80,443 192.168.1.1 Scan specific ports
nmap -p- 192.168.1.1 Scan all ports (1-65535)

Nmap + Wireshark Integration

· Run Nmap scan → Capture in Wireshark → Analyze traffic
· SYN scan shows tcp.flags.syn == 1 packets in Wireshark
· Version scan shows service banners

My Practice

· Installed Nmap on WSL Ubuntu
· Ran ping scan to discover devices on my network
· Ran SYN scan to see open ports
· Combined Nmap with Wireshark for traffic analysis

---

My Personal Notes

Commands I Want to Remember

· cat ./-file07 - Read a file that starts with -
· grep millionth data.txt - Search for "millionth" in a large file
· find / -user bandit7 -size 33c - Find a file by size and owner
· 2>/dev/null - Hide error messages when searching
· echo "text" \| openssl s_client ... - Send text via SSL
· crypto key generate rsa — Must have domain name set first
· transport input ssh — Only allow SSH (not Telnet)
· no shutdown — Enable an interface
· write memory — Save configuration
· ip routing — Enable routing on L3 switch

File Type Flowchart

1. Always start with: file filename
2. Based on output:
   · ASCII text → cat filename
   · gzip compressed → gunzip filename
   · bzip2 compressed → bunzip2 filename
   · tar archive → tar -xf filename
   · data → strings filename

SSH Key Tips

· Always use chmod 600 for SSH keys
· Save keys in /tmp if permission denied in home directory
· Use ssh -i keyfile user@host -p port to connect

Ports I Used

· Port 2220 - SSH for Bandit
· Port 30000 - Netcat service (Level 14)
· Port 30001 - SSL service (Level 15)
· Port 31790 - SSL service for SSH key (Level 16)
· Port 443 - HTTPS/QUIC
· Port 80 - HTTP
· Port 53 - DNS



