def solution(my_string):
    vowels = 'aeiou'
    answer = ''.join([char for char in my_string if char not in vowels])
    return answer
