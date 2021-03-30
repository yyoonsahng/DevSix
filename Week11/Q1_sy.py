from itertools import combinations


def canBeCourse(combiCase, orders, orderAmounts):
    combiCaseLength = len(combiCase)
    count = 0
    for i, order in enumerate(orders):
        if count >= 2:
            break
        if orderAmounts[i] < combiCaseLength:
            continue
        flag = True
        for alph in combiCase:
            if order.find(alph) == -1:
                flag = False
        if flag:
            count += 1
    return True if count >= 2 else False


def arrayToString(answer):
    strAnswer = []
    for a in answer:
        strAnswer.append(''.join(a))
    return strAnswer


def solution(orders, course):
    answer = []

    allDishes = []
    orderAmounts = []
    for order in orders:
        orderAmounts.append(len(order))
        for o in order:
            try:
                findIndex = allDishes.index(o)
            except:
                allDishes.append(o)

    for c in course:
        combi = combinations(allDishes, c)
        for _c in list(combi):
            combiCase = sorted(list(_c))
            isCourse = canBeCourse(combiCase, orders, orderAmounts)
            if isCourse:
                answer.append(combiCase)
    temp = arrayToString(sorted(answer))
    print(temp)
    return answer
