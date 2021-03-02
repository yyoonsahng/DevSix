# again
import copy

N = int(input())
T, P = [], []
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0]*(N+1)
max_value = 0
for i in range(N-1, -1, -1):
    time = T[i] + i
    if time > N:
        dp[i] = max_value
    else:
        dp[i] = max(P[i]+dp[time], max_value)
        max_value = dp[i]

print(max_value)
