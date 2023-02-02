import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))
    
arr.sort()

start = 0
end = arr[-1]

while start <= end:
    sum = 0 
    mid = math.ceil((start + end) / 2)
    
    for i in arr:
        sum += (i // mid)

    # print(f'start: {start}, end: {end}, mid: {mid}, sum: {sum}')
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1
    
print(start-1)