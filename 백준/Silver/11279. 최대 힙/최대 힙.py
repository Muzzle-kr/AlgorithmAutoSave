import sys
import heapq as hq
input = sys.stdin.readline

arr = []
hq.heapify(arr)

for i in range(int(input())):
    
    num = int(input())
    
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(hq.heappop(arr)[1])
    else:
        hq.heappush(arr, (-num, num))