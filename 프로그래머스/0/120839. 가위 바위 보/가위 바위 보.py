def solution(rsp):
    answer = []
    for a in rsp:
        if a == "0":  # 바위
            answer.append("5")  # 이기는 경우: 가위
        elif a == "5":  # 보
            answer.append("2")  # 이기는 경우: 바위
        elif a == "2":  # 가위
            answer.append("0")  # 이기는 경우: 보
    return ''.join(answer)  # 리스트를 문자열로 변환하여 반환
