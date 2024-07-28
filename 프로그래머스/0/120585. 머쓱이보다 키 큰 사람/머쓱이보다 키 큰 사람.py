def solution(array, height):
    array.append(height)
    array.sort()
    array.reverse()
    answer = array.index(height)
    return answer