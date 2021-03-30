def makeNewBoard(board):
    return board


def isSameNumber(n, board):
    currentN = n
    for h in range(H):
        if board[h][currentN] == 2:
            currentN += 1
        elif currentN - 1 >= 0 and board[h][currentN - 1] == 2:
            currentN -= 1
    return True if currentN == n else False


def checkAll(board):
    # check all n go to number n
    for n in range(N):
        result = isSameNumber(n, board)
        if result == False:
            return False
    return True


N, M, H = map(int, input().split())

board = [[0] * N for i in range(H)]

for i in range(M):
    h, n = map(int, input().split())
    board[h-1][n-1] = 2
    board[h-1][n-2] = 1 if n-2 >= 0 else 0  # left
    board[h-1][n] = 1 if n < N else 0  # right
    # can't place line if board[][] > 0

answer = -1
for lineCount in range(4):
    # add line (bfs?dfs?)
    newBoard = makeNewBoard(board)
    result = checkAll(newBoard)
    if result:
        answer = lineCount
        break

print(answer)
