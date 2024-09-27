from collections import Counter

def solution(s):
    char_count = Counter(s)
    answer = ''.join(sorted(char for char in s if char_count[char] == 1))
    return answer