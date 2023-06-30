from collections import deque

n = int(input())
graph = [[0] * n for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())
dir = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))

def bfs():
    q = deque()
    q.append((x1, y1, 0))
    visited = [[False] * n for _ in range(n)]
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == x2 and y == y2:
            return cnt
        
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
    return -1

print(bfs())