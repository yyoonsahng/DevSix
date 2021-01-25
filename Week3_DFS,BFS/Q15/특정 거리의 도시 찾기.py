from collections import deque

n, m, k, start_city = map(int,input().split())
arr = [[] for _ in range(n)]
dist = [-1 for _ in range(n)]
answer = []
for _ in range(m):
    a, b = map(int,input().split())
    arr[a-1].append(b)

dq = deque()
dq.append(start_city)
dist[start_city-1] = 0
while dq:
    cur_city = dq.popleft()
    for next_city in arr[cur_city-1]:
        if dist[next_city-1] >= 0:
            continue
        else:
            dq.append(next_city)
            dist[next_city-1] = dist[cur_city-1] + 1
for i, d in enumerate(dist):
    if d == k:
        answer.append(i+1)
if not answer:
    answer.append(-1)
for city in answer:
    print(city)
