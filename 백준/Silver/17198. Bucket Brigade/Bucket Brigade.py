from collections import deque
graph = [list(input().strip()) for _ in range(10)]
result_map = [[0] * 10 for _ in range(10)]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < 10 and 0 <= ny < 10:
                if graph[nx][ny] == "." and result_map[nx][ny] <= result_map[x][y]:
                    result_map[nx][ny] = result_map[x][y] + 1
                    q.append((nx, ny))
                
                elif graph[nx][ny] == "B":
                    return result_map[x][y]
    return 0
                
                
        
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(10):
    for j in range(10):
        if graph[i][j] == "L":
            print(bfs(i, j))
            exit()