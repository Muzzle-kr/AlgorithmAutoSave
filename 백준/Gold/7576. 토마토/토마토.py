from collections import deque
import sys
input = sys.stdin.readline
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, m = map(int, input().split())
farm = []

for i in range(m):
    farm.append(list(map(int, input().split())))
                

visit = [[0] * n for _ in range(m)]
q = deque()
tomato = 0
empty = 0
day = 0

for i in range(m):
    for j in range(n):
        if farm[i][j] == 1:
            q.append((i, j, 0))
            visit[i][j] = 1
        
        if farm[i][j] == -1:
            empty += 1

while q:
    y, x, count = q.popleft()
    # print(y, x, count)
    visit[y][x] = 1
    tomato += 1
    day = max(day, count)
    
    for i in range(4):
        ny = y + direction[i][0]
        nx = x + direction[i][1]
        
        # print(f'ny: {ny}, x: {nx}')
        if 0 <= ny < m and 0 <= nx < n and visit[ny][nx] == 0 and farm[ny][nx] == 0:
            farm[ny][nx] = count + 1
            q.append((ny, nx, count + 1))
    
# print(visit, day, tomato, empty)
if tomato + empty < n * m:
    print(-1)
else:
    print(day)