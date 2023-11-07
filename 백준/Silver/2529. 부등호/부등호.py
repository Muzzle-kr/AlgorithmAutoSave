import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
signOfInequality = list(input().strip().split())
max_val = 0
min_val = int(1e11)


def dfs(n, array):
    if n == N:
        global max_val, min_val
        max_val = max(max_val, int(''.join([str(i) for i in array])))
        min_val = min(min_val, int(''.join([str(i) for i in array])))
        return
    
    sign = signOfInequality[n]
    lastValue = array[-1]
    
    if sign == "<":
        for currentValue in range(lastValue + 1, 10):
            if lastValue < currentValue and currentValue not in array:
                array.append(currentValue)
                dfs(n+1, array)
                array.pop()
    elif sign == ">":
        for currentValue in range(lastValue):
            if lastValue > currentValue and currentValue not in array:
                array.append(currentValue)
                dfs(n+1, array)
                array.pop()
    return
for i in range(10):
    dfs(0, [i])
    
print(str(max_val).zfill(N+1))
print(str(min_val).zfill(N+1))
            
        
