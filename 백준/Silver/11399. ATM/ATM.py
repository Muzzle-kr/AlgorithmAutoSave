# 5
# 3 1 4 3 2
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

arr.sort()

total = 0
lastMin = 0

for i in arr:
    total = total + (lastMin + i)
    lastMin += i
    
print(total)    