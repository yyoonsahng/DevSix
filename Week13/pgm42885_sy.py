def solution(people, limit):
    people.sort(reverse=True)
    startIdx = 0
    endIdx = len(people) - 1
    answer = 0
    while startIdx <= endIdx:
        answer += 1
        sum = people[startIdx] + people[endIdx]
        startIdx += 1
        if sum <= limit:
            endIdx -= 1

    return answer
