import re
from itertools import product


def getMatchedList(regex, user_id):
    p = re.compile(regex)
    matchedList = []
    for uid in user_id:
        if p.match(uid):
            matchedList.append(uid)
    return matchedList


def getCaseCount(matchedList):
    possibleCaseCount = 0
    li = map(lambda x: frozenset(x), filter(
        lambda c: len(c) == len(set(c)), product(*matchedList)))
    return len(set(li))


def solution(user_id, banned_id):
    matchedList = [[] for _ in range(len(banned_id))]
    for i, bid in enumerate(banned_id):
        regex = bid.replace("*", "[a-z\d]")
        regex = "^"+regex+"$"
        matchedList[i] = getMatchedList(regex, user_id)
    answer = getCaseCount(matchedList)
    return answer
