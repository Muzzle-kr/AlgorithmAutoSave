from collections import deque

N, M, K = map(int, input().split())
condo = [[0] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 콘도에 음식물 쓰레기 투척
for _ in range(K):
    x, y = map(int, input().split())
    condo[x-1][y-1] = 1
    
visited = [[False] * M for _ in range(N)] 

def bfs(i, j):
    visited[i][j] = True
    q = deque()
    q.append((i, j))
    count = 0
    
    while q:
        x, y = q.popleft()
        count += 1
        
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            
            if 0 <= nx < N and 0 <= ny < M and condo[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return count    

answer = 0

for i in range(N):
    for j in range(M):
        if condo[i][j] == 1 and not visited[i][j]:
            answer = max(answer, bfs(i, j))

print(answer)