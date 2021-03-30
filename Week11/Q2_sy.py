from itertools import combinations


def getStrengthSum(team, board):
    combiList = list(combinations(team, 2))
    strengthSum = 0
    for combi in combiList:
        i, j = combi
        strengthSum += board[i][j]
    return strengthSum


N = int(input())
nodes = [i for i in range(N)]

board = []

for i in range(N):
    board.append(list(map(int, input().split())))

for combi in list(combinations(nodes, 2)):
    i, j = combi
    Sij = board[i][j]
    Sji = board[j][i]
    totalS = Sij + Sji
    board[i][j] = board[j][i] = totalS

combiList = list(combinations(nodes, N//2))
combiListLength = len(combiList)

minStrengthDiff = 9999
for i in range(len(combiList)//2):
    startTeam = combiList[i]
    linkTeam = combiList[combiListLength - i - 1]

    startTeamS = getStrengthSum(startTeam, board)
    linkTeamS = getStrengthSum(linkTeam, board)
    diff = abs(startTeamS-linkTeamS)
    if diff < minStrengthDiff:
        minStrengthDiff = diff

print(minStrengthDiff)
