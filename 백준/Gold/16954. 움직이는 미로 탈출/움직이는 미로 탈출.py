import sys
from collections import deque
    
input = sys.stdin.readline
chess = [list(input().rstrip()) for _ in range(8)]

dx = [0, 0, -1, -1, -1, 1, 1, 1, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1, 0]

walls = set()

for i in range(8):
    for j in range(8):
        if chess[i][j] == '#':
            walls.add((i, j))
            

q = deque()
q.append((7, 0))

visited = set()

while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        
        if (x, y) in walls:
            continue

        if x == 0 and y == 7:
            print(1)
            exit()
        
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 8 and 0 <= ny < 8:
                if (nx, ny) not in visited and (nx, ny) not in walls:
                    visited.add((nx, ny))
                    q.append((nx, ny))

    # 벽이 있다면 방문 초기화
    if walls:
        visited = set()
    
    next_walls = set()
    
    for x, y in walls:
        if x + 1 < 8:
            next_walls.add((x+1, y))
    
    # 벽 위치 갱신
    walls = next_walls

print(0)