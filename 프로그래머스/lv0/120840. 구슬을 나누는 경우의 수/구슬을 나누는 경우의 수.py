def factorial(n):
    result = 1    
    for i in range(1, n+1):
        result *= i
    return result
        
def solution(balls, share):
    r = factorial(balls)
    d = factorial((balls - share)) * factorial(share)
    return int(r/d)