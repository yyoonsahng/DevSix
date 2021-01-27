from itertools import combinations
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def go(y, x, dir, objects):
    if arr[y][x] == 'S':
        return True
    elif (y, x) in objects:
        return False
    ny, nx = y + dy[dir], x + dx[dir]
    if 0 <= ny < N and 0 <= nx < N:
        return go(ny, nx, dir, objects)
    return False


N = int(input())
arr = []
emptys = []
teachers = []
for i in range(N):
    arr.append(list(map(str, input().split())))
    for j in range(N):
        if arr[i][j] == 'X':
            emptys.append((i, j))
        elif arr[i][j] == 'T':
            teachers.append((i, j))

flg2 = False
for objects in list(combinations(emptys, 3)):
    flg = False
    for teacher in teachers:
        for i in range(4):
            ny, nx = teacher[0] + dy[i], teacher[1] + dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                if go(ny, nx, i, objects):
                    # 학생 발견
                    flg = True
                    break
    if not flg:
        flg2 = True
        print("YES")
        break
if not flg2:
    print("NO")