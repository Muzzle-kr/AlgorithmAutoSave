import math
def solution(brown, yellow):
    divide = []
    sum = brown + yellow
    
    for i in range(math.ceil(math.sqrt(sum)), sum + 1):
        if sum % i == 0:
            divide.append(i)
    
    for i in divide:
        x = i
        y = sum // i
        
        if (x-2) * (y-2) != yellow:
            continue
        else: 
            return [x, y]