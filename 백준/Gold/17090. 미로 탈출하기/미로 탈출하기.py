import sys
sys.setrecursionlimit(10**9)

def escape_maze(x, y):
    
    if x < 0 or x >= r or y < 0 or y >= c:
        return 1
    
    
    if visited[x][y]:
        return visited[x][y]
    
    visited[x][y] = -1
    
    dx, dy = dir[graph[x][y]]
    nx, ny = x + dx, y + dy
    visited[x][y] = escape_maze(nx, ny)
    return visited[x][y]
    

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dir = {"U": [-1, 0], "R": [0, 1], "D": [1, 0], "L": [0, -1]}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0


for i in range(r):
    for j in range(c):
        if not visited[i][j] and escape_maze(i, j) == 1:
            answer += 1
        elif visited[i][j] == 1:
            answer += 1
            
print(answer)