import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

# 북남동서 direction
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 시작, 끝 문의 좌표
open_x, open_y, close_x, close_y = -1, -1, -1, -1

for i in range(n):
    for j in range(n):
        if arr[i][j] == "#":
            if open_x == -1 and open_y == -1:
                open_x, open_y = i, j
            else:
                close_x, close_y = i, j

check = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
q = deque()

for d in range(4):
    q.append((open_x, open_y, d))
    check[open_x][open_y][d] = 0
    
while q:
    x, y, dir = q.popleft()
    
    if x == close_x and y == close_y:
        print(check[x][y][dir])
        break
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    # 범위에 만족하는 경우
    if 0 <= nx < n and 0 <= ny < n:
        
        # 벽이 아닌 경우
        if arr[nx][ny] != "*":
            if check[nx][ny][dir] == -1 or check[nx][ny][dir] > check[x][y][dir]:
                check[nx][ny][dir] = check[x][y][dir]
                q.appendleft((nx, ny, dir))
        
        # 거울을 놓을 수 있는 경우
        if arr[nx][ny] == "!":
            # 방향이 북 or 남이면 동 or 서로 반사
            if dir < 2:
                for n_dir in range(2, 4):
                    if check[nx][ny][n_dir] == -1 or check[nx][ny][n_dir] > check[x][y][dir] + 1:
                        check[nx][ny][n_dir] = check[x][y][dir] + 1
                        q.append((nx, ny, n_dir))
            # 방향이 동 or 서면 북 or 남으로 반사
            else:
                for n_dir in range(2):
                    if check[nx][ny][n_dir] == -1 or check[nx][ny][n_dir] > check[x][y][dir] + 1:
                        check[nx][ny][n_dir] = check[x][y][dir] + 1
                        q.append((nx, ny, n_dir))