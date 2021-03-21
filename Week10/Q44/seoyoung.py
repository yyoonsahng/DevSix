def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def getDistance(A, B):
    (xa, ya, za) = A
    (xb, yb, zb) = B
    return min(abs(xa - xb), abs(ya - yb), abs(za - zb))


N = int(input())

parent = [i for i in range(N)]

graph = []
for i in range(N):
    x, y, z = list(map(int, input().split()))
    graph.append((x, y, z))

edges = []
for i in range(N):
    for j in range(i):
        edges.append((getDistance(graph[i], graph[j]), i, j))

edges.sort()

minCost = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        minCost += cost

print(minCost)
