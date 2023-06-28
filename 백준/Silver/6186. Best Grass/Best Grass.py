from collections import deque

r, c = map(int, input().split())
pasture = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
cnt = 0

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if pasture[nx][ny] == '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    
for i in range(r):
    for j in range(c):
        if pasture[i][j] == '#' and not visited[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt)