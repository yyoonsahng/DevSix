bracketList = input()

answer = 0
leftCount = 0
prevIsLeft = True
for i in range(len(bracketList)):
    if bracketList[i] == '(':
        leftCount += 1
        prevIsLeft = True
    else:
        leftCount -= 1
        answer += leftCount if prevIsLeft else 1
        prevIsLeft = False

print(answer)
