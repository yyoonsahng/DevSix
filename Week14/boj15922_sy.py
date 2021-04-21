N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

(px, py) = lines[0]
totalLength = py-px
for i, line in enumerate(lines):
    if i == 0:
        continue
    (x, y) = line
    if x >= py:
        totalLength += (y-x)
    elif x < py:
        totalLength += (y-py) if py < y else 0
    (px, py) = (x, max(y, py))

print(totalLength)
