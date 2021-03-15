def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())

cities = [0] * (N+1)
for i in range(1, N + 1):
    cities[i] = i

for i in range(1, N+1):
    isConnected = list(map(int, input().split()))
    for j in range(1, N+1):
        if j > i:
            break
        if isConnected[j-1] == 1:
            union_parent(cities, i, j)

plan = list(map(int, input().split()))
group = find_parent(cities, plan[0])
for i in range(1, M):
    print(group, find_parent(cities, plan[i]))
    if group != find_parent(cities, plan[i]):
        group = -1
        break

print("YES") if group != -1 else print("NO")
