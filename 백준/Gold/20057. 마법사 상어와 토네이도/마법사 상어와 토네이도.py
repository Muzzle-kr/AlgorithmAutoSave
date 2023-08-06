import sys

def distribute_sand(x, y, d):
    global graph
    global ratio
    global direction
    global outside_sand
    
    # 모래가 없다면
    if graph[x][y] == 0:
        return
    
    # 모래가 있다면
    # 모래의 양
    sand = graph[x][y]
    
    # 모래의 양 초기화
    graph[x][y] = 0
    remain_sand = sand
    # 모래의 양에 따라 분배
    for i in range(9):
        nx = x + direction[d][i][0]
        ny = y + direction[d][i][1]
        
        # 범위 안에 들어온다면
        if 0 <= nx < N and 0 <= ny < N:
            # 모래 분배
            graph[nx][ny] += int(sand * ratio[i])
        # 범위 밖이라면
        else:
            # 모래 분배
            outside_sand += int(sand * ratio[i])
        
        # 남는 모래 계산
        remain_sand -= int(sand * ratio[i])
            
    # 남은 모래
    nx = x + dx[d]
    ny = y + dy[d]
    
    # 범위 안에 들어온다면
    if 0 <= nx < N and 0 <= ny < N:
        graph[nx][ny] += remain_sand
    
    # 범위 밖이라면
    else:
        outside_sand += remain_sand
        
input = sys.stdin.readline
ratio = [0.1, 0.07, 0.01, 0.1, 0.07, 0.01, 0.02, 0.02, 0.05]
# 좌하우상
direction = [
    [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [-2, 0], [2, 0], [0, -2]], # 좌
    [[1, -1], [0, -1], [-1, -1], [1, 1], [0, 1], [-1, 1], [0, -2], [0, 2], [2, 0]], # 하
    [[-1, 1], [-1, 0], [-1, -1], [1, 1], [1, 0], [1, -1], [-2, 0], [2, 0], [0, 2]], # 우
    [[-1, -1], [0, -1], [1, -1], [-1, 1], [0, 1], [1, 1], [0, -2], [0, 2], [-2, 0]] # 상
]


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

sx, sy = N//2, N//2

# 좌하우상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d = 0
idx = 1
cnt = 1
outside_sand = 0
while True:
    # 2번에 한 번씩 idx + 1
    for _ in range(2):
        for _ in range(idx):
            sx += dx[d]
            sy += dy[d]
            
            # 범위 안에 들어온다면    
            if 0 <= sx < N and 0 <= sy < N:
                # 모래 분배
                distribute_sand(sx, sy, d)
                
            # 기저조건
            if sx == 0 and sy == 0:
                print(outside_sand)
                exit()
        d = (d + 1) % 4
    idx += 1