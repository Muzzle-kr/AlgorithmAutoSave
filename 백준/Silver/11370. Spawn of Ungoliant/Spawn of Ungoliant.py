from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[False] * c for _ in range(r)]
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and graph[nx][ny] == "T":
                    graph[nx][ny] = "S"
                    visited[nx][ny] = True
                    q.append((nx, ny))
while True:
    c, r = map(int, input().split())
    
    if c == 0 and r == 0:
        break
    
    graph = [list(input().strip()) for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "S":
                bfs(i, j)
    
    for g in graph:
        for s in g:
            print(s, end="")
        print()