from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))
    
    while q:
        x, cnt = q.popleft()
        
        if x == b:
            return cnt
        
        for nx in graph[x]:
            if not visited[nx]:
                q.append((nx, cnt+1))
                visited[nx] = 1
    return -1

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
    
for _ in range(m):
    x, y = map(int, input().split())
    
    graph[x].append(y)
    graph[y].append(x)

print(bfs(a))