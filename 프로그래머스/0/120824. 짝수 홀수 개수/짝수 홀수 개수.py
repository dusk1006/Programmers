def solution(num_list):
    a = []
    b = []
    for num in num_list:
        if num % 2 == 0:
            a.append(num)
        elif num % 2 == 1:
            b.append(num)
    answer = [len(a), len(b)]
    return answer