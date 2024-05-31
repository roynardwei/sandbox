import os

#全局变量
board = [[0 for i in range(0, 9)] for j in range(0, 9)]
player_row = 0
player_col = 0
cpu_row = 0
cpu_col = 0

def isPlayerWin():
    global  player_row
    global  player_col
    count = 1
    for i in range(1, 5):
        if player_row + i < 9 and isBlack(player_row + i, player_col):
            count += 1
        else:
            break
    for i in range(-1,-5,-1):
        if player_row + i > 0 and isBlack(player_row + i, player_col):
            count += 1
        else:
            break
    if count >= 5:
        return True

    count = 1
    for i in range(1, 5):
        if player_col + i < 9 and isBlack(player_row, player_col + i):
            count += 1
        else:
            break
    for i in range(-1,-5,-1):
        if player_col + i > 0 and isBlack(player_row, player_col + i):
            count += 1
        else:
            break
    if count >= 5:
        return True

    count = 1
    for i in range(-1,-5,-1):
        if player_row + i > 0 and player_col + i > 0 and isBlack(player_row + i,player_col + i):
            count += 1
        else:
            break
    for i in range(1, 5):
        if player_row + i < 9 and player_col + i < 9 and isBlack(player_row + i, player_col + i):
            count += 1
        else:
            break
    if count >= 5:
        return True

    count = 1
    for i in range(1, 5):
        if player_row+ i > 0 and player_col + i < 9 and isBlack(player_row + i, player_col + i):
            count += 1
        else:
            break
    for i in range(-1,-5,-1):
        if player_row + i < 9 and player_col + i > 0 and isBlack(player_row + i, player_col + i):
            count += 1
        else:
            break
    if count >= 5:
        return True
    return False

def isCPUWin():
    global  cpu_row
    global  cpu_col
    count = 1
    for i in range(1, 5):
        if cpu_row + i < 9 and isWhite(cpu_row + i, cpu_col):
            count += 1
        else:
            break
    for i in range(-1,-5,-1):
        if cpu_row + i > 0 and isWhite(cpu_row + i, cpu_col):
            count += 1
        else:
            break
    if count >= 5:
        return True

    count = 1
    for i in range(1, 5):
        if cpu_col + i < 9 and isWhite(cpu_row, cpu_col + i):
            count += 1
        else:
            break
    for i in range(-1,-5,-1):
        if cpu_col + i > 0 and isWhite(cpu_row, cpu_col + i):
            count += 1
        else:
            break
    if count >= 5:
        return True

    count = 1
    for i in range(-1,-5,-1):
        if cpu_row + i > 0 and cpu_col + i > 0 and isWhite(cpu_row + i,cpu_col + i):
            count += 1
        else:
            break
    for i in range(1, 5):
        if cpu_row + i < 9 and cpu_col + i < 9 and isWhite(cpu_row + i, cpu_col + i):
            count += 1
        else:
            break
    if count >= 5:
        return True

    count = 1
    for i in range(1, 5):
        if cpu_row+ i > 0 and cpu_col + i < 9 and isWhite(cpu_row + i, cpu_col + i):
            count += 1
        else:
            break
    for i in range(-1,-5,-1):
        if cpu_row + i < 9 and cpu_col + i > 0 and isWhite(cpu_row + i, cpu_col + i):
            count += 1
        else:
            break
    if count >= 5:
        return True
    return False

def isBlank(row, col):
    if board[row][col] == 0:
        return True
    return False

def isWhite(row, col):
    if board[row][col] == 1:
        return True
    return False

def isBlack(row, col):
    if board[row][col] == 2:
        return True
    return False

def down(row, col, is_player):
    if is_player:
      board[row][col] = 2
    else:
      board[row][col] = 1

def showBoard():
    os.system('cls')
    print('  1  2  3  4  5  6  7  8  9 ')
    for r in range(0, len(board)):
        data = str(r+1)
        for c in range(0, len(board[r])):
            if board[r][c] == 0:
                data += ' + '
            elif board[r][c] == 1:
                data += ' □ '
            else:
                data += ' ▲ '
        print(data)

def playerRound():
    global  player_row
    global  player_col
    player_input = input('你是黑子，请你输入行列来落子，例如:18 表示1行8列')
    player_row = int(player_input[0]) - 1
    player_col = int(player_input[1]) - 1
    down(player_row, player_col, True)

