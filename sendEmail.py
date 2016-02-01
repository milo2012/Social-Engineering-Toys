import re
from random import randint
from time import sleep
import argparse
import smtplib
import sys
import email.utils
import dns.resolver
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

spoofedSenderName = ""
spoofedSenderEmail = ""
subject = ""



verbose=False
delayTime = 0

def cleanhtml(raw_html):
  	cleanr =re.compile('<.*?>')
  	cleantext = re.sub(cleanr,'', raw_html)
  	return cleantext

def sendEmail(targetName, targetEmail, htmlEmail, trackingCode):
	domain = targetEmail.split("@")[1]
	smtpServer = ""
	for x in dns.resolver.query(domain, 'MX'):
		smtpServer =  (x.to_text()).split(" ")[-1]

	print "Sending email to: "+targetEmail
	msg = MIMEMultipart('alternative')

	msg['To'] = email.utils.formataddr((targetName, targetEmail))
	msg['From'] = email.utils.formataddr((spoofedSenderName, spoofedSenderEmail))
	msg['Subject'] = subject
	
	html = htmlEmail
	html = html.replace("@user",targetName)

	if len(trackingCode.strip())>0:
		html = html.replace("@trackingCode",trackingCode)
	
	text = html.replace("<br>","\n")
	text = cleanhtml(text)

	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')
	
	msg.attach(part1)
	msg.attach(part2)

	server = smtplib.SMTP(smtpServer)
	server.helo("mta5.am0.yahoodns.net")
	#server.helo("mailext2.novatte.com")
	if verbose==True:
		server.set_debuglevel(True) # show communication with the server
	try:
	    server.sendmail(spoofedSenderEmail, [targetEmail], msg.as_string())
	finally:
	    server.quit()

if __name__ == '__main__':
    	global filename
    	parser = argparse.ArgumentParser()
    	parser.add_argument('-f', action='store', help='[html file containing the email body]')
    	parser.add_argument('-n', action='store', help='[recipient name]')
    	parser.add_argument('-e', action='store', help='[recipient email]')
    	parser.add_argument('-t', action='store', help='[delay between 1 to x seconds (random)]')
    	parser.add_argument('-iL', action='store', help='[file containing recipient name and email addresses per line separated by comma]')
    	parser.add_argument('-v', action='store_true', help='[verbose]')

    	if len(sys.argv)==1:
        	parser.print_help()
        	sys.exit(1)

    	options = parser.parse_args()
	
	if (options.iL and (options.n or options.e)):
		print "- You cannot use the -iL together with the (-n and -e) options"
		sys.exit()
	else:
		if (len(spoofedSenderName)<1 or len(spoofedSenderEmail)<1 or len(subject)<1):
			if len(spoofedSenderName)<1:
				print "- Please set the spoofedSenderName variable in "+sys.argv[0]	
			if len(spoofedSenderEmail)<1:
				print "- Please set the spoofedSenderEmail variable in "+sys.argv[0]
			if len(subject)<1:
				print "- Please set the subject variable in "+sys.argv[0]
			sys.exit()	
		if options.t:
			delayTime = options.t

		if options.iL and options.f:
			htmlEmail = ""
			with open(options.f, 'r') as myfile:
    				htmlEmail=myfile.read().replace('\n', '')

			dataList = [line.strip() for line in open(options.iL, 'r')]
			for x in dataList:
				if len(x.split(","))>2:
					targetName = x.split(",")[0]
					targetEmail = x.split(",")[1]
					trackingCode = x.split(",")[2]
					if delayTime!=0:
						sleep(randint(10,int(delayTime)))
					sendEmail(targetName, targetEmail, htmlEmail, trackingCode)
					
				else:
					targetName = x.split(",")[0]
					targetEmail = x.split(",")[1]
					sleep(randint(10,100))
					if delayTime!=0:
						sleep(randint(10,int(delayTime)))
					sendEmail(targetName, targetEmail, htmlEmail, "")
			sys.exit()
		if options.n and options.e and options.f:
			htmlEmail = ""
			with open(options.f, 'r') as myfile:
    				htmlEmail=myfile.read().replace('\n', '')
			targetName = options.n
			targetEmail = options.e
			if delayTime!=0:
				sleep(randint(10,int(delayTime)))
			sendEmail(targetName, targetEmail, htmlEmail, "")
			sys.exit()
		else:	
			print "- Please use a combination of (-iL and -f) or (-n, -e and -f) options"
			sys.exit()
