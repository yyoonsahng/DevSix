from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(arr, q, S):
    while q:
        v = q.popleft()
        y, x = v[0]
        time = v[1]
        if time == S:
            break
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] == 0:
                    q.append(((ny, nx), time + 1))
                    arr[ny][nx] = arr[y][x]


N, K = map(int, input().split())
status = []
virus = []
for i in range(N):
    line = list(map(int, input().split()))
    status.append(line)
    for j in range(len(line)):
        if line[j] >= 1:
            # 바이러스 번호, 위치(y, x)
            virus.append((line[j], (i, j)))
virus.sort()

S, X, Y = map(int, input().split())
queue = deque([])
for vi in virus:
    num = vi[0]
    vy, vx = vi[1]
    # 바이러스의 위치(y, x), 시간
    queue.append((vi[1], 0))
bfs(status, queue, S)
print(status[X - 1][Y - 1])

