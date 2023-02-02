import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

start = 1
end = arr[-1]
result = 0

while start <= end:
    saw = math.ceil((start + end) / 2)
    total = 0
    
    for i in arr:
        if i > saw:
            total += (i - saw)
    
    if total < m:
        end = saw - 1
        
    else:
        start = saw + 1

print(end)