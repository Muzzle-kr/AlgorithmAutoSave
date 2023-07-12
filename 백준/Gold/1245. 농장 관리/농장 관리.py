import sys
input = sys.stdin.readline

def dfs(i, j):
    global trigger
    visited[i][j] = True
    
    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        
        if (0 <= nx < N) and (0 <= ny < M):
            if mountains[nx][ny] > mountains[i][j]:
                trigger = False # 기존 봉우리는 가장 크지 않음
                
            if not visited[nx][ny] and mountains[nx][ny] == mountains[i][j]:
                dfs(nx, ny)

N, M = map(int, sys.stdin.readline().split())
mountains = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

cnt = 0

# logic
for i in range(N):
    for j in range(M):
        if mountains[i][j] > 0 and not visited[i][j]:
            trigger = True # init
            dfs(i, j)
            if trigger:
                cnt += 1

print(cnt)