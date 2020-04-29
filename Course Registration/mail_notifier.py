#anilkumarravuru

import urllib2,cookielib
import time
import webbrowser
from datetime import datetime
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def waitTime(t):
	# endTime = time.time() + t
	# while(time.time() < endTime):
	# 	anil = 1
	time.sleep(t)
	print '.'
	return

def send_mail(subject):
	mail_id = 'anilravurupublic@gmail.com'
	password = open('password.txt', 'r').read()

	# att        	@mms.att.net
	# tmobile    	@tmomail.net
	# verizon    	@vtext.com
	# sprint    	@page.nextel.com

	recipients = ['aravuru1@student.gsu.edu', '4438089584@mms.att.net']
	send_to_id = ', '.join(recipients)
	message = 'Go register buddy!!!'
	msg = MIMEMultipart()
	msg['From'] = mail_id
	msg['To'] = send_to_id
	msg['Subject'] = subject

	msg.attach(MIMEText(message, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(mail_id, password)
	text = msg.as_string()
	server.sendmail(mail_id, recipients, text)
	server.quit()


def main():
	reg_url = 'https://registration.gosolar.gsu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_level=GS&txt_subject=CSC&txt_campus=A&txt_term=202001&startDatepicker=&endDatepicker=&uniqueSessionId=4oq2p1579211697415&pageOffset=0&pageMaxSize=50&sortColumn=subjectDescription&sortDirection=asc&[object%20Object]'
	cookie = 'JSESSIONID=osOwWh95vrF3HASh30cjBTu9vsd69_y8R7BbmZLpeZBmzMSjRqXh!1863951014; _ga=GA1.2.1342397038.1574345364; __cfduid=dbb4bc40bb4493f937de63ac27b2e0f181578074454; BIGipServerregistration.gosolar.gsu.edu=474177667.2336.0000; _gid=GA1.2.1690759397.1578427574; __cf_bm=d1e96de9f74c518bcc310b2f43356cddb9dcd6f6-1579211570-1800-AZDgJ3+4/lG7K/jPTTx+XR2i8TAxHP9GSXeDPX9iEdcxEebDhheA87bCUI0mzJ9dS4WAHXANhAefw5M8j81G/kU=; _gat=1; _gat_Ellucian=1'

	alert_song = "Sunflower.mp3"

	desired_course_numbers = ['8530', '8224']

	iteration = 1

	prev_count = 1
	while True:
		flag = False
		try:
			reg_req = urllib2.Request(reg_url)
			reg_req.add_header('cookie', cookie)
			reg_response = urllib2.urlopen(reg_req).read()
			reg_json = json.loads(reg_response)
			if reg_json['totalCount'] == 0:
				print 'False response'
				send_mail('Script Failed... Update URL and restart')
		except:
			print '-----------', datetime.now().time(),'something wrong with connection or urls'
			waitTime(60)
			flag = True

		if flag == False:
			for course_json in reg_json['data']:
				if course_json['courseNumber'] in desired_course_numbers and course_json['seatsAvailable'] > 0:
					print course_json['courseTitle'] + ' Opened'
					#webbrowser.get(browser_path).open_new(alert_song)
					send_mail(course_json['courseTitle'] + ' Opened')
					desired_course_numbers.remove(course_json['courseNumber'])
					print desired_course_numbers
					if len(desired_course_numbers) == 0:
						return 
			else:
				if iteration == 60:
					iteration = 0
					fp = open('timer.txt', 'r')
					l = fp.read()
					hrs = int(l)
					fp.close()
					print datetime.now().time(), "Wait is still on... Its been", hrs, "hours"
					fp = open('timer.txt', 'w')
					fp.write(str(hrs+1))
					fp.close()
				waitTime(60)
				iteration += 1

if __name__ == '__main__':
	main()
