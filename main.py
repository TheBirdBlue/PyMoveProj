#!/usr/bin/python

import sys

sys.path.insert(0, './func_modules')
sys.path.insert(1, './func_modules/dicts')

import time
import common
import buildDataBase
import printMap
import battleFunction

run = True

startingPositionPlayer = [0, 0]
startingPositionEnemy = [29, 9]

def gameLoop():

    buildDataBase.buildDB()

    x = startingPositionPlayer[0]
    y = startingPositionPlayer[1]
    a = startingPositionEnemy[0]
    b = startingPositionEnemy[1]

    # Begin game loop
    while run:

        positionPlayer = [x, y]
        positionEnemy = [a, b]

        common.clear()
        printMap.printMap(positionPlayer, positionEnemy)

        if (a - 1) == x and (b - 1) == y or a == x and (b - 1) == y or (a + 1) == x and (b - 1) == y or \
            (a - 1) == x and b == y or (a + 1) == x and b == y or (a + 1) == x and (b - 1) == y or \
            a == x and (b - 1) == y or (a + 1) == x and (b + 1) == y:
            print('The battle begins!')
            time.sleep(1)
            battleFunction.battleProcess()


        print('              ▲  ▲  ▲\n'
              '            ◄ 7  8  9 ►\n'
              '            ◄ 4  ■  6 ►\n'
              '            ◄ 1  2  3 ►\n'
              '              ▼  ▼  ▼\n')

        direction = input(' Action input: ')

        if direction == '7':
            if y == 0 or x == 0:
                print(" There's a wall in the way.")
                time.sleep(1)
            else:
                y -= 1
                x -= 1

        elif direction == '8':
            if y == 0:
                print(" There's a wall in the way.")
                time.sleep(1)
            else:
                y -= 1

        elif direction == '9':
            if y == 0 or x == 29:
                print(" There's a wall in the way.")
                time.sleep(1)
            else:
                y -= 1
                x += 1

        elif direction == '4':
            if x == 0:
                print(" There's a wall in the way.")
                time.sleep(1)
            else:
                x -= 1

        elif direction == '5':
            print(' Waiting...')
            time.sleep(1)

        elif direction == '6':
            if x == 29:
                print(" There's a wall in the way.")
                time.sleep(1)
            else:
                x += 1

        elif direction == '1':
            if y == 9 or x == 0:
                print(" There's a wall in the way.")
                time.sleep(1)
            else:
                y += 1
                x -= 1

        elif direction == '2':
            if y == 9:
                print(" There's a wall in the way.")
                time.sleep(1)
            else:
                y += 1

            print(x, y)

        elif direction == '3':
            if y == 9 or x == 29:
                print(" There's a wall in the way.")
                time.sleep(1)
            else:
                y += 1
                x += 1

        else:
            print(' Invalid direction.')
            time.sleep(1)

        enemyAction = printMap.enemyMove(positionPlayer, positionEnemy)
        a += enemyAction[0]
        b += enemyAction[1]

gameLoop()
