def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    for y in range(n):
        for x in range(m):
            if x == 0 and y == 0:
                continue
            if [x+1, y+1] in puddles:
                continue
            up = dp[y - 1][x] if y >= 0 else 0
            left = dp[y][x - 1] if x >= 0 else 0
            dp[y][x] = up + left

    answer = dp[n-1][m-1] % 1000000007
    return answer
