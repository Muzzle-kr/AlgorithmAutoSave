import sys
sys.setrecursionlimit(10**9)

N = int(input()) 
maps = [list(map(int, input().split())) for _ in range(N)]

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
dp = [[-1] * N for _ in range(N)]
answer = 0

def validate_condition(nx, ny, sx, sy):
    return 0 <= nx < N and 0 <= ny < N and maps[nx][ny] > maps[sx][sy]

def dfs(sx, sy):
    if dp[sx][sy] != -1:
        return dp[sx][sy]
    
    dp[sx][sy] = 1
    
    for dx, dy in dir:
        nx = dx + sx
        ny = dy + sy
        
        if validate_condition(nx, ny, sx, sy):
            dp[sx][sy] = max(dp[sx][sy], dfs(nx, ny) + 1)
            
    return dp[sx][sy]

for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))

print(answer)