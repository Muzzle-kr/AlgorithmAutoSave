import math
def solution(n):
    answer = 0
    arr = []
    middle = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if i * i == n:
            middle += 1
            continue
            
        if n % i == 0:
            answer += 1
            arr.append(i)
    answer = answer * 2 + middle
    return answer