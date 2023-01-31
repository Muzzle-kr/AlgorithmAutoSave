import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) 


def dfs(x, y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:    
            if corridor[nx][ny] == 1:
                corridor[nx][ny] = 0
                
                cnt += dfs(nx, ny)
    return cnt
                
n, m, numberOfTrash = map(int, input().split())
corridor = [[0 for _ in range(m)] for _ in range(n)]
answer = 0

for j in range(numberOfTrash):
    x, y = map(int, input().split())
    corridor[x-1][y-1] = 1

# for i in corridor:
#     print(i)
    
for x in range(n):
    count = 0
    for y in range(m):
        if corridor[x][y] == 1:
            corridor[x][y] = 0
            answer = max(answer, dfs(x, y))

print(answer)