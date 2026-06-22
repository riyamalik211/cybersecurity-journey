# Linux Commands I Learned

## Day 1: Navigation & Files

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

## Day 2: Reading & Searching

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

---

## Day 3: Compression & Encoding

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

## Day 4: SSH, Networking & SSL

| Command | What It Does | Example |
|---------|--------------|---------|
| `ssh user@host -p port` | Connect to remote server | `ssh bandit0@... -p 2220` |
| `ssh -i keyfile user@host -p port` | Connect using SSH private key | `ssh -i sshkey.private bandit14@localhost -p 2220` |
| `su user` | Switch to another user | `su bandit14` |
| `nc host port` | Connect to a service on a port | `nc localhost 30000` |
| `nmap -p range host` | Scan for open ports | `nmap -p 31000-32000 localhost` |
| `openssl s_client -connect host:port` | Connect using SSL/TLS | `openssl s_client -connect localhost:30001` |
| `echo "text" \| command` | Send text as input to a command | `echo "password" \| openssl s_client -connect localhost:31790 -quiet` |
| `nano filename` | Create/edit a file | `nano key.txt` |
| `chmod 600 file` | Set file permissions | `chmod 600 key.txt` |

---

## Day 5-6: Package Management & System Commands

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

## Day 7: Process Management

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

---

## My Personal Notes

### Commands I Want to Remember
- `cat ./-file07` - Read a file that starts with `-`
- `grep millionth data.txt` - Search for "millionth" in a large file
- `find / -user bandit7 -size 33c` - Find a file by size and owner
- `2>/dev/null` - Hide error messages when searching
- `echo "text" \| openssl s_client ...` - Send text via SSL

### File Type Flowchart
1. Always start with: `file filename`
2. Based on output:
   - `ASCII text` → `cat filename`
   - `gzip compressed` → `gunzip filename`
   - `bzip2 compressed` → `bunzip2 filename`
   - `tar archive` → `tar -xf filename`
   - `data` → `strings filename`

### SSH Key Tips
- Always use `chmod 600` for SSH keys
- Save keys in `/tmp` if permission denied in home directory
- Use `ssh -i keyfile user@host -p port` to connect

### Ports I Used
- Port 2220 - SSH for Bandit
- Port 30000 - Netcat service (Level 14)
- Port 30001 - SSL service (Level 15)
- Port 31790 - SSL service for SSH key (Level 16)
