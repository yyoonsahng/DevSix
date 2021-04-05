import copy


def rollDice(d):
    global dice
    temp = copy.deepcopy(dice)
    if d == 1:  # east
        dice[1] = temp[4]
        dice[3] = temp[1]
        dice[4] = temp[6]
        dice[6] = temp[3]
    elif d == 2: # west
        dice[1] = temp[3]
        dice[3] = temp[6]
        dice[4] = temp[1]
        dice[6] = temp[4]
    elif d == 3: # north
        dice[1] = temp[5]
        dice[2] = temp[1]
        dice[5] = temp[6]
        dice[6] = temp[2]
    elif d == 4: # south
        dice[1] = temp[2]
        dice[2] = temp[6]
        dice[5] = temp[1]
        dice[6] = temp[5]

    return


N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
inputs = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]  # 3: north, 4: south
dy = [0, 1, -1, 0, 0]  # 1: east, 2: west
dice = [0 for _ in range(7)]
for i in range(K):
    d = inputs[i]
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    rollDice(d)

    if board[nx][ny] == 0:
        board[nx][ny] = dice[6]
    else:
        dice[6] = board[nx][ny]
        board[nx][ny] = 0
    print(dice[1])
    x = nx
    y = ny
