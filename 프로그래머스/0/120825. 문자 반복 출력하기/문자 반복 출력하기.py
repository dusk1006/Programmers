def solution(my_string, n):
    result = ''
    for char in my_string:  # my_string의 각 문자에 대해 반복
        result += char * n  # 각 문자를 n번 반복하여 결과 문자열에 추가
    return result  # 최종 결과 문자열 반환
