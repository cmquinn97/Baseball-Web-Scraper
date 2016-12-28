import requests, bs4
import openSheet

sheet = openSheet.wks.worksheet("MinorLeagueBall")

def scrapeMIB():
    #opens site (computer language)
    hdr = {'Accept': 'text/html,application/xhtml+xml,*/*',
           "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
    site = requests.get('http://www.minorleagueball.com/2016/9/24/12932956/top-100-prospects-end-of-2016', headers = hdr)
    site.raise_for_status()

    #opens site (human language)
    siteSoup = bs4.BeautifulSoup(site.text, 'html.parser')

    #Adds players to google sheet
    #Skips some players becuase of weird website formatting. Inserted them manually
    for players in siteSoup.findAll("b"):
        try:
            name, pos, team, grade = players.text.split(',')
            rank = name[:3]
            if rank[1] == ")":
                rank = rank[0]
            if rank[0] == " ":
                rank = rank[1:]
            if len(rank)> 1:
                if rank[2] == ")":
                    rank = rank[:2]
            rank = int(rank) +1
            name = name[3:]
            if name[0] == " ":
                name=name[1:]
            if name[0]==")":
                name = name[2:]
            print(name + " " + rank)
            sheet.update_acell("A"+str(rank), name)
        except:
            continue

    # Adds teams to google sheet
    # Skips some teams becuase of weird website formatting. Inserted them manually
    for players in siteSoup.findAll("b"):
        try:
            name, pos, team, grade = players.text.split(',')
            rank = name[:3]
            if rank[1] == ")":
                rank = rank[0]
            if rank[0] == " ":
                rank = rank[1:]
            if len(rank)> 1:
                if rank[2] == ")":
                    rank = rank[:2]
            rank = int(rank) + 1
            print(team + " " + str(rank))
            sheet.update_acell("C" + str(rank), team)
        except:
            continue

        # Adds positions to google sheet
        # Skips some positions becuase of weird website formatting. Inserted them manually
    for players in siteSoup.findAll("b"):
        try:
            name, pos, team, grade = players.text.split(',')
            rank = name[:3]
            if rank[1] == ")":
                rank = rank[0]
            if rank[0] == " ":
                rank = rank[1:]
            if len(rank) > 1:
                if rank[2] == ")":
                    rank = rank[:2]
            rank = int(rank) + 1
            print(pos + " " + str(rank))
            sheet.update_acell("B" + str(rank), pos)
        except:
            continue


scrapeMIB()