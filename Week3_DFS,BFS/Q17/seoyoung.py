from collections import deque

N, K = map(int, input().split())

board = []
data = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] != 0:
            # save virus type, sec, x, y
            data.append((board[i][j], 0, i, j))

S, X, Y = map(int, input().split())

data.sort()
q = deque(data)

# define accessible direction
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# start BFS
while q:
    virusType, sec, x, y = q.popleft()
    if sec == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # out of bound
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] == 0:
            board[nx][ny] = virusType
            q.append((virusType, sec + 1, nx, ny))


print(board[X-1][Y-1])
