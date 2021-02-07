def solution(N, stages):
    answer = []
    failureInfo = [[0, 0] for _ in range(N)]
    for stage in stages:
        if stage-1 <= N-1:
            failureInfo[stage-1][0] += 1
        for j in range(stage):
            if j <= N-1:
                failureInfo[j][1] += 1
    failureRate = [[i+1, 0] for i in range(N)]
    for i, info in enumerate(failureInfo):
        if info[1] > 0:
            failureRate[i][1] = info[0] / info[1]
    failureRate.sort(key=lambda x: x[1], reverse=True)

    answer = [i[0] for i in failureRate]
    return answer
