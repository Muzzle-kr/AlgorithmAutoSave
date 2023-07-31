from collections import deque
import sys

input = sys.stdin.readline
INF = sys.maxsize

T = int(input())


def bfs():
    q = deque()
    visited = [[False] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                q.append((i, j, 0))
                visited[i][j] = True
            elif graph[i][j] == '*':
                q.appendleft((i, j, 0))
                visited[i][j] = True
    
    while q:
        x, y, time = q.popleft()
            
        if (x == 0 or x == h-1 or y == 0 or y == w-1) and graph[x][y] == '@':
            return time + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w:
                
                # print(f'nx: {nx}, ny: {ny}, w: {w}, h: {h}')
                
                # 불 case
                if graph[x][y] == "*":    
                    if graph[nx][ny] != '#' and not visited[nx][ny]:
                        graph[nx][ny] = '*'
                        visited[nx][ny] = True
                        q.append((nx, ny, time + 1))
                        
                elif graph[x][y] == '@':
                    if graph[nx][ny] == '.' and not visited[nx][ny]:
                        graph[nx][ny] = '@'
                        visited[nx][ny] = True
                        q.append((nx, ny, time + 1))
    return -1
        
for _ in range(T):
    w, h = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    result = bfs()
    
    if result == -1:
        print("IMPOSSIBLE")
    else:
        print(result)