def cpuRound():
    hengPos1 = -1
    hengPos2 = 1
    continueCount = 1
    maxContinueCount = 1
    finnalyRow = 0
    finnalyCol = 0
    while player_col + hengPos1 > 0 and isBlack(player_row, player_col + hengPos1):
        continueCount += 1
        hengPos1 -= 1
    while player_col + hengPos2 < 9 and isBlack(player_row, player_col + hengPos2):
        continueCount += 1
        hengPos2 += 1

    if continueCount >= maxContinueCount:
        if isBlank(player_row, player_col + hengPos1):
            maxContinueCount = continueCount
            finnalyRow = player_row
            finnalyCol = player_col + hengPos1
        elif isBlank(player_row, player_col + hengPos2):
            maxContinueCount = continueCount
            finnalyRow = player_row
            finnalyCol = player_col+hengPos2

    shuPos1 = -1
    shuPos2 = 1
    continueCount = 1
    while player_row+ shuPos1 > 0 and isBlack(player_row + shuPos1, player_col):
        continueCount += 1
        shuPos1 -= 1
    while player_row + shuPos2 < 9 and isBlack(player_row + shuPos2, player_col):
        continueCount += 1
        shuPos2 += 1
    if continueCount >= maxContinueCount:
        if isBlank(player_row + shuPos1, player_col):
            maxContinueCount = continueCount
            finnalyRow = player_row + shuPos1
            finnalyCol = player_col
        elif isBlank(player_row + shuPos2, player_col):
            maxContinueCount = continueCount
            finnalyRow = player_row+shuPos2
            finnalyCol = player_col

    zuoShangRow = -1
    zuoShangCol = -1
    youXiaRow = 1
    youXiaCol = 1
    continueCount = 1
    while player_row + zuoShangRow > 0 and player_col + zuoShangCol > 0 and isBlack(
            player_row + zuoShangRow, player_col + zuoShangCol):
        continueCount += 1
        zuoShangRow -= 1
        zuoShangCol -= 1
    while player_row + youXiaRow < 9 and player_col + youXiaCol < 9 and isBlack(player_row + youXiaRow, player_col + youXiaCol):
        continueCount += 1
        youXiaRow += 1
        youXiaCol += 1
    if continueCount >= maxContinueCount:
        if isBlank(player_row + zuoShangRow, player_col + zuoShangCol):
            maxContinueCount = continueCount
            finnalyRow = player_row + zuoShangRow
            finnalyCol = player_col+ zuoShangCol
        elif isBlank(player_row + youXiaRow, player_col + youXiaCol):
            maxContinueCount = continueCount
            finnalyRow = player_row + youXiaRow
            finnalyCol = player_col + youXiaCol

    zuoXiaRow = 1
    zuoXiaCol = -1
    youShangRow = -1
    youShangCol = 1
    continueCount = 1
    while player_row+ zuoXiaRow < 9 and player_col + zuoXiaCol > 0 and isBlack(
        player_row + zuoXiaRow, player_col + zuoXiaCol):
        continueCount += 1
        zuoXiaRow += 1
        zuoXiaCol -= 1
    while player_row + youShangRow > 0 and player_col + youShangCol < 9 and isBlack(
            player_row + youShangRow, player_col + youShangCol):
        continueCount += 1
        youShangRow -= 1
        youShangCol += 1

    if continueCount >= maxContinueCount:
        if isBlank(player_row + zuoXiaRow, player_col + zuoXiaCol):
            maxContinueCount = continueCount
            finnalyRow = player_row + zuoXiaRow
            finnalyCol = player_col + zuoXiaCol
        elif isBlank(player_row + youShangRow, player_col + youShangCol):
            maxContinueCount = continueCount
            finnalyRow = player_row + youShangRow
            finnalyCol = player_col + youShangCol
    down(finnalyRow, finnalyCol, False)

while True:
    showBoard()
    playerRound()  #玩家的回合 下黑子
    if isPlayerWin():
        print('恭喜！你赢了！')
        break
    cpuRound()  #电脑的回合 下白子
    if isCPUWin():
        print('哎！你输了！')
        break