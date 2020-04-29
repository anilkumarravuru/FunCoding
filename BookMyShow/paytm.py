#anilkumarravuru
import urllib2
import time
import webbrowser
from twilio.rest import Client
from datetime import datetime


def waitTime(t):
	endTime = time.time() + t
	while(time.time() < endTime):
		anil = 1
	return

def substring(s,t):
	return s[:s.index(t)]
# account_sid = ""
# auth_token  = ""
# client = Client(account_sid, auth_token)
print 'Code restarted at:', datetime.now().time()
bangalore_url_26 = "https://paytm.com/movies/bengaluru/avengers-endgame-m/o9otdt?fromdate=2019-04-26"
bangalore_url_27 = "https://paytm.com/movies/bengaluru/avengers-endgame-m/o9otdt?fromdate=2019-04-27"
bangalore_url_28 = "https://paytm.com/movies/bengaluru/avengers-endgame-m/o9otdt?fromdate=2019-04-28"
hyderabad_url = "https://paytm.com/movies/hyderabad/avengers-endgame-m/o9otdt?fromdate=2019-04-26"

bangalore_song = "Sunflower.mp3"
hyderabad_song = "Happy.mp3"
chrome_path = "open -a /Applications/Google\ Chrome.app %s"

end_string = 'Avengers: Endgame Movie Ticket Booking Online'

bangalore_html_old_count_26 = 1
bangalore_html_old_count_27 = 1
bangalore_html_old_count_28 = 1
iteration = 1
got_in_bangalore = False
got_in_hyderabad = False
while True:
	flag = False
	try:
		bangalore_html_26 = urllib2.urlopen(bangalore_url_26).read()
		bangalore_html_26 = substring(bangalore_html_26, end_string)
		# print bangalore_html_26.count('IMAX 3D')
		bangalore_html_27 = urllib2.urlopen(bangalore_url_27).read()
		bangalore_html_27 = substring(bangalore_html_27, end_string)
		# print bangalore_html_27.count('IMAX 3D')
		bangalore_html_28 = urllib2.urlopen(bangalore_url_28).read()
		bangalore_html_28 = substring(bangalore_html_28, end_string)
		# print bangalore_html_28.count('IMAX 3D')
		hyderabad_html = urllib2.urlopen(hyderabad_url).read()
	except:
		print '-----------', datetime.now().time(),'something wrong with connection or urls'
		waitTime(60)
		flag = True
	if flag== False:
		if bangalore_html_old_count_26 != bangalore_html_26.count('IMAX 3D'):
			print 'New IMAX 3D show added in Bangalore on 26th', bangalore_html_old_count_26, bangalore_html_26.count('IMAX 3D')
			webbrowser.get(chrome_path).open_new(bangalore_song)
			bangalore_html_old_count_26 = bangalore_html_26.count('IMAX 3D')
		if bangalore_html_old_count_27 != bangalore_html_27.count('IMAX 3D'):
			print 'New IMAX 3D show added in Bangalore on 27th', bangalore_html_old_count_27, bangalore_html_27.count('IMAX 3D')
			webbrowser.get(chrome_path).open_new(bangalore_song)
			bangalore_html_old_count_27 = bangalore_html_27.count('IMAX 3D')
		if bangalore_html_old_count_28 != bangalore_html_28.count('IMAX 3D'):
			print 'New IMAX 3D show added in Bangalore on 28th', bangalore_html_old_count_28, bangalore_html_28.count('IMAX 3D')
			webbrowser.get(chrome_path).open_new(bangalore_song)
			bangalore_html_old_count_28 = bangalore_html_28.count('IMAX 3D')
		# if (got_in_bangalore == False) and ("PVR Forum IMAX, Koramangala" in bangalore_html):
		# 	print "Got it in Bangalore"
		# 	webbrowser.get(chrome_path).open_new(bangalore_song)
		# 	# message = client.messages.create(to="+919741709101", from_="+919085596252", body="Tickets opened in Bangalore")
		# 	# message.sid
		# 	got_in_bangalore = True
		if (got_in_hyderabad == False) and ("Large Screen" in hyderabad_html):
			print "Got it in Hyderabad Prasads Large Screen"
			webbrowser.get(chrome_path).open_new(hyderabad_song)
			# message = client.messages.create(to="9085596252", from_="9085596252", body="Tickets opened in Hyderabad")
			# message.sid
			got_in_hyderabad = True
		if (got_in_bangalore == False or got_in_hyderabad == False):
			if iteration==60:
				iteration = 0
				fp = open('time2.txt', 'r')
				l = fp.read()
				hrs = int(l)
				fp.close()
				print datetime.now().time(), "Wait is still on... Its been", hrs, "hours"
				fp = open('time2.txt', 'w')
				fp.write(str(hrs+1))
				fp.close()
			waitTime(60)
			iteration+=1
