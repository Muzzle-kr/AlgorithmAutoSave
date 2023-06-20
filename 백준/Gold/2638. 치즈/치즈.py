from collections import deque
import copy
import sys

input = sys.stdin.readline
n, m = map(int ,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited =[[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def melt_cheese():
    global nq
    q = copy.deepcopy(nq)
    nq = deque()
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m and ((not visited[nx][ny] and not graph[nx][ny]) or graph[nx][ny] == 1):
                visited[nx][ny] += 1
                
                if graph[nx][ny] == 1:
                    if visited[nx][ny] >= 2: # 녹을 치즈
                        nq.append((nx, ny))
                if not graph[nx][ny]:
                    q.append((nx, ny))
    for x, y in nq:
        graph[x][y] = 0
    
nq = deque([(0, 0)])
time = 0

while nq:
    melt_cheese()
    if nq:
        time += 1

print(time)