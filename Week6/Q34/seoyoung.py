N = int(input())
power = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if power[j] > power[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))
