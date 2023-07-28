import heapq as hq
import sys

def dijkstra(sx, sy):
    q = []
    hq.heappush(q, (0, 0, sx, sy))
    INF = float("inf")
    visit = [[0] * M for _ in range(N)]
    visit[sx][sy] = 1
    
    while q:
        a, b, x, y = hq.heappop(q)
            
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                visit[nx][ny] = 1
                
                if graph[nx][ny] == ".":
                    hq.heappush(q, (a, b, nx, ny))
                elif graph[nx][ny] == "G":
                    hq.heappush(q, (a, b+1, nx, ny))
                elif graph[nx][ny] == "g":
                    hq.heappush(q, (a+1, b, nx, ny))
                else:
                    print(a, b)
                    break
                
        
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
sx, sy = 0, 0
garbage = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == "S":
            sx, sy = i, j
        elif graph[i][j] == "g":
            garbage.append((i, j))

for i, j in garbage:
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == ".":
            graph[nx][ny] = "G"

dijkstra(sx, sy)
            