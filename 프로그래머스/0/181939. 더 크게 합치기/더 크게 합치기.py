def solution(a, b):
    answer = 0
    
    a1 = int(str(a) + str(b))
    a2 = int(str(b) + str(a))
    
    if a1 > a2:
        answer = a1
    elif a1 < a2:
        answer = a2
    else:
        answer = a1
    
    return int(answer)