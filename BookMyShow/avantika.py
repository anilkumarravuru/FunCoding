#anilkumarravuru
import urllib2,cookielib
import time
import webbrowser
# from twilio.rest import Client
from datetime import datetime


def waitTime(t):
	endTime = time.time() + t
	while(time.time() < endTime):
		anil = 1
	return

def substring(s,t):
	return s[:s.index(t)]

bangalore_url = "https://paytm.com/movies/bengaluru/avengers-endgame-m/o9otdt?fromdate=2019-05-01"
bangalore_song = "Happy.mp3"
chrome_path = "open -a /Applications/Google\ Chrome.app %s"

end_string = 'Avengers: Endgame Movie Ticket Booking Online'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

iteration = 1

prev_count = 1
while True:
	flag = False
	try:
		bang_req = urllib2.Request(bangalore_url, headers=hdr)
		bangalore_html = urllib2.urlopen(bang_req).read()
		bangalore_html = substring(bangalore_html, end_string)
		# bangalore_html = ''
	except:
		print '-----------', datetime.now().time(),'something wrong with connection or urls'
		waitTime(60)
		flag = True
	if flag== False:
		if 'PVR Forum IMAX, Koramangala' in bangalore_html:
			print "Tickets opened in Forum IMAX, Koramangala on May 1st"
			webbrowser.get(chrome_path).open_new(bangalore_song)
			break
		else:
			if iteration==60:
				iteration = 0
				fp = open('avantika.txt', 'r')
				l = fp.read()
				hrs = int(l)
				fp.close()
				print datetime.now().time(), "Wait is still on... Its been", hrs, "hours"
				fp = open('avantika.txt', 'w')
				fp.write(str(hrs+1))
				fp.close()
			waitTime(60)
			iteration+=1