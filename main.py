import requests, bs4
import openSheet
sheet = openSheet.wks
#This program Scrapes a website for the top fantasy prospects

#Opens the site (computer language)
site = requests.get('http://www.baseballamerica.com/minors/midseason-top-100-prospects/#ek0SY6JFtSUcwTlb.97')
site.raise_for_status()

#opens the site (human language)
siteSoup = bs4.BeautifulSoup(site.text, 'html.parser')

#singles out the players on the site
sitePlayers = siteSoup.select('tbody tr')

#Formats the header for each column
i=0
for players in siteSoup.findAll('td')[:5]:
    i+=1
    sheet.update_cell(1,i, players.getText())

#Prints players and info in appropriate cells
i=0
x=2
for players in siteSoup.findAll('td')[5:]:
    i+=1
    sheet.update_cell(x,i, players.getText())
    if i%5 == 0:
        x+=1
        i=0



print('Your worksheet is filled out')