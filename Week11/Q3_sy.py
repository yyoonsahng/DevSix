def getVisibleBuildingCount(i, building):
    buildingLength = len(building)
    total = 1
    diff = 0
    leftMinSlope = 99999999999
    rightMaxSlope = -99999999999
    leftBreak, rightBreak = False, False
    while True:
        diff += 1
        left = i - diff
        right = i + diff
        if left < 0:
            leftBreak = True
        if right >= buildingLength:
            rightBreak = True
        if leftBreak and rightBreak:
            break

        x, y = i, building[i]

        if not leftBreak:
            lx, ly = left, building[left]
            leftSlope = (y-ly)/(x-lx)
            if leftSlope < leftMinSlope:
                total += 1
                leftMinSlope = leftSlope
            else:
                leftBreak = True

        if not rightBreak:
            rx, ry = right, building[right]
            rightSlope = (y-ry)/(x-rx)
            if rightSlope > rightMaxSlope:
                total += 1
                rightMaxSlope = rightSlope
            else:
                rightBreak = True

    return total


N = int(input())
building = list(map(int, input().split()))

answer = 0
for i in range(N):
    count = getVisibleBuildingCount(i, building)
    if answer < count:
        answer = count

print(answer)
