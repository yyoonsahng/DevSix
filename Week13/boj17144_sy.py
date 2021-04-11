import copy

R, C, T = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(R)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for i in range(T):
    n_board = [[0] * C for _ in range(R)]
    lowerMachineR = 0
    # spreading
    for r in range(R):
        for c in range(C):
            amount = board[r][c]
            if amount == -1:
                n_board[r][c] = -1
                lowerMachineR = r
                continue
            spreadCount = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr >= 0 and nr < R and nc >= 0 and nc < C and board[nr][nc] != -1:
                    n_board[nr][nc] += amount // 5
                    spreadCount += 1
            n_board[r][c] += (amount - (amount // 5) * spreadCount)

    board = copy.deepcopy(n_board)

    # cleaning
    upperMachineR = lowerMachineR - 1
    for i in range(C):
        n_board[upperMachineR][i] = board[upperMachineR][i -
                                                         1] if i != 0 and board[upperMachineR][i-1] != -1 else 0
        n_board[0][C - i - 1] = board[0][C - i] if i != 0 else board[1][C - 1]

        n_board[lowerMachineR][i] = board[lowerMachineR][i -
                                                         1] if i != 0 and board[lowerMachineR][i-1] != -1 else 0
        n_board[R - 1][C - i - 1] = board[R-1][C -
                                               i] if i != 0 else board[R-2][C - 1]
    for i in range(1, upperMachineR):
        n_board[i][0] = board[i-1][0]
        n_board[i][C - 1] = board[i+1][C-1]

    for i in range(lowerMachineR + 1, R - 1):
        n_board[i][0] = board[i+1][0]
        n_board[i][C - 1] = board[i-1][C-1]

    n_board[upperMachineR][0] = n_board[lowerMachineR][0] = -1

    board = copy.deepcopy(n_board)


total = 2
for r in range(R):
    total += sum(board[r])
print(total)
