
 

def solution(a):
    result = [False for _ in range(len(a))]
    min_left, min_right = float("inf"), float("inf")
    
    for i in range(len(a)):
        if a[i] < min_left:
            min_left = a[i]
            result[i] = True
        if a[-1-i] < min_right:
            min_right = a[-1-i]
            result[-1-i] = True
    return sum(result)