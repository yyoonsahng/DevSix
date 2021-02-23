import copy

height = int(input())
triangle = []
for i in range(height):
    triangle.append(list(map(int, input().split())))

dp = copy.deepcopy(triangle)
for i in range(1, height):
    for j in range(i+1):
        left = 0 if j-1 < 0 else dp[i-1][j-1]
        right = 0 if j >= i else dp[i-1][j]
        dp[i][j] = dp[i][j] + max(left, right)

print(max(dp[i]))
