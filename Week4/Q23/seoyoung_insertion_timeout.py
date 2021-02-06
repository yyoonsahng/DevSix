# insertion sorting: timeout

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
for i in range(1, n-1):
    for j in range(i, 0, -1):
        if info[j-1][1] > info[j][1]:
            break
        elif info[j-1][1] == info[j][1]:
            if info[j-1][2] < info[j][2]:
                break
            elif info[j-1][2] == info[j][2]:
                if info[j-1][3] > info[j][3]:
                    break
                elif info[j-1][3] == info[j][3]:
                    if info[j-1][0] < info[j][0]:
                        break
        info = swapPositions(info, j-1, j)


for i, data in enumerate(info):
    print(data[0])
