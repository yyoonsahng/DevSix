from collections import deque

N, K = map(int, input().split())
status = []
virus = []
for i in range(N):
    line = list(map(int, input().split()))
    status.append(line)
    for j in range(len(line)):
        if line[j] >= 1:
            virus.append((line[j], (i, j)))
virus.sort()
S, X, Y = map(int, input().split())


queue = deque([])
for v in range(K):
    # 바이러스 위치, 시간
    queue.append((virus[v][1], 0))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while queue:
    c = queue.popleft()
    time = c[1]
    if time == S:
        break
    x, y = c[0][0], c[0][1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if status[nx][ny] == 0:
                status[nx][ny] = status[x][y]
                queue.append(((nx, ny), time + 1))

print(status[X - 1][Y - 1])

