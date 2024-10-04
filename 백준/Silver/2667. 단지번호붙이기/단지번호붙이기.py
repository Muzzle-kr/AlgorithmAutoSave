from collections import deque

N = int(input())
estate = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = []

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    count = 0
    
    while q:
        x, y = q.popleft()
        count += 1
        
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            
            if 0 <= nx < N and 0 <= ny < N and estate[nx][ny] == "1" and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return count
        
        
for i in range(N):
    for j in range(N):
        if estate[i][j] == "1" and not visited[i][j]:
            answer.append(bfs(i, j))

answer.sort()

print(len(answer))

for a in answer:
    print(a)