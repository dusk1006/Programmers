def solution(box, n):
    box0 = box[0]
    box1 = box[1]
    box2 = box[2]
    answer = (box0//n) * (box1//n) * (box2//n)
    return answer