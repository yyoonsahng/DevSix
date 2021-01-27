dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


# pypy로 돌려야 오류 안남
def dfs(graph, y, x, visited, union):
    visited[y][x] = True
    union.append((y, x))
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if L <= abs(graph[ny][nx] - graph[y][x]) <= R:
                if not visited[ny][nx]:
                    dfs(graph, ny, nx, visited, union)


N, L, R = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))


answer = 0
while True:
    visited = [[False] * N for _ in range(N)]
    unions = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                unions.append([])
                dfs(A, i, j, visited, unions[cnt])
                cnt += 1
    if len(unions) == N * N:
        break
    for i in range(len(unions)):
        sum = 0
        for j in range(len(unions[i])):
            y, x = unions[i][j]
            sum += A[y][x]
        for c in unions[i]:
            y, x = c
            A[y][x] = sum // len(unions[i])
    answer += 1

print(answer)

