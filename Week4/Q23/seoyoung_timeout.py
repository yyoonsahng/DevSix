# selection sorting: timeout

# input
n = int(input())

info, result = [], []
for i in range(n):
    name, kor, eng, math = input().split()
    info.append([name, int(kor), int(eng), int(math)])


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# sorting
for i in range(n):
    p_index = i  # priority index
    for j in range(i+1, n):
        if info[p_index][1] < info[j][1]:
            p_index = j
        elif info[p_index][1] == info[j][1]:
            if info[p_index][2] > info[j][2]:
                p_index = j
            elif info[p_index][2] == info[j][2]:
                if info[p_index][3] < info[j][3]:
                    p_index = j
                elif info[p_index][3] == info[j][3]:
                    if info[p_index][0] > info[j][0]:
                        p_index = j
    info = swapPositions(info, i, p_index)

for i, data in enumerate(info):
    print(data[0])
