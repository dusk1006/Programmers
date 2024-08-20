def solution(my_string):
    a = []
    for b in my_string:
        if b.isdigit():
            a.append(int(b))
    answer = sum(a)
    return answer
