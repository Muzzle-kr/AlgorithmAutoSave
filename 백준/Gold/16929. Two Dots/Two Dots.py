import sys

def dfs(x, y, start, cnt):
    global flag
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if 0 <= nx < N and 0 <= ny < M:
            
            if visited[nx][ny] and (nx, ny) == start and cnt >= 4:
                return True
            
            if not visited[nx][ny] and graph[x][y] == graph[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny, start, cnt+1):
                    return True
                visited[nx][ny] = False
    return False

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]
flag = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        if dfs(i, j, (i, j), 1):
            print("Yes")
            exit()
        visited[i][j] = False
print("No")
