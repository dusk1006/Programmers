def solution(array):
    array.sort()
    mid_index = len(array) // 2
    answer = array[mid_index]
    return answer