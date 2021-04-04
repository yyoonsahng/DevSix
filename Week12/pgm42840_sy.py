students = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
]


def solution(answers):
    scores = [0] * len(students)
    count = 0
    for a in answers:
        for i, student in enumerate(students):
            if a == student[count % len(student)]:
                scores[i] += 1
        count += 1

    answer = []
    maxValue = 0
    for i, score in enumerate(scores):
        if score > maxValue:
            answer.clear()
            answer.append(i+1)
            maxValue = score
        elif score == maxValue:
            answer.append(i+1)
    return answer
