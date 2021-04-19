import re
from itertools import permutations


def canSplited(expression):
    return True if expression.find("*") != -1 or expression.find("+") != -1 or expression.find("-") != -1 else False


def getCalcTotal(expression, operators, i):
    if i == -1:
        return int(expression)
    eList = expression.split(operators[i])
    total = getCalcTotal(eList[0], operators, i -
                         1) if canSplited(eList[0]) else int(eList[0])
    for e in eList[1:]:
        nextNum = getCalcTotal(e, operators, i-1)
        if operators[i] == '+':
            total += nextNum
        elif operators[i] == '-':
            total -= nextNum
        elif operators[i] == '*':
            total *= nextNum
    return total


def solution(expression):
    answer = 0
    operators = ['*', '+', '-']
    for perm in permutations(operators, 3):
        answer = max(answer, abs(getCalcTotal(expression, list(perm), 2)))

    return answer
