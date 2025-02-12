from collections import deque
m, n = map(int, input().split())
maps = [list(input()) for _ in range(n)]

w_answer = 0
b_answer = 0

visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    count = 0
    
    a = maps[x][y]
    
    while len(queue):
        sx, sy = queue.popleft()
        
        count += 1
        
        for k in range(4):
            nx = dx[k] + sx
            ny = dy[k] + sy
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == a:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
            
    return count ** 2
        
    
    
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            score = bfs(i, j)
            
            if maps[i][j] == "W":
                w_answer += score
            else:
                b_answer += score

print(w_answer, b_answer)