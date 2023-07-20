from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

INF = int(1e9)

def bfs(graph, n):
    visited = [[INF] * n for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = graph[0][0]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if visited[x][y] + graph[nx][ny] < visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + graph[nx][ny]
    return visited[n-1][n-1]

idx = 0
while True:
    idx += 1
    n = int(input())
    
    if n == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    print(f'Problem {idx}: {bfs(graph, n)}')