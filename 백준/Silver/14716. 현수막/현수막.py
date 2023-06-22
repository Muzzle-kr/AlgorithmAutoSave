from collections import deque


r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
count = 0

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    
    while q:
        x, y = q.popleft()
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    
for i in range(r):
    for j in range(c):
        if graph[i][j] and not visited[i][j]:
            count += 1
            bfs(i, j)

print(count)