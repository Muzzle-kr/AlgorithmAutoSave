from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    new_virus_list = []
    
    while q:
        qx, qy = q.popleft()
        
        for k in range(4):
            nx = qx + dx[k]
            ny = qy + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[qx][qy]
                    new_virus_list.append((nx, ny))
                    virus[graph[nx][ny]].append((nx, ny))

    return new_virus_list
                
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus = [[] for _ in range(k+1)]

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus[graph[i][j]].append((i, j))

for _ in range(s):
    for i in range(1, k+1):
        q = deque()
        
        for vx, vy in virus[i]:
            q.append((vx, vy))
        
        # 새로운 바이러스를 리스트로 할당
        virus[i] = bfs()

print(graph[x-1][y-1])