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

# account_sid = "AC5e2b3364a1982f568939fa23ffd7ded4"i
# auth_token  = "6bc20071e0a0071f52c9aab656034e57"
# client = Client(account_sid, auth_token)
bangalore_url = "https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190426"
hyderabad_url = "https://in.bookmyshow.com/buytickets/avengers-endgame-hyderabad/movie-hyd-ET00100559-MT/20190426"

bangalore_song = "Sunflower.mp3"
hyderabad_song = "Happy.mp3"
chrome_path = "open -a /Applications/Google\ Chrome.app %s"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

iteration = 1
got_in_bangalore = False
got_in_hyderabad = False

prev_count = 1
while True:
	flag = False
	try:
		hyd_req = urllib2.Request(hyderabad_url, headers=hdr)
		bang_req = urllib2.Request(bangalore_url, headers=hdr)
		hyderabad_html = urllib2.urlopen(hyd_req).read()
		bangalore_html = urllib2.urlopen(bang_req).read()
		# bangalore_html = ''
	except:
		print '-----------', datetime.now().time(),'something wrong with connection or urls'
		waitTime(60)
		flag = True
	if flag== False:
		now_count = bangalore_html.count('data-showtime-code')
		if prev_count != now_count:
			print "New IMAX 3d show added in Bangalore on 26th", prev_count, now_count
			webbrowser.get(chrome_path).open_new(bangalore_song)
			prev_count = now_count
			# message = client.messages.create(to="+919741709101", from_="+919085596252", body="Tickets opened in Bangalore")
			# message.sid
		if (got_in_hyderabad == False) and ("Large Screen" in hyderabad_html):
			print "Got it in Hyderabad Prasads Large Screen"
			webbrowser.get(chrome_path).open_new(hyderabad_song)
			# message = client.messages.create(to="9085596252", from_="9085596252", body="Tickets opened in Hyderabad")
			# message.sid
			got_in_hyderabad = True
		if (got_in_bangalore == False or got_in_hyderabad == False):
			if iteration==60:
				iteration = 0
				fp = open('time.txt', 'r')
				l = fp.read()
				hrs = int(l)
				fp.close()
				print datetime.now().time(), "Wait is still on... Its been", hrs, "hours"
				fp = open('time.txt', 'w')
				fp.write(str(hrs+1))
				fp.close()
			waitTime(60)
			iteration+=1