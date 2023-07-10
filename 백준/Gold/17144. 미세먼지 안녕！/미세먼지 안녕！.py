from collections import deque
r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

air_top = 0
air_bottom = 0

for i in range(r):
    if graph[i][0] == -1:
        air_top = i
        air_bottom = i+1
        break
    
def work_top_air_cleaner():
    x = air_top
    
    # 맨 첫행부터 공기청정기로 흡수
    for i in range(x-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    
    # 첫열 공기청정기 흡수
    for j in range(c-1):
        graph[0][j] = graph[0][j+1]
        
    # 마지막행 공기청정기 흡수
    for i in range(x):
        graph[i][c-1] = graph[i+1][c-1]
    
    # x열 공기청정기 흡수
    for j in range(c-1, 1, -1):
        graph[x][j] = graph[x][j-1]
        
    graph[x][1] = 0

def work_bottom_air_cleaner():
    x = air_bottom
    
    # 맨 첫행부터 공기청정기로 흡수
    for i in range(x+1, r-1):
        graph[i][0] = graph[i+1][0]
    
    # 마지막열 공기청정기 흡수
    for j in range(c-1):
        graph[r-1][j] = graph[r-1][j+1]
        
    # 마지막행 공기청정기 흡수
    for i in range(r-1, x, -1):
        graph[i][c-1] = graph[i-1][c-1]
    
    # x열 공기청정기 흡수
    for j in range(c-1, 1, -1):
        graph[x][j] = graph[x][j-1]
    
    graph[x][1] = 0
        
second = 0  

def check_air_cleaner(x, y):
    return y == 0 and (x == air_top or x == air_bottom)

def work_air_cleaner(): 
    work_top_air_cleaner()
    work_bottom_air_cleaner()
    
def spread_micro_dust(i, j):
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
        
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 한 번에 더 해줘야함
        if 0 <= nx < r and 0 <= ny < c and not check_air_cleaner(nx, ny):
            shared_dust = graph[x][y] // 5
            new_graph[nx][ny] += shared_dust
            new_graph[x][y] -= shared_dust
        
while second < t:
    micro_dust = []
    
    for i in range(r):
        for j in range(c):
            # 공기청정기라면 생략
            if not check_air_cleaner(i, j) and graph[i][j] != 0:
                # 미세먼지 배열에 삽입
                micro_dust.append((i, j))            
    # 새로운 곳에 미세먼지 퍼뜨리기
    new_graph = [[0] * c for _ in range(r)]
    
    for x, y in micro_dust:
        spread_micro_dust(x, y)
    
    # 퍼뜨린 미세먼지 계산하기
    for i in range(r):
        for j in range(c):
            graph[i][j] += new_graph[i][j]
            
    # 공기 청정기 돌리기
    work_air_cleaner()
    
    second += 1
    # print(f'--------{second}초 후--------')
    # for g in graph:
    #     print(g)

total_micro_dust = 0

for i in range(r):
    for j in range(c):
        if not check_air_cleaner(i, j):
            total_micro_dust += graph[i][j]

print(total_micro_dust)
    