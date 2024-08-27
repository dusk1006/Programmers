def solution(my_string):
    answer = []
    for char in my_string:
        if char.isdigit():
            answer.append(int(char))  # 숫자를 정수형으로 변환하여 리스트에 추가

    # 오름차순 정렬
    answer.sort()
    
    return answer