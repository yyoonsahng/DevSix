from collections import deque
n, l, r = map(int, input().split())
arr = [[] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0
for i in range(n):
    arr[i] = list(map(int, input().split()))


def bfs(x, y, visited):
    dq = deque()
    dq.append((x, y))
    cur_union = [(x, y)]
    while dq:
        cx, cy = dq.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] \
                    and l <= abs(arr[cy][cx] - arr[ny][nx]) <= r:
                visited[ny][nx] = True
                dq.append((nx, ny))
                cur_union.append((nx, ny))
    return cur_union

def move():
    moved = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    unions = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                cur_union = bfs(j, i, visited)
                if len(cur_union) > 1:
                    unions.append(cur_union)
    if unions:
        moved = True
        for union in unions:
            avg_of_unions = sum([arr[country[1]][country[0]] for country in union]) // len(union)
            for country in union:
                arr[country[1]][country[0]] = avg_of_unions

    return moved

while move():
    answer += 1

print(answer)
