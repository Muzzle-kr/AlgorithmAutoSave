import sys
from collections import deque
input = sys.stdin.readline

result = []

while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:
        break
    
    maps = []
    
    for i in range(H):
        maps.append(list(map(int, input().split())))
    
    
    
    countOfIsland = 0
    
    visit = [[0 for i in range(W)] for j in range(H)]
    
    for i in range(H):
        for j in range(W):
            
            if visit[i][j] == 0 and maps[i][j] == 1:
                # print(f'새로운 섬을 찾았습니다!! 시작점: {i, j}')
                
                q = deque()
                q.append((i, j))
                
                # 방문체크
                visit[i][j] = 1
                
                # 새로운 섬의 시작점 찾을 때마다 1을 추가
                countOfIsland += 1
                
                dx = [0, 0, -1, 1, -1, -1, 1, 1]
                dy = [-1, 1, 0, 0, -1, 1, 1, -1]
                
                while q:
                        x, y = q.popleft()
                        # print(f'pop한 좌표: {x, y}')
                        for k in range(8):
                            nx = x + dx[k]
                            ny = y + dy[k]

                            if 0 <= nx < H and 0 <= ny < W and visit[nx][ny] == 0:
                                if maps[nx][ny] == 1:
                                    visit[nx][ny] = 1
                                    # print(f'시작점: {i, j}에서 방문한 섬의 좌표: {nx, ny}')
                                    q.append((nx, ny))
    result.append(countOfIsland)
                        

for r in result:
    print(r)