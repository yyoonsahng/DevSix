min_val = 1000000000
max_val = -1000000000


# 남아있는 연산자 변수를 리스트로 넘겨주면 참조값을 넘겨주게 되므로
# value 값을 복사해서 넘겨주기 위해 int 변수로 쪼개서 넘겨줌
def dfs(value, cnt, add, minus, mul, div, type):
    # 전역변수로 사용
    global min_val
    global max_val
    operations = [add, minus, mul, div]
    operations[type] -= 1
    if type == 0:
        value += num[cnt]
    elif type == 1:
        value -= num[cnt]
    elif type == 2:
        value *= num[cnt]
    else: # oper == 3
        if value >= 0:
            value //= num[cnt]
        else:
            value = ((value * -1) // num[cnt]) * -1
    cnt += 1
    if cnt == N:
        max_val = max(max_val, value)
        min_val = min(min_val, value)

    for i in range(4):
        if operations[i] > 0:
            dfs(value, cnt, operations[0], operations[1], operations[2], operations[3], i)


N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

for i in range(4):
    if op[i] > 0:
        dfs(num[0], 1, op[0], op[1], op[2], op[3], i)

print(max_val)
print(min_val)
