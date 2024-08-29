def solution(numbers):
    numbers.sort()
    max_product_positive = numbers[-1] * numbers[-2]
    max_product_negative = numbers[0] * numbers[1]
    return max(max_product_positive, max_product_negative)

