N = int(input())
import heapq as hq

if N == 1:
    print(int(input()))
    exit()
    
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)

arr.sort()

maxNum = 0
length = len(arr)
for idx, n in enumerate(arr):
    if length - idx == 1:
        continue
    maxNum = max(maxNum, (n * (length - idx)))

print(maxNum)
