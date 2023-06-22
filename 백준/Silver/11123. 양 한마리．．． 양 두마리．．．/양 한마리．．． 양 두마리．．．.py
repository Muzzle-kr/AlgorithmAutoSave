from collections import deque

for _ in range(int(input())):
    r, c = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(r)]
    visited = [[False] * c for _ in range(r)]
    count = 0
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def bfs(i, j):
        q = deque()
        q.append((i, j))
        
        while q:
            x, y = q.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == '#' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '#' and not visited[i][j]:
                count += 1
                bfs(i, j)
    print(count)
                
    