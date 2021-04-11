from itertools import combinations


def isMinimality(answerList, combi):
    for al in answerList:
        allIn = True
        for a in al:
            if a not in combi:
                allIn = False
                break
        if allIn:
            return False
    return True


def solution(relation):
    colLen = len(relation[0])

    answerList = []
    colIdxList = [i for i in range(colLen)]
    for i in range(1, colLen+1):
        combiList = list(combinations(colIdxList, i))
        for combi in combiList:
            if isMinimality(answerList, combi) == False:
                continue
            canCandiKey = True
            strList = []
            for i, row in enumerate(relation):
                joinedStr = ''.join([row[i] for i in list(combi)])
                if joinedStr in strList:
                    canCandiKey = False
                    break
                else:
                    strList.append(joinedStr)

            if canCandiKey == True:
                answerList.append(combi)

    answer = len(answerList)
    return answer
