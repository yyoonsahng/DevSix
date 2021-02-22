N, target_x = map(int, input().split())

data = list(map(int, input().split()))


def countTarget(target_idx, target_x, data):
    if target_idx == -1:
        return -1

    count = 1
    right = target_idx + 1
    left = target_idx - 1
    while right != -1 or left != -1:
        if right >= len(data) or data[right] != target_x:
            right = -1
        if left < 0 or data[left] != target_x:
            left = -1

        if right != -1:
            count += 1
            right += 1
        if left != -1:
            count += 1
            left -= 1
    return count


start, end = 0, N-1
target_idx = -1
while start <= end:
    mid = (start + end)//2
    if data[mid] == target_x:
        target_idx = mid
        break
    elif data[mid] < target_x:
        start = mid + 1
    elif data[mid] > target_x:
        end = mid - 1

print(countTarget(target_idx, target_x, data))
