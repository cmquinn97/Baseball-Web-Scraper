import requests, bs4

#This program Scrapes a website for the top fantasy prospects

#Opens the site (computer language)
site = requests.get('http://www.baseballamerica.com/minors/midseason-top-100-prospects/#ek0SY6JFtSUcwTlb.97')
site.raise_for_status()

#opens the site (human language)
siteSoup = bs4.BeautifulSoup(site.text, 'html.parser')

#singles out the players on the site
sitePlayers = siteSoup.select('tbody tr')

#goes through the players on the site, and prints them
for players in sitePlayers[1:11]:
     print(players.getText())