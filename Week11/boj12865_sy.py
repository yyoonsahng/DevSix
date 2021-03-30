import sys


def knapsack(K, wList, vList, N):  # K: 배낭의 무게한도, wList: 각 보석의 무게, vList: 각 보석의 가격, N: 보석의 수
    dp = [[0] * (K + 1) for _ in range(N+1)]
    for n in range(N+1):
        for k in range(K + 1):  # 각 칸을 돌면서
            if n == 0 or k == 0:  # 0번째 행/열은 0으로 세팅
                dp[n][k] = 0
            elif wList[n-1] <= k:  # 점화식을 그대로 프로그램으로
                dp[n][k] = max(vList[n-1]+dp[n-1][k-wList[n-1]],
                               dp[n-1][k])
            else:
                dp[n][k] = dp[n-1][k]
    return dp[N][K]


wList = []
vList = []
N, K = map(int, sys.stdin.readline().strip().split())
for i in range(N):
    w, v = map(int, sys.stdin.readline().strip().split())
    wList.append(w)
    vList.append(v)
print(knapsack(K, wList, vList, N))
