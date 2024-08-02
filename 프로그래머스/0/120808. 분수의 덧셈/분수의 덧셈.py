import math

def solution(numer1, denom1, numer2, denom2):
    numerator = (numer1 * denom2) + (numer2 * denom1)
    denominator = denom1 * denom2
    gcd = math.gcd(numerator, denominator)
    return [numerator // gcd, denominator // gcd]
