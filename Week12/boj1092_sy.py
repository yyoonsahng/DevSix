def canContinue(canMove):
    for cm in canMove:
        if cm == True:
            return True
    return False


def getCanCarryBoxIndex(craneWeight, boxs):
    if craneWeight < boxs[len(boxs) - 1]:
        return -1
    for i, boxWeigth in enumerate(boxs):
        if craneWeight >= boxWeigth:
            return i


N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxs = list(map(int, input().split()))

canMove = [True] * N

cranes.sort(reverse=True)
boxs.sort(reverse=True)

mins = 0
while True:
    mins += 1
    for i in range(N):
        if len(boxs) == 0:
            break
        if canMove[i] == True:
            idx = getCanCarryBoxIndex(cranes[i], boxs)
            if idx == -1:
                canMove[i] = False
            else:
                del boxs[idx]
    if len(boxs) == 0:
        break
    if canContinue(canMove) == False:
        mins = -1
        break

print(mins)
