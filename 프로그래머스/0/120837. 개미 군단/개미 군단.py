def solution(hp):
    a = 5
    b = 3
    c = 1
    k = 0
    k += hp // a
    hp %= a
    k += hp // b
    hp %= b
    k += hp // c

    return k