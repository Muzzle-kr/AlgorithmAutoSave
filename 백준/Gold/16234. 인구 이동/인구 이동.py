from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    united_arr = [(i, j)]
    total = graph[i][j]
    visited[i][j] = True
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    united_arr.append((nx, ny))
                    total += graph[nx][ny]
    
    if len(united_arr) > 1:
        return united_arr, total
    else:
        return [], 0
        
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

day = 0

while True:
    visited = [[False] * N for _ in range(N)]
    flag = False
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                united, total = bfs(i, j)
                
                if united:
                    new_citizen = total // len(united)
                    flag = True
                    
                    for ux, uy in united:
                        graph[ux][uy] = new_citizen
    
    if not flag:
        break
    
    day += 1

print(day)