from collections import deque

m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = [0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
    
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == graph[i][j]:
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return cnt ** 2

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                result[0] += bfs(i, j)
            else:
                result[1] += bfs(i, j)

print(*result)