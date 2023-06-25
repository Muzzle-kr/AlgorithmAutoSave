from collections import deque
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0] * m for _ in range(n)]

def bfs():
    q = deque()
    
    for i in range(m):
        # 전류가 통하는 선이라면
        if graph[0][i] == '0':
            visited[1][i] = 1
            q.append((1, i))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '0' and not visited[nx][ny]:
                    if nx == n -1:
                        return True
                    
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return False                
                
            
if bfs():
    print("YES")
else:
    print("NO")