import openSheet

sheet = openSheet.wks.worksheet("Combined")
baSheet = openSheet.wks.worksheet("BaseballAmerica")
mlbSheet = openSheet.wks.worksheet("MLB")
mibSheet = openSheet.wks.worksheet("MinorLeagueBall")

names = baSheet.range("A2:A101")
names2 = mlbSheet.range("A2:A101")
names3 = mibSheet.range("A2:A101")

def combine():
    class Player(object):
        def __init__(self, playerName):
            self.playerName = str(playerName)
            self.points = 0

    players = []
    for name in names:
        players.append(Player(name.value))

    count = 0
    for name in names:
        try:
            activePlayer = Player(name.value)
            point = name.row
            match = mlbSheet.find(activePlayer.playerName[1:])
            point2 = match.row
            match2 = mibSheet.find(activePlayer.playerName[1:])
            point3 = match2.row
            activePlayer.points = point+point2+point3
            players[count] = activePlayer
            count+=1
            #print(activePlayer.playerName + " " + str(activePlayer.points))
        except:
            print("This player is not on all lists")
            continue
    players.sort(key = lambda x: x.points)
    row = 1
    for player in players:
        if player.points > 1:
            row += 1
            sheet.update_acell("A"+str(row), player.playerName)
            print(player.playerName + " " + str(player.points))