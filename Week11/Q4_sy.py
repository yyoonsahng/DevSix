from itertools import combinations

while True:
    lottos = list(map(int, input().split()))
    count = lottos[0]
    if count == 0:
        break
    S = lottos[1:]
    for combi in list(combinations(S, 6)):
        print(' '.join(map(str, list(combi))))
    print()
