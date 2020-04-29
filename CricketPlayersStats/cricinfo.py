# AnilKumarRavuru

import urllib2, cookielib
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def getPlayerStats(playerUrl):
	cricbuzzRequest = urllib2.Request(playerUrl, headers = header)
	playerContent = BeautifulSoup(urllib2.urlopen(cricbuzzRequest).read(), features = 'lxml')
     playerStatsTable = playerContent.find('table').findAll('tr')[1:]
     for row in playerStatsTable:
          columns = [data.text for data in row.findAll('td')[0:]]
          print columns

# Main class

playerProfileFileName = 'playerIdList.txt'
cricinfoPlayerBaseUrl = 'http://www.espncricinfo.com/india/content/player/'

with open(playerProfileFileName, 'r') as profiles:
    for line in profiles:
      lineSplit = line.split()
      playerCode = lineSplit[-1]
      playerName = ''.join(lineSplit[:-1])
      playerProfileUrl = cricinfoPlayerBaseUrl + playerCode + '.html'
      print playerProfileUrl
      getPlayerStats(playerProfileUrl)