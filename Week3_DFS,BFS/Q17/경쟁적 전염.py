from collections import deque
n, k = map(int, input().split())
arr = [[] for _ in range(n)]
viruses = [[] for _ in range(k)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
for i in range(n):
    arr[i] = list(map(int,input().split()))
s, y, x = map(int, input().split())
answer = k+2
dq = deque()
dq.append((x-1, y-1, 0))
if arr[y-1][x-1] > 0:
    answer = arr[y-1][x-1]
else:
    arr[y-1][x-1] = -1
    while dq:
        cx, cy, cnt = dq.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<=nx<n and 0<=ny<n and cnt < s:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = -1
                    dq.append((nx, ny, cnt+1))
                elif arr[ny][nx] > 0:
                    answer = min(answer, arr[ny][nx])
                    s = cnt + 1
if answer == k+2:
    answer = 0
print(answer)