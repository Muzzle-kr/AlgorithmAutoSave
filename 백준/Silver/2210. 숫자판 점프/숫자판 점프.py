from collections import deque
import sys

input = sys.stdin.readline

def dfs(x, y, word):
    global result
    
    if len(word) == 6:
        result.add(word)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, word + str(graph[nx][ny]))
            
    return
            
graph = [list(map(int, input().split())) for _ in range(5)]
result = set()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(5):
    for j in range(5):
        dfs(i, j, str(graph[i][j]))
print(len(result))