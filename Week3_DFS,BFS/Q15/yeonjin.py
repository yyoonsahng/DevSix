from collections import deque


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([(start, 0)])
    ans = []
    while queue:
        v = queue.popleft()
        time = v[1] + 1
        for i in graph[v[0]]:
            if not visited[i]:
                visited[i] = True
                # cnt 초에 i 노드 도착
                queue.append((i, time))
                if time == K:
                    ans.append(i)
    return ans


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (N + 1)
ans = bfs(graph, X, visited)
ans.sort()
if len(ans) > 0:
    for i in ans:
        print(i)
else:
    print(-1)