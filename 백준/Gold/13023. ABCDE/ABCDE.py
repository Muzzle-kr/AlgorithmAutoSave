def dfs(i, cnt):
    if cnt == 5:
        return True
    
        
    for x in graph[i]:
        if not visited[x]:
            visited[x] = 1
            if dfs(x, cnt + 1):
                return True
            visited[x] = 0
    return False
            

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    if dfs(i, 1):
        print(1)
        break
    visited[i] = 0
else:
    print(0)