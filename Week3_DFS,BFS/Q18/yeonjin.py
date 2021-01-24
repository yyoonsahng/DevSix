def recur(w):
    if w == "":
        return ""
    sum = 0
    i = 0
    for i in range(len(w)):
        if w[i] == '(':
            sum += 1
        else:
            sum -= 1
        if sum == 0:
            break
    u = w[0: i + 1]
    v = w[i + 1:]
    sum = 0
    right = True
    for i in range(len(u)):
        if u[i] == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            right = False
            break
    # u가 올바른 문자열일 때
    if right:
        return u + recur(v)
    else:
        if len(u) == 2:
            u = ""
        else:
            u = u[1: len(u) - 1]
        u_reversed = ""
        for j in range(len(u)):
            if u[j] == '(':
                u_reversed += ')'
            else:
                u_reversed += '('
        return '(' + recur(v) + ')' + u_reversed


def solution(p):
    answer = recur(p)
    return answer


print(solution("()))((()"))
