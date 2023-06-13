from collections import deque

# 입력값
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
num = 1
result = int(1e9)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 1번째 bfs (섬 구분)
def bfs(i,j):
    q = deque()
    q.append([i,j])
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = 1
                graph[nx][ny] = num
                q.append([nx,ny])

        
# 2번째 bfs (최단거리 구하기)
def bfs2(v):
    queue = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == v:
                dist[i][j] = 0
                queue.append([i,j])

    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
        
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] and graph[nx][ny] != v:
                    return dist[x][y]

                elif (not graph[nx][ny]) and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]+1
                    queue.append([nx,ny])
    return int(1e9)   



# 섬 구분
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            visited[i][j] = 1
            graph[i][j] = num
            bfs(i,j)
            num += 1

# 최단거리 구하기
for v in range(1, num):
    result = min(result, bfs2(v))
    
print(result)