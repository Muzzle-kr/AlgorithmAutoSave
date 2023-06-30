from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs():
    q = deque()
    q.append((night_x-1, night_y-1, 0))
    visited = [[False] * (n) for _ in range(n)]
    visited[night_x-1][night_y-1] = True
    result = [0] * m
    
    while q:
        x, y, dist = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 상대편 말을 찾는다면
                if graph[nx][ny] == 2:
                    graph[nx][ny] = 0
                    result[opponent.index((nx+1, ny+1))] = dist+1
                    
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))

    return result
n, m = map(int, input().split())
graph = [[0] * (n) for _ in range(n)]
night_x, night_y = list(map(int, input().split()))
opponent = []

for _ in range(m):
    x, y = map(int, input().split())
    opponent.append((x, y))
    graph[x-1][y-1] = 2

r = bfs()
print(*r)