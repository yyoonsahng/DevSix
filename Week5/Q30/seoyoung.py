def findLengthMatchedWord(query, words):
    queryLength = len(query)
    start = 0
    end = len(words) - 1
    while start <= end:
        mid = (start + end)//2
        wordLength = len(words[mid])
        if wordLength == queryLength:
            return mid
        elif queryLength < wordLength:
            end = mid - 1
        elif queryLength > wordLength:
            start = mid + 1
    return -1


def isMatched(word, query):
    if len(word) != len(query):
        return False
    for i in range(len(query)):
        if query[i] == '?':
            continue
        if word[i] != query[i]:
            return False
    return True


def countMatchedWord(index, query, words):
    count = 0
    if isMatched(words[index], query):
        count += 1
    left = index - 1
    right = index + 1
    while left != -1 or right != -1:
        if left < 0 or len(words[left]) != len(query):
            left = -1
        if right >= len(words) or len(words[right]) != len(query):
            right = -1
        if left != -1:
            if isMatched(words[left], query):
                count += 1
            left -= 1
        if right != -1:
            if isMatched(words[right], query):
                count += 1
            right += 1
    return count


def solution(words, queries):
    answer = []
    words.sort(key=len)
    reversed_words = [word[::-1] for word in words]
    lengthMatchedMap = {}
    for query in queries:
        queryLength = len(query)
        index = lengthMatchedMap.get(queryLength)
        if index == None:
            index = findLengthMatchedWord(query, words)
            lengthMatchedMap[queryLength] = index
        if index == -1:
            answer.append(0)
        else:
            if query[0] != '?':
                answer.append(countMatchedWord(
                    index, query[::-1], reversed_words))
            else:
                answer.append(countMatchedWord(index, query, words))
    return answer


answer = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                  ["fro??", "????o", "fr???", "fro???", "pro?"])
print(answer)
