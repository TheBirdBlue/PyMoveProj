topLine = ' ╔══════════════════════════════╗'
endCap = '║'
bottomLine = ' ╚══════════════════════════════╝'

def printMap(positionPlayer, positionEnemy):

    print(positionPlayer, positionEnemy)
    print(topLine)
    sameLine = False

    # Find Y Position
    for y in range(0,10):
        line = ''

        # For when player and enemy on the same line
        if positionPlayer[1] == y and positionEnemy[1] == y:
            sameLine = True
            line += ' ' + endCap

            for x in range(0, 30):
                if x == positionPlayer[0]:
                    line += '0'
                elif x == positionEnemy[0]:
                    line += 'X'
                else:
                    line += '.'

            line += endCap

        if positionPlayer[1] != y and positionEnemy[1] != y:
            line = ' ' + endCap + '.' * 30 + endCap

        # Find Y Position for player
        if positionPlayer[1] == y and sameLine == False:
            line += ' ' + endCap

            # Find X Position for Player:
            for x in range(0, 30):
                if x == positionPlayer[0]:
                    line += 'O'

                else:
                    line += '.'

            line += endCap

        # Find Y Position of enemy
        if positionEnemy[1] == y and sameLine == False:
            line += ' ' + endCap

            # Find X Position of enemy
            for x in range(0, 30):
                if x == positionEnemy[0]:
                    line += 'X'

                else:
                    line += '.'

            line += endCap

        print(line)

    print(bottomLine)

def enemyMove(positionPlayer, positionEnemy):
    x = positionPlayer[0]
    y = positionPlayer[1]
    a = positionEnemy[0]
    b = positionEnemy[1]
    aDelta = 0
    bDelta = 0

    if x < a and y < b:
        aDelta -= 1
        bDelta -= 1
        positionEnemy = [a, b]

    elif x > a and y > b:
        aDelta += 1
        bDelta += 1
        positionEnemy = [a, b]

    elif x < a:
        aDelta -= 1
        positionEnemy = [a, b]

    elif x > a:
        aDelta += 1
        positionEnemy = [a, b]

    elif y < b:
        bDelta -= 1
        positionEnemy = [a, b]

    elif y > b:
        bDelta += 1
        positionEnemy = [a, b]

    return aDelta, bDelta
