def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


G = int(input())
P = int(input())

parent = [i for i in range(G+1)]

flag = True
answer = 0
for i in range(P):
    pGate = int(input())
    if flag:
        nextGate = find_parent(parent, pGate)
        if nextGate == 0:
            flag = False
        else:
            parent[nextGate] = parent[nextGate] - 1
            answer = i + 1

print(answer)
