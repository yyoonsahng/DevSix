n = int(input())

houseLocations = list(map(int, input().split()))

houseLocations.sort()

print(houseLocations[n//2 - 1])
