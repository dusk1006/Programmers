def solution(s1, s2):
    a = list(s1)
    b = list(s2)
    count = 0
    
    for char in a:
        if char in b:
            count += 1
            b.remove(char)
    return count