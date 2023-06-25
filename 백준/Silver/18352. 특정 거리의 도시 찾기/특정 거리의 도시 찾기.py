N, M, K, S = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist_arr = [0] * (N+1)
visited = [0] * (N+1)
for _ in range(M):
    s, e = map(int, input().split())    
    graph[s].append(e)

from collections import deque
result = []

def bfs(x):
    q = deque()
    q.append((x, 0))
    visited[x] = 1
    while q:
        s_p, dist = q.popleft()
        
        for e_p in graph[s_p]:
            if not dist_arr[e_p] and not visited[e_p]:
                dist_arr[e_p] = dist + 1
                visited[e_p] = 1
                q.append((e_p, dist+1))      
bfs(S)

isFind = False
for idx, da in enumerate(dist_arr):
    if idx == 0:
        continue
    if da == K:
        isFind = True
        print(idx)

if not isFind:
    print(-1)