# 빈 칸에서 (상어가 아닌) 상어까지의 최단 거리 (BFS)를 구하는 문제
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
    
answer = []
                
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:        
            visit = [[0 for i in range(M)] for j in range(N)]
            visit[i][j] = 1
            
            q = deque()
            q.append((i, j, 0))
            
            dx = [0, 0, -1, 1, -1, -1, 1, 1]
            dy = [-1, 1, 0, 0, -1, 1, 1, -1]
            
            isFind = False
            
            while q:
                x, y, count = q.popleft()
                
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                        if maps[nx][ny] == 1:
                            # print(f'시작점 {i, j}, 도착점 {nx, ny}, 거리 {count+1}')
                            answer.append(count+1)
                            isFind = True
                            break
                        visit[nx][ny] = 1
                        q.append((nx, ny, count + 1))   
                if isFind:
                    break
            
print(max(answer))