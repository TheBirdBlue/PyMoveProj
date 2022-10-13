from os import path as path
import sqlite3 as sdb
from enemyDict import enemy
from playerDict import player
from itemDict import item

dictList = [enemy, player, item]

def buildDB():

    sqlEnemy = 'INSERT INTO enemy (name, rank, hp, attack, defense, special, skillOne, skillTwo, skillThree)' \
               ' values (?, ?, ?, ?, ?, ?, ?, ?, ?)'
    sqlPlayer = 'INSERT INTO player (name, rank, level, hp, sp, attack, defense, special, experience, skillOne, skillTwo, skillThree)' \
                ' values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    sqlProgress = 'INSERT INTO progress (name, rank, level, hp, sp, attack, defense, special, experience, skillOne, skillTwo, skillThree)' \
                ' values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    sqlBag = 'INSERT INTO bag (name, rank, effect, value, price, inventory) values (?, ?, ?, ?, ?, 3)'
    sqlStorage = 'INSERT INTO storage (name, rank, effect, value, price, inventory) values (?, ?, ?, ?, ?, 0)'
    sqlShop = 'INSERT INTO shop (name, rank, effect, value, price) values (?, ?, ?, ?, ?)'
    sqlDropTable = 'INSERT INTO droptable (name, rank, effect, value, price) values (?, ?, ?, ?, ?)'
    '''sqlList = [sqlBag, sqlDropTable, sqlStorage, sqlEnemy, sqlPlayer, sqlShop]'''

    sqlList = [sqlEnemy, sqlPlayer, sqlProgress, sqlBag, sqlStorage, sqlShop, sqlDropTable]


    dbConnect = sdb.connect('infoDB.db')

    # Create and connect to database
    with dbConnect:

        try:
            dbConnect.execute("""
                CREATE TABLE enemy (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    rank INTEGER,
                    hp INTEGER,
                    attack INTEGER,
                    defense INTEGER,
                    special INTEGER,
                    skillOne INTEGER,
                    skillTwo INTEGER,
                    skillThree INTEGER
                ) ;
            """)

            # Initial build enemy DB
            # Go through key values in dictionary and add to data
            dict = dictList[0]
            sql = sqlList[0]
            for x, y in dict.items():
                data = []
                for a, b in y.items():
                    data.append(b)

                # Connect to database and add data values to one line
                # Loops back to next sql in queue
                dbConnect.executemany(sql, (data,))

        except:
            pass

        try:
            dbConnect.execute("""
                CREATE TABLE player (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    rank INTEGER,
                    level INTEGER,
                    hp INTEGER,
                    sp INTEGER,
                    attack INTEGER,
                    defense INTEGER,
                    special INTEGER,
                    experience INTEGER,
                    skillOne INTEGER,
                    skillTwo INTEGER,
                    skillThree INTEGER
                ) ;
            """)

            # Initial build player DB
            # Pulls first ID from player DB to give first player
            dict = dictList[1]
            sql = sqlList[1]
            for x, y in dict.items():
                data = []
                for a, b in y.items():
                    data.append(b)

                # Connect to database and add data values to one line
                # Loops back to next sql in queue
                dbConnect.executemany(sql, (data,))

        except:
            pass

        try:
            dbConnect.execute("""
                CREATE TABLE progress (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    rank INTEGER,
                    level INTEGER,
                    hp INTEGER,
                    sp INTEGER,
                    attack INTEGER,
                    defense INTEGER,
                    special INTEGER,
                    experience INTEGER,
                    skillOne INTEGER,
                    skillTwo INTEGER,
                    skillThree INTEGER
                ) ;
            """)

            # Initial build progress DB
            # Go through key values in database and add to data
            sql = sqlList[2]
            dataGrab = dbConnect.execute("SELECT * FROM player WHERE id = 1")
            for row in dataGrab:
                data = list(row)
                data.pop(0)

            dbConnect.executemany(sql, (data,))

        except:
            pass

        try:
            dbConnect.execute("""
                CREATE TABLE shop (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    rank INTEGER,
                    effect TEXT,
                    value INTEGER,
                    price INTEGER
                ) ;
            """)

            # Initial build shop DB
            dict = dictList[2]
            sql = sqlList[5]
            for x, y in dict.items():
                data = []
                for a, b in y.items():
                    data.append(b)

                # Connect to database and add data values to one line
                # Loops back to next sql in queue
                dbConnect.executemany(sql, (data,))

        except:
            pass

        try:
            dbConnect.execute("""
                CREATE TABLE bag (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    rank INTEGER,
                    effect TEXT,
                    value INTEGER,
                    price INTEGER,
                    inventory INTEGER
                ) ;
            """)

            # Adds starting inventory in BAG
            sql = sqlList[3]
            dataGrab = dbConnect.execute("SELECT * FROM shop WHERE id = 1")
            for row in dataGrab:
                data = list(row)
                data.pop(0)

            dbConnect.executemany(sql, (data,))

            dataGrab = dbConnect.execute("SELECT * FROM shop WHERE id = 2")
            for row in dataGrab:
                data = list(row)
                data.pop(0)

            dbConnect.executemany(sql, (data,))

        except:
            pass

        try:
            dbConnect.execute("""
                CREATE TABLE storage (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    rank INTEGER,
                    effect TEXT,
                    value INTEGER,
                    price INTEGER,
                    inventory INTEGER
                ) ;
            """)

        except:
            pass

        try:
            dbConnect.execute("""
                CREATE TABLE droptable (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    rank INTEGER,
                    effect TEXT,
                    value INTEGER,
                    price INTEGER
                ) ;
            """)

        except:
            pass
