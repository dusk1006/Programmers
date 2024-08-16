def solution(n):
    for i in range(int(n**0.5) + 1):
        if n == i * i:
            answer = 1
            break
    else:
        answer = 2
    return answer
