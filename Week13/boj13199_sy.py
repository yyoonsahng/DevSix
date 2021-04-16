import sys
t = int(sys.stdin.readline())
for _ in range(t):
    price, budget, need, give = map(int, sys.stdin.readline().split())
    base = budget // price  # 처음에 가능한 치킨 주문량
    if base == 0:
        print(0)
        continue
    total = base * give  # 첫 치킨 주문 후 받는 쿠폰 양
    if total // need == 0:
        print(0)
        continue
    coupon_chicken = total // need  # 쿠폰으로 시킬 수 있는 치킨의 양
    total = total - coupon_chicken * need  # 총 쿠폰 - (쿠폰으로 시킬 수 있는 치킨의 양)*필요한 쿠폰
    total += coupon_chicken * give  # 쿠폰으로 치킨을 시켰을때 받는 쿠폰의 양을 더해준다
    if total >= need:
        total = total - need
        ans = total // (need - give) + 1
    else:
        ans = 0
    print(ans)
