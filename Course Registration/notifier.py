#anilkumarravuru

import urllib2,cookielib
import time
import webbrowser
from datetime import datetime
import json

def waitTime(t):
	# endTime = time.time() + t
	# while(time.time() < endTime):
	# 	anil = 1
	time.sleep(t)
	print '.'
	return

def main():

	reg_url = 'https://registration.gosolar.gsu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_level=GS&txt_subject=CSC&txt_campus=A&txt_term=202001&startDatepicker=&endDatepicker=&uniqueSessionId=a93oc1579290820283&pageOffset=0&pageMaxSize=50&sortColumn=subjectDescription&sortDirection=asc&[object%20Object]'
	cookie = 'JSESSIONID=Dx-zv-lReqGjjyir4d3r8nCqnXwLe5FRWSBQuJj6SoXqJgSSH8oC!1863951014; _ga=GA1.2.1342397038.1574345364; __cfduid=dbb4bc40bb4493f937de63ac27b2e0f181578074454; BIGipServerregistration.gosolar.gsu.edu=474177667.2336.0000; _gid=GA1.2.1690759397.1578427574; IDMSESSID=3CD652B0DBCCFB69CC0C8EAE333CB1B3264B06AA233D155AB816790D8503D115202E6CBB2EF022ACBE0A358B7D74BE921F2012779B14A3D4FF7D54CF9DA65B92; _gat=1; _gat_Ellucian=1'

	alert_song = "Sunflower.mp3"

	desired_course_numbers = ['8530', '8224']

	chrome_path = "open -a /Applications/Google\ Chrome.app %s"

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
				return
		except:
			print '-----------', datetime.now().time(),'something wrong with connection or urls'
			waitTime(60)
			flag = True

		if flag == False:
			for course_json in reg_json['data']:
				if course_json['courseNumber'] in desired_course_numbers and course_json['seatsAvailable'] > 0:
					print course_json['courseTitle'] + ' Opened'
					webbrowser.get(chrome_path).open_new(alert_song)
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
