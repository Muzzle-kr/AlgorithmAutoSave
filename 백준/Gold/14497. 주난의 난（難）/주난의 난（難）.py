import heapq as hq
from collections import deque
import sys


def bfs():
    queue = deque()
    queue.append((x1-1, y1-1))
    visited = [[-1] * M for _ in range(N)]
    visited[x1-1][y1-1] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if x == x2-1 and y == y2-1:
            return visited[x][y] + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == '1':
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                    else:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft((nx, ny))
        
input = sys.stdin.readline
N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 뚫린 길을 걸어가는 경우
# 막힌 길을 점프하는 경우

print(bfs())