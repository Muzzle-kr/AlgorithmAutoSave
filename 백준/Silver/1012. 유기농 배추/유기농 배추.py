import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) 


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if farm[nx][ny] == 1:
                farm[nx][ny] = 0
                dfs(nx, ny)

for i in range(int(input())):
    n, m, numOfCabbage = map(int, input().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]
    check = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0
    
    for j in range(numOfCabbage):
        x, y = map(int, input().split())
        farm[x][y] = 1
    
    for x in range(n):
        for y in range(m):
            if farm[x][y] == 1:
                farm[x][y] = 0
                dfs(x, y)
                answer += 1
    
    print(answer)