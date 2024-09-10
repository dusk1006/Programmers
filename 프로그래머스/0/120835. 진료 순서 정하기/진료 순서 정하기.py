def solution(emergency):
    answer = []
    e_sort = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(e_sort.index(i)+1)
    return answer
