from itertools import combinations
import copy
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(graph, v):
    y, x = v[0], v[1]
    graph[y][x] = 2
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        # 범위 밖으로 나가는지 체크
        if 0 <= ny < N and 0 <= nx < M:
            # 다음 칸이 빈공간이면 바이러스 이동
            if graph[ny][nx] == 0:
                dfs(graph, (ny, nx))


N, M = map(int, input().split())
graph = []
empty = []
virus = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 0:
            empty.append((i, j))
        elif line[j] == 2:
            virus.append((i, j))
    graph.append(line)

ans = 0
# 빈공간중에 벽이 들어올수 있는 세자리의 조합 리스트 구하기
walls_added_combi = list(combinations(empty, 3))
# 모든 조합에 대해 계산
for i in range(len(walls_added_combi)):
    walls_added = walls_added_combi[i]
    # 깊은 복사 해야 값이 복사됨
    # .copy()는 참조 복사라 new_graph 값 변경하면 graph 의 값도 같이 변경됨)
    new_graph = copy.deepcopy(graph)
    for c in walls_added:
        new_graph[c[0]][c[1]] = 1
    # 모든 바이러스의 위치에서 시작해서 dfs 수행
    for v in virus:
        dfs(new_graph, v)

    # 빈 공간 계산
    cnt = 0
    for line in new_graph:
        for j in line:
            if j == 0:
                cnt += 1
    ans = max(ans, cnt)

print(ans)
