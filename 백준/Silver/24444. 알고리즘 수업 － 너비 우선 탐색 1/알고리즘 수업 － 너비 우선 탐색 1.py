from collections import deque
import heapq as hq
import sys

input = sys.stdin.readline
    
def bfs():
    global order
    visited = [False] * (n+1)
    visited[s] = True
    
    q = deque()
    q.append(s)
    result[s] = order
    
    while q:
        now = q.popleft()
        
        not_used = []
        
        while arr[now]:
            i = hq.heappop(arr[now])
            if not visited[i]:
                visited[i] = True
                order += 1
                result[i] = order
                q.append(i)
            else:
                not_used.append(i)
        
        for i in not_used:
            hq.heappush(arr[now], i)


n, m, s = map(int, input().split())
arr = [[] for _ in range(n+1)]
order = 1
result = [0] * (n+1)
for _ in range(m):
    i, j = map(int, input().split())
    
    hq.heappush(arr[i], j)
    hq.heappush(arr[j], i)
    
bfs()

for i in range(1, n+1):
    print(result[i])