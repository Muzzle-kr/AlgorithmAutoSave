from collections import deque
import sys

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[INF, INF] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 0
    
    while q:
        x, y, is_sword = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][is_sword] == INF:
                    visited[nx][ny][is_sword] = visited[x][y][is_sword] + 1
                    q.append((nx, ny, is_sword))
                elif graph[nx][ny] == 1 and visited[nx][ny][is_sword] == INF:
                    if is_sword == 1:
                        visited[nx][ny][is_sword] = visited[x][y][is_sword] + 1
                        q.append((nx, ny, is_sword))
                elif graph[nx][ny] == 2 and visited[nx][ny][1] == INF:
                    visited[nx][ny][1] = visited[x][y][is_sword] + 1
                    q.append((nx, ny, 1))
    
    return min(visited[-1][-1][0], visited[-1][-1][1])
                        
input = sys.stdin.readline
N, M, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

INF = sys.maxsize
result = bfs()

if result > T or result == INF:
    print('Fail')
else:
    print(result)