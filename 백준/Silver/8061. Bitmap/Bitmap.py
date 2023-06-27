from collections import deque

def get_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
    
def bfs():
    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '0':
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    for g in graph:
        print(*g)

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
result = []
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
        
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            graph[i][j] = 0
            queue.append((i, j))

bfs()