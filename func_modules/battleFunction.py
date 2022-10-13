import time
import random
import common
import sqlite3 as sdb

def pullStatsPlayer():

    selection = False
    dbConnect = sdb.connect('infoDB.db')
    dataGrab = dbConnect.execute("SELECT * FROM progress")
    playerChoice = []

    # Shows available character options
    while selection == False:
        common.clear()
        print(' Pick your hero! \n')
        for row in dataGrab:
            data = list(row)
            print(data)
            data.pop(0)
            playerChoice.append(data)

        playerSelection = input(' Which character will you summon? ')

        # Checks player input for integer and returns selection

        try:
            playerSelection = int(playerSelection) - 1

            if playerSelection in range(0, len(playerChoice) + 1):
                selection = True
                return playerChoice[playerSelection - 1]

            else:
                print(' Invalid choice.')
        except:
            print(' Invalid choice.')
            time.sleep(1)

def pullStatsEnemy(rank):

    dbConnect = sdb.connect('infoDB.db')
    enemyChoice = []
    for x in range(1, rank + 1):
        dataGrab = dbConnect.execute("SELECT * FROM enemy WHERE rank = " + str(x))
        for row in dataGrab:
            data = list(row)
            data.pop(0)
            enemyChoice.append(data)

    enemySelection = random.randrange(0, len(enemyChoice) + 1)
    return enemyChoice[enemySelection - 1]

def battleProcess():

    # Initialize Variables
    enemyInfo = {
        "enemyName": '',
        "enemyRank": 0,
        "enemyHP": 0,
        "enemyAtk": 0,
        "enemyDef": 0,
        "enemySpe": 0,
        "enemySkill1": 0,
        "enemySkill2": 0,
        "enemySkill3": 0
    }

    playerInfo = {
        "playerName": '',
        "playerRank": 0,
        "playerLevel": 0,
        "playerHP": 0,
        "playerSP": 0,
        "playerAtk": 0,
        "playerDef": 0,
        "playerSpe": 0,
        "playerSkill1": 0,
        "playerSkill2": 0,
        "playerSkill3": 0
    }

    playerPull = pullStatsPlayer()
    for dictItem, playerItem in zip(playerInfo, playerPull):
        playerInfo[dictItem] = playerItem

    enemyPull = pullStatsEnemy(playerInfo.get('playerRank'))
    for dictItem, enemyItem in zip(enemyInfo, enemyPull):
        playerInfo[dictItem] = enemyItem
