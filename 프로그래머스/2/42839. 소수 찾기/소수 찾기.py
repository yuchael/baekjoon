from itertools import permutations

def is_prime(num):
    num = int(num)
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    
    return True
    
def solution(numbers):
    answer = 0
    n = len(numbers)
    
    for i in range(1, n + 1):
        p = set(list(permutations(numbers, i)))
        for num in p:
            num = ''.join(num)
            if num == "0" or num == "1" or num[0] == "0":
                continue
            if is_prime(num):
                answer += 1

    return answer