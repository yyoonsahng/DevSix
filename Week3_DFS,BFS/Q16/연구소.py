from collections import deque
from copy import deepcopy
from itertools import combinations
n, m = map(int,input().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
arr = [[0 for _ in range(m)] for _ in range(n)]
viruses, spaces = [], []
cnt_of_virus = n * m

def bfs():
    arr_temp = deepcopy(arr)
    cnt = 0
    dq = deque()
    for virus in viruses:
        dq.append(virus)
        while dq:
            x, y = dq.popleft()
            cnt += 1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= ny < n and 0 <= nx < m and arr_temp[ny][nx] == 0:
                    arr_temp[ny][nx] = 2
                    dq.append((nx, ny))
    return cnt

for i in range(n):
    arr[i] = list(map(int,input().split()))
    for j in range(m):
        if arr[i][j] == 0:
            spaces.append((j, i))
        if arr[i][j] == 2:
            viruses.append((j, i))

for f, s, t in combinations(spaces,3):
    arr[f[1]][f[0]], arr[s[1]][s[0]], arr[t[1]][t[0]] = 1, 1, 1
    cnt_of_virus = min(cnt_of_virus, bfs())
    arr[f[1]][f[0]], arr[s[1]][s[0]], arr[t[1]][t[0]] = 0, 0, 0

cnt_of_walls = n*m - len(viruses) - len(spaces) + 3
print(n*m - cnt_of_virus - cnt_of_walls)
