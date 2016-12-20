import requests,bs4
from bs4 import BeautifulSoup
from selenium import webdriver
import openSheet

#This program Scrapes a website for the top fantasy prospects

sheet = openSheet.wks.worksheet("MLB")
chrome_path = r'C:/Users/Chris/Desktop/chromedriver.exe'

#Opens the site
driver = webdriver.Chrome(chrome_path)
driver.get("http://m.mlb.com/prospects/2016")

#Singles out the players names
content = driver.find_elements_by_class_name('player-name')


#updats google sheet with scraped info
i=1
print("Filling out sheet...")
for players in content:
    i+=1
    #Checks if player has 2 or 3 names, and updates google sheet
    if players.text.count(" ") == 2:
        first, middle, last = players.text.split(" ")
        sheet.update_acell('A' + str(i), first.lower().capitalize() + " " +middle.lower().capitalize() + " " + last.lower().capitalize())
    else:
        first, last = players.text.split(" ")
        sheet.update_acell('A'+str(i), first.lower().capitalize() + " " + last.lower().capitalize())



print('Your worksheet is filled out')