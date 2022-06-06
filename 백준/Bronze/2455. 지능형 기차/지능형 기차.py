import heapq as hq
import math

sum = []
for i in range(4):
    down, up = map(int, input().split())
    total = 0
    if i == 0:
        total = up - down
        sum.append(total)
    else:
        total = sum[i-1] - down + up
        sum.append(total)
        
print(max(sum))