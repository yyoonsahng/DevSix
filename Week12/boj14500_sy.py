# 19 blocks
blocks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],

    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 1), (2, 0), (2, 1)],
    [(0, 2), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],

    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (1, 1), (2, 0)],
    [(0, 1), (0, 2), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],

    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 1)]
]


def getSum(x, y, block, board, N, M):
    sum = 0
    for i in range(4):
        nx = x + block[i][0]
        ny = y + block[i][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            return 0
        sum += board[nx][ny]
    return sum


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for x in range(N):
    for y in range(M):
        for block in blocks:
            answer = max(answer, getSum(x, y, block, board, N, M))

print(answer)
