def solution(my_string):
    total_sum = 0
    number = ''
    for char in my_string:
        if char.isdigit():
            number += char
        else:
            if number:
                total_sum += int(number)
                number = ''
    if number:
        total_sum += int(number)
    
    return total_sum