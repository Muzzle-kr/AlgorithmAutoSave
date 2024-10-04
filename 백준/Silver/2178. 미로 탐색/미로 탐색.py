from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):

    q = deque()
    q.append((i, j, 1))
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    while q:
        x, y, count = q.popleft()
        
        if x == N-1 and y == M-1:
            print(count)
            break
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
        
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == "1":
                visited[nx][ny] = True
                q.append((nx, ny, count+1))
                
bfs(0, 0)