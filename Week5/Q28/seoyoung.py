N = int(input())
data = list(map(int, input().split()))


def findStaticPoint(start, end, data):
    if start > end:
        return -1
    mid = (start + end)//2
    if data[mid] == mid:
        return mid
    left = findStaticPoint(start, mid-1, data)
    right = findStaticPoint(mid+1, end, data)
    if left != -1:
        return left
    elif right != -1:
        return right
    else:
        return -1


print(findStaticPoint(0, N-1, data))
