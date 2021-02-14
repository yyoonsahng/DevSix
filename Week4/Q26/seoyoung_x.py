n = int(input())

card_amount = []
for i in range(n):
    card_amount.append(int(input()))

card_amount.sort()

total = 0
prev_sum = 0
for amount in card_amount:
    now_sum = prev_sum + amount
    total += now_sum
    prev_sum = now_sum

total -= card_amount[0]

print(total)
