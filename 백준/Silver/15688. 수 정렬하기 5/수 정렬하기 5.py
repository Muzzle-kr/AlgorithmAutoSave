import heapq as hq

arr = []
for i in range(int(input())):
    num = int(input())
    hq.heappush(arr, num)
    
for _ in range(len(arr)):
    print(hq.heappop(arr))