from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and graph[nx][ny] == "*":
                    visited[nx][ny] = True
                    q.append((nx, ny))

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
count = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] == "*" and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)