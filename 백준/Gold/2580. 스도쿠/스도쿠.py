import sys

def check_row(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def check_col(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def check_rect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(empty):
        for i in range(9):
            print(*graph[i])
        exit()

    
    x, y = empty[idx]
    
    for i in range(1, 10):
        if check_row(x, i) and check_col(y, i) and check_rect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

input = sys.stdin.readline
graph = [list(map(int, input().split())) for _ in range(9)]
empty = []

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            empty.append((i, j))
            
dfs(0)