# Linux Commands I Learned

## Navigation Commands

| Command | What It Does | Example |
|---------|--------------|---------|
| `ls` | List files | `ls` |
| `ls -la` | List all files (including hidden) | `ls -la` |
| `cd` | Change directory | `cd inhere` |
| `pwd` | Show current directory | `pwd` |

## File Commands

| Command | What It Does | Example |
|---------|--------------|---------|
| `cat` | Read a file | `cat readme` |
| `file` | Check file type | `file ./-file00` |
| `grep` | Search inside files | `grep millionth data.txt` |

## Search Commands

| Command | What It Does | Example |
|---------|--------------|---------|
| `find` | Find files with specific properties | `find / -user bandit7 -size 33c` |

## SSH Commands

| Command | What It Does | Example |
|---------|--------------|---------|
| `ssh` | Connect to remote server | `ssh bandit0@... -p 2220` |
| `exit` | Log out | `exit` |

## My Personal Notes

### Commands I Want to Remember
- `cat ./-file07` - To read a file that starts with `-` (dash)
- `grep millionth data.txt` - Search for "millionth" in a large file
- `find / -user bandit7 -size 33c` - Find a file by size and owner
- `2>/dev/null` - Hide error messages when searching
