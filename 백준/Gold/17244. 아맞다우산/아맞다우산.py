from collections import deque
from itertools import permutations
import sys

def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * M for _ in range(N)]
    visited[sx][sy] = True
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == ex and y == ey:
            return cnt
            
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]: 
                if graph[nx][ny] != "#":
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
    return int(1e9)

input = sys.stdin.readline
M, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
stuff_cnt = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ex, ey = 0, 0
sx, sy = 0, 0

things = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == "X":
            stuff_cnt += 1
            things.append((i, j)) 
            
        elif graph[i][j] == "E":
            ex, ey = i, j
        
        elif graph[i][j] == "S":
            sx, sy = i, j
            
things_permu = list(permutations(things, stuff_cnt))
length = len(things_permu)
l_length = len(things_permu[0])
answer = int(1e9)

if stuff_cnt == 0:
    answer = bfs(sx, sy, ex, ey)
else:
    for i in range(length):
        distance = 0
        # S에서 첫번째 물건까지
        distance += bfs(sx, sy, things_permu[i][0][0], things_permu[i][0][1])        
        
        # 첫번째 물건에서 마지막 물건까지
        for j in range(1, l_length):
            distance += bfs(things_permu[i][j-1][0], things_permu[i][j-1][1], things_permu[i][j][0], things_permu[i][j][1])
        
        # 마지막 물건에서 E까지
        distance += bfs(things_permu[i][l_length-1][0], things_permu[i][l_length-1][1], ex, ey)
        answer = min(answer, distance)

print(answer)
    
