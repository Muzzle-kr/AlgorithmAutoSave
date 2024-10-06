import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

def recur(y, x):    
    if y == N-1 and x == M - 1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    ways = 0

    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ny, nx = dy + y, dx + x
        
        if 0 <= ny < N and 0 <= nx < M and maps[y][x] > maps[ny][nx]:
            ways += recur(ny, nx)
            
    dp[y][x] = ways
    return dp[y][x]

print(recur(0, 0))