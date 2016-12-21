import requests,bs4
from bs4 import BeautifulSoup
from selenium import webdriver
import openSheet

#This program Scrapes a website for the top fantasy prospects

def scrapeMLB():
    sheet = openSheet.wks.worksheet("MLB")
    sheet2 = openSheet.wks.worksheet("BaseballAmerica")
    chrome_path = r'C:/Users/Chris/Desktop/chromedriver.exe'

    # Opens the site
    driver = webdriver.Chrome(chrome_path)
    driver.get("http://m.mlb.com/prospects/2016")

    # Singles out the players names
    content = driver.find_elements_by_class_name('player-name')

    # updates google sheet with scraped info
    i = 1
    print("Filling out sheet...")
    for players in content:
        i += 1
        # Checks if player has 2 or 3 names, and updates google sheet
        if players.text.count(" ") == 2:
            first, middle, last = players.text.split(" ")
            sheet.update_acell('A' + str(i),
                               first.lower().capitalize() + " " + middle.lower().capitalize() + " " + last.lower().capitalize())
        else:
            first, last = players.text.split(" ")
            sheet.update_acell('A' + str(i), first.lower().capitalize() + " " + last.lower().capitalize())

    # Scrapes the baseball america list to scrape the positions as it is easier than doing it from the website
    sheetCell = 1
    sheetList = sheet.range("A2:A101")
    sheet2List = sheet2.range("A2:A101")
    for player in sheetList:
        sheetCell += 1
        try:
            match = sheet2.find(" " + player.value)
            matchRow = match.row
            print(match.value)
            sheet.update_acell('B' + str(sheetCell), sheet2.acell('B' + str(matchRow)).value)
        except:
            print("That player was not on Baseball Americas list")
            pass

    # Scrapes the baseball america list to scrape the teams as it is easier than doing it from the website
    sheetCell = 1
    sheetList = sheet.range("A2:A101")
    sheet2List = sheet2.range("A2:A101")
    for player in sheetList:
        sheetCell += 1
        try:
            match = sheet2.find(" " + player.value)
            matchRow = match.row
            print(match.value)
            sheet.update_acell('C' + str(sheetCell), sheet2.acell('C' + str(matchRow)).value)
        except:
            print("That player was not on Baseball Americas list")
            pass

    print('Your worksheet is filled out')