# Bandit Walkthrough

## Level 0 → 1
**Command:** `ssh bandit0@bandit.labs.overthewire.org -p 2220`
**Password:** `bandit0`
**Steps:** `ls` → `cat readme`
**Password found:** `ZjLjTmM6FvvvRnrb2rfNWOZ0Ta6ip5IF`

## Level 1 → 2
**Command:** `ssh bandit1@bandit.labs.overthewire.org -p 2220`
**Steps:** `ls` → `cat ./-`
**Password found:** `263JGJPfgU6LtdEvgfWUfXPTr5J9iKMp`

## Level 2 → 3
**Command:** `ssh bandit2@bandit.labs.overthewire.org -p 2220`
**Steps:** `ls` → `cat "spaces in this filename"`
**Password found:** `MNk8KNH3Usio41PRUEoDFPqfxLP1Smx`

## Level 3 → 4
**Command:** `ssh bandit3@bandit.labs.overthewire.org -p 2220`
**Steps:** `cd inhere` → `ls -la` → `cat .hidden`
**Password found:** `2WmrDFRmJIq3IPxneAaMghap0pFhF3NJ`

## Level 4 → 5
**Command:** `ssh bandit4@bandit.labs.overthewire.org -p 2220`
**Steps:** `cd inhere` → `file ./-file*` → `cat ./-file07`
**Password found:** `40QYVPkxZOOE005pTW81FB8j8LxXGUQw`

## Level 5 → 6
**Command:** `ssh bandit5@bandit.labs.overthewire.org -p 2220`
**Steps:** `find . -type f -size 1033c ! -executable -exec file {} \; | grep ASCII` → `cat [file]`
**Password found:** `[Your Level 6 password]`

## Level 6 → 7
**Command:** `ssh bandit6@bandit.labs.overthewire.org -p 2220`
**Steps:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null` → `cat /var/lib/dpkg/info/bandit7.password`
**Password found:** `morbNTDKSW6j1Uc0ym0dMaLn0LFVAaj`

## Level 7 → 8
**Command:** `ssh bandit7@bandit.labs.overthewire.org -p 2220`
**Steps:** `grep millionth data.txt`
**Password found:** `dfwvzFQi4mU0wfNbFOe9R0wSkMLg7eEc`

## Level 8 → 9
**Command:** `ssh bandit8@bandit.labs.overthewire.org -p 2220`
**Steps:** `cat data.txt | sort | uniq -u`
**Password found:** `4CKMh1J1J91bUIZZPXDqGanaL4xvAg0JM`

## Level 9 → 10
**Command:** `ssh bandit9@bandit.labs.overthewire.org -p 2220`
**Steps:** `strings data.txt | grep "=="`
**Password found:** `FGUW5iLLVJrxx9kMYMmLN4MgbfMiqey`

## Level 10 → 11
**Command:** `ssh bandit10@bandit.labs.overthewire.org -p 2220`
**Steps:** `base64 -d data.txt`
**Password found:** `dtR173fZkboRRsDFSGsg2RWnpNVj3qRr`

## Level 11 → 12
**Command:** `ssh bandit11@bandit.labs.overthewire.org -p 2220`
**Steps:** `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
**Password found:** `7x16WNeHIi5YkIhWsFFIqoognUTyj9Q4`

## Level 12 → 13
**Command:** `ssh bandit12@bandit.labs.overthewire.org -p 2220`
**Steps:** 
1. `cd /tmp` → `mkdir riya_bandit12` → `cd riya_bandit12`
2. `cp ~/data.txt .`
3. `xxd -r data.txt > compressed_file`
4. Decompress layers: `gunzip` → `bunzip2` → `gunzip` → `tar -xf` → `tar -xf` → `bunzip2` → `gunzip`
5. `cat data8.bin`
**Password found:** `F05dWFsC0cBaI1H0h8J2eUk2vdtDWAn`

## Level 13 → 14
**Command:** `ssh bandit13@bandit.labs.overthewire.org -p 2220`
**Password:** `F05dWFsC0cBaI1H0h8J2eUk2vdtDWAn`
**Steps:** `ssh -i sshkey.private bandit14@localhost -p 2220`
**Password found:** `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`

## Level 14 → 15
**Command:** `ssh bandit14@bandit.labs.overthewire.org -p 2220`
**Password:** `MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`
**Steps:** `nc localhost 30000` → Submit password
**Password found:** `8xCjnmgokbGLhHFAZLGE5Tmu4M2tKJQo`

## Level 15 → 16
**Command:** `ssh bandit15@bandit.labs.overthewire.org -p 2220`
**Password:** `8xCjnmgokbGLhHFAZLGE5Tmu4M2tKJQo`
**Steps:** `openssl s_client -connect localhost:30001` → Submit password
**Password found:** `kSkvUpMQ7LBVyCM4GBPvCvT1BfWRy0Dx`

## Level 16 → 17 (In Progress)
**Command:** `ssh bandit16@bandit.labs.overthewire.org -p 2220`
**Password:** `kSkvUpMQ7LBVyCM4GBPvCvT1BfWRy0Dx`
**Steps:** 
1. `nmap -p 31000-32000 localhost` (Found port 31790)
2. `echo "password" | openssl s_client -connect localhost:31790 -quiet 2>/dev/null` (Received SSH key)
3. Tried to save key but getting `Permission denied` error
**Status:** Stuck at saving SSH key (will solve tomorrow)
