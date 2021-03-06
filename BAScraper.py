import requests, bs4
import openSheet

sheet = openSheet.wks.worksheet("BaseballAmerica")

def scrapeBA():
    # This program Scrapes a website for the top fantasy prospects

    # Opens the site (computer language)
    site = requests.get('http://www.baseballamerica.com/minors/midseason-top-100-prospects/#ek0SY6JFtSUcwTlb.97')
    site.raise_for_status()

    # opens the site (human language)
    siteSoup = bs4.BeautifulSoup(site.text, 'html.parser')

    # singles out the players on the site
    sitePlayers = siteSoup.select('tbody tr')

    # Formats the header for each column
    i = 0
    for players in siteSoup.findAll('td')[:5]:
        i += 1
        sheet.update_cell(1, i, players.getText())

    # Prints players and info in appropriate cells
    i = 0
    x = 2
    for players in siteSoup.findAll('td')[5:]:
        i += 1
        sheet.update_cell(x, i, players.getText())
        if i % 5 == 0:
            x += 1
            i = 0

    # Removes the numbers from the player row
    sheetList = sheet.range("A2:A101")
    i = 1
    for player in sheetList:
        i += 1
        play = player.value[3:]
        sheet.update_acell('A' + str(i), play)

    print('Your worksheet is filled out')


def removeVid():
    removeList = sheet.range('E1:E101')
    print("Removing the videos column...")
    for remove in removeList:
        remove.value = ''
    sheet.update_cells(removeList)
    print("Videos column removed.")