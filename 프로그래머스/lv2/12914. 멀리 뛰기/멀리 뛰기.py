def solution(n):
    if n < 3:
        return n
    
    a, b = 2, 3
    for i in range(2, n):
        a, b = b, a + b
    
    return a % 1234567