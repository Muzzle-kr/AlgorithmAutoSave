import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x, y, color, sort):
    
    chk[x][y] = 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # weak = RG일 때 RG면 같은 영역
        # normal 일때는 무조건 같은 영역
        if 0 <= nx < N and 0 <= ny < N and chk[nx][ny] == 0:
            if sort == "weak" and (color == "R" or color == "G"):
                if matrix[nx][ny] == "R" or matrix[nx][ny] == "G":
                    dfs(nx, ny, matrix[nx][ny], sort)
            else:
                if color == matrix[nx][ny]:
                    dfs(nx, ny, matrix[nx][ny], sort)
                

matrix = []
N = int(input())
for i in range(N):
    matrix.append(list(input()[:-1]))
    

chk = [[0] * N for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        
        if chk[i][j] == 0:
            answer += 1
            color = matrix[i][j]
            dfs(i, j, color, "normal")
print(answer)

chk = [[0] * N for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        
        if chk[i][j] == 0:
            answer += 1
            color = matrix[i][j]
            dfs(i, j, color, "weak")
print(answer)