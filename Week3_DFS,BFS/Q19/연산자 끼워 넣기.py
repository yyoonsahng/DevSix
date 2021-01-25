from itertools import permutations


def cal(op, pre_num, post_num):
    if op == 0:
        return pre_num + post_num
    elif op == 1:
        return pre_num - post_num
    elif op == 2:
        return pre_num * post_num
    else:
        if pre_num < 0:
            return (abs(pre_num) // post_num) * -1
        else:
            return pre_num // post_num


n = int(input())
arr = list(map(int, input().split()))
operator_counts = list(map(int, input().split()))
operators = []
for op, op_cnt in enumerate(operator_counts):
    operators.extend([op for _ in range(op_cnt)])
answer_min = 100000001
answer_max = -100000001
for op_list in permutations(operators):
    result = arr[0]
    for i, op in enumerate(op_list):
        result = cal(op, result, arr[i + 1])
    answer_max = max(answer_max, result)
    answer_min = min(answer_min, result)

print(answer_max)
print(answer_min)
