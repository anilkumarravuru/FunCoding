#anilkumarravuru
import urllib2,cookielib
import time
import webbrowser
from datetime import datetime


def waitTime(t):
	endTime = time.time() + t
	while(time.time() < endTime):
		anil = 1
	return

hyderabad_url_30 = "https://in.bookmyshow.com/buytickets/saaho-hyderabad/movie-hyd-ET00056595-MT/20190830"
hyderabad_url_31 = "https://in.bookmyshow.com/buytickets/saaho-hyderabad/movie-hyd-ET00056595-MT/20190831"
hyderabad_url_1 = "https://in.bookmyshow.com/buytickets/saaho-hyderabad/movie-hyd-ET00056595-MT/20190901"
hyderabad_song = "Happy.mp3"
chrome_path = "open -a /Applications/Google\ Chrome.app %s"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

iteration = 1
while True:
	flag = False
	try:
		hyd_req_30 = urllib2.Request(hyderabad_url_30, headers=hdr)
		hyderabad_html_30 = urllib2.urlopen(hyd_req_30).read()
		hyd_req_31 = urllib2.Request(hyderabad_url_31, headers=hdr)
		hyderabad_html_31 = urllib2.urlopen(hyd_req_31).read()
		hyd_req_1 = urllib2.Request(hyderabad_url_1, headers=hdr)
		hyderabad_html_1 = urllib2.urlopen(hyd_req_1).read()
		# bangalore_html = ''
	except:
		print '-----------', datetime.now().time(),'something wrong with connection or urls'
		waitTime(60)
		flag = True
	if flag== False:
		# now_count = hyderabad_html_26.count('data-showtime-code')
		# if prev_count_26 != now_count:
		# 	print "New show added in Hyderabad on 26th", prev_count_26, now_count
		# 	webbrowser.get(chrome_path).open_new(hyderabad_song)
		# 	prev_count_26 = now_count
		# now_count = hyderabad_html_27.count('data-showtime-code')
		# if prev_count_27 != now_count:
		# 	print "New show added in Hyderabad on 27th", prev_count_27, now_count
		# 	webbrowser.get(chrome_path).open_new(hyderabad_song)
		# 	prev_count_27 = now_count
		# now_count = hyderabad_html_28.count('data-showtime-code')
		# if prev_count_28 != now_count:
		# 	print "New show added in Hyderabad on 28th", prev_count_28, now_count
		# 	webbrowser.get(chrome_path).open_new(hyderabad_song)
		# 	prev_count_28 = now_count
		if 'INOX: GVK One, Banjara Hills' in hyderabad_html_30 or 'Prasads' in hyderabad_html_30:
			print 'Good shows opened for Sahoo for friday'
			webbrowser.get(chrome_path).open_new(hyderabad_song)
		if 'INOX: GVK One, Banjara Hills' in hyderabad_html_31 or 'Prasads' in hyderabad_html_31:
			print 'Good shows opened for Sahoo for saturday'
			webbrowser.get(chrome_path).open_new(hyderabad_song)
		if 'INOX: GVK One, Banjara Hills' in hyderabad_html_1 or 'Prasads' in hyderabad_html_1:
			print 'Good shows opened for Sahoo for sunday'
			webbrowser.get(chrome_path).open_new(hyderabad_song)
		if iteration==60:
			iteration = 0
			fp = open('saaho_hyd.txt', 'r')
			l = fp.read()
			hrs = int(l)
			fp.close()
			print datetime.now().time(), "Wait is still on... Its been", hrs, "hours"
			fp = open('saaho_hyd.txt', 'w')
			fp.write(str(hrs+1))
			fp.close()
		waitTime(60)
		iteration+=1