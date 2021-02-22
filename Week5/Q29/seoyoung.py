N, C = map(int, input().split())

houseLocs = []
for i in range(N):
    houseLocs.append(int(input()))

houseLocs.sort()

start = houseLocs[1] - houseLocs[0]
end = houseLocs[N-1] - houseLocs[0]
maximumGap = 0
while start <= end:
    gap = (start+end)//2
    currLoc = houseLocs[0]
    count = 1
    for i in range(1, N):
        if houseLocs[i] >= currLoc + gap:
            currLoc = houseLocs[i]
            count += 1
    if count >= C:
        maximumGap = gap
        start = gap + 1
    else:
        end = gap - 1

print(maximumGap)
