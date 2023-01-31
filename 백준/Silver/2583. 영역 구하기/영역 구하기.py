import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) 


def dfs(x, y):
    nx = [0, 0, 1, -1]
    ny = [1, -1, 0, 0]
    cnt = 1
    
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]    
        
        if 0 <= dx < n and 0 <= dy < m:
            if maps[dx][dy] == 0:
                maps[dx][dy] = 1
                cnt += dfs(dx, dy)
    return cnt

n, m, c = map(int, input().split())
maps = [[0 for _ in range(m)] for _ in range(n)]
answer = []
count = 0

for i in range(c):
    vx, vy, tx, ty = map(int, input().split())
    
    for i in range(vx, tx):
        for j in range(vy, ty):
            maps[j][i] += 1

for i in range(n):
    for j in range(m):
        
        if maps[i][j] == 0:
            count += 1
            maps[i][j] = 1
            cnt = dfs(i, j)
            answer.append(cnt)
            
answer.sort()

print(count)
print(*answer)