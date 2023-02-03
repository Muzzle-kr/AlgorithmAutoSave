import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

result = [0, 0]

R, C = map(int, input().split())
maps = []
for i in range(R):
    maps.append(list(input()))
    
    
visit = [[False for i in range(C)] for j in range(R)]

def dfs(x, y):
    global wolfs
    global sheeps
    
    visit[x][y] = True
    
    if maps[x][y] == "v":
        wolfs += 1
    elif maps[x][y] == "k":
        sheeps += 1
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C:
            if visit[nx][ny] == False and maps[nx][ny] != '#':
                dfs(nx, ny)
    
for i in range(R):
    for j in range(C):
        if visit[i][j] == False and maps[i][j] != '#':
            wolfs = 0
            sheeps = 0
            
            dfs(i, j)
            
            if wolfs >= sheeps:
                result[1] += wolfs
            else:
                result[0] += sheeps

print(*result)