def solution(i, j, k):
    answer = 0
    a = 0
    for a in range(i, j + 1):
        answer += str(a).count(str(k))
    return answer
