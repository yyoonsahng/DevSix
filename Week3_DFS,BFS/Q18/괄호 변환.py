def solution(p:str):
    answer = get_correct_str(p)
    return answer

def get_correct_str(b:str):
    if b == "": return b
    u, v = "", ""
    balance = 0
    for i, ch in enumerate(b):
        balance += 1 if ch == '(' else -1
        if balance == 0:
            u, v = b[:i+1], b[i + 1:]
            break
    if u[0] == ')':
        return '(' + get_correct_str(v) + ')' + ''.join([')' if ch == '(' else '(' for ch in u[1:-1]])
    else:
        return u + get_correct_str(v)