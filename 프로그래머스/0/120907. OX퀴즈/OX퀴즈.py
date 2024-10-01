def solution(quiz):
    return ["O" if eval(q.split(" = ")[0]) == int(q.split(" = ")[-1]) else "X" for q in quiz]
