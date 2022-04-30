import heapq as hq
N = int(input())

for _ in range(N):
    arr = []
    iter = int(input())
    for i in range(iter):
        uni, liter = input().split()
        liter = int(liter)
        hq.heappush(arr, (-liter, liter, uni))
    print(arr[0][2])
