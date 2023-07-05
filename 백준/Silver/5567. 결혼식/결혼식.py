from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = 0
result_arr = []
def bfs():
    global result
    global result_arr
    
    q = deque()
    visited[1] = 1
    
    for s in graph[1]:
        visited[s] = 1
        q.append((s, 1))
    
    while q:
        x, cnt = q.popleft()
        
        if cnt <= 2:
            result += 1
            result_arr.append(x)
        else:
            continue
        
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = 1
                q.append((nx, cnt+1))

    return result    
for _ in range(int(input())):
    a, b = map(int, input().split())    
    graph[a].append(b)
    graph[b].append(a)
    
print(bfs())