dx = [-1, 0, 1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    inputs = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(inputs[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            temp_list = []
            for t in range(3):
                nx = i + dx[t]
                ny = j - 1
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    temp_list.append(dp[nx][ny])
            dp[i][j] = dp[i][j] + max(temp_list)

    last_line = []
    for i in range(n):
        last_line.append(dp[i][m-1])
    print(max(last_line))
