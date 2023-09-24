import sys
input = sys.stdin.readline

def factorial(n):
    result = 1
    
    for i in range(1, n + 1):
        result *= i
        
    return result

while True:
    N, K = map(int, input().rstrip().split())
    
    
    if N == 0 and K == 0:
        break
    
    K = min(K, N-K)
    idx = 0
    numerator = 1
    
    while idx < K:
        numerator *= (N - idx)
        idx += 1
    print(int(numerator / factorial(K)))