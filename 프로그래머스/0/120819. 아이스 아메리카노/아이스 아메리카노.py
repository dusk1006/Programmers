def solution(money):
    a = 0
    while money >= 5500:
        a += 1
        money -= 5500

    b = money
    answer = [a, b]
    return answer
