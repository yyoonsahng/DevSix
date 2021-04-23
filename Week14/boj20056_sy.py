import copy

N, M, K = list(map(int, input().split()))

board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    ri, ci, mi, si, di = list(map(int, input().split()))
    board[ri-1][ci-1].append((mi, si, di))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def getMovedCoordi(x, y, ball):
    global N
    (_, s, d) = ball
    nx = (x + dx[d] * s) % N
    ny = (y + dy[d] * s) % N
    return nx, ny


for i in range(K):
    newBoard = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if len(board[x][y]) == 0:
                continue
            for ball in board[x][y]:
                nx, ny = getMovedCoordi(x, y, ball)
                newBoard[nx][ny].append(ball)

    for x in range(N):
        for y in range(N):
            if len(newBoard[x][y]) >= 2:
                shouldSplitBallList = newBoard[x][y]
                sum_m, sum_s = 0, 0
                isSame = True
                isEven = shouldSplitBallList[0][2] % 2
                for ball in shouldSplitBallList:
                    sum_m += ball[0]
                    sum_s += ball[1]
                    if isSame and isEven != ball[2] % 2:
                        isSame = False
                nm = sum_m // 5
                newBoard[x][y] = []
                if nm == 0:
                    continue
                ns = sum_s // len(shouldSplitBallList)
                nd = [0, 2, 4, 6] if isSame else [1, 3, 5, 7]
                for d in nd:
                    newBoard[x][y].append((nm, ns, d))

    board = copy.deepcopy(newBoard)

total_sum_m = 0
for x in range(N):
    for y in range(N):
        unit_sum = 0
        for ball in board[x][y]:
            unit_sum += ball[0]
        total_sum_m += unit_sum

print(total_sum_m)
