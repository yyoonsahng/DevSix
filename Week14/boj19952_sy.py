import sys
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
t = int(sys.stdin.readline())
for _ in range(t):
    h, w, o, f, sy, sx, ey, ex = map(int, sys.stdin.readline().split())
    arr = [[0 for _ in range(w)] for _ in range(h)]
    visit = [[False for _ in range(w)] for _ in range(h)]
    for i in range(o):
        y, x, l = map(int, sys.stdin.readline().split())
        arr[y-1][x-1] = l

    q = deque()
    q.append((sx-1, sy-1, f))
    visit[0][0] = True
    success = False
    while q:
        x, y, p = q.popleft()
        if (x, y) == (ex-1, ey-1):
            success = True
            break
        if p == 0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and not visit[ny][nx] and arr[ny][nx] - arr[y][x] <= p:
                visit[ny][nx] = True
                q.append((nx, ny, p-1))
    print("잘했어!!" if success else "인성 문제있어??")
