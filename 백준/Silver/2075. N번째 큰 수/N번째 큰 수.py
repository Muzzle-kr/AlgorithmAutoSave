import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
arr = []
ans = []
for i in range(n):
    tmp = list(map(int, input().rstrip().split()))
    arr.append(tmp)
    
for i in range(n):
    for j in range(n):
        hq.heappush(ans, arr[j][i])
        
        while len(ans) > n:
            hq.heappop(ans)
        
print(hq.heappop(ans))