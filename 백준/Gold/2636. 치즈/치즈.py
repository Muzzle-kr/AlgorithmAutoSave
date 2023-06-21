import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
inside_arr_list = []
cheese_list = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i ,j))
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            bfs(i, j)
            break

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cheese_list.append((i, j))
            
        if not graph[i][j] and not visited[i][j]:
            # 내부 공기 처리
            graph[i][j] = 2
            inside_arr_list.append((i, j))
            
time = 0
last_cheese_cnt = 0

def change_air_bfs(x, y):
    q = deque()
    q.append((x, y))
    change_air_list.append((x, y))
    visited_inside_arr[x][y] = 1
    
    while q:
        xx, yy = q.popleft()
        
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 2 and not visited_inside_arr[nx][ny]:
                    q.append((nx, ny))
                    change_air_list.append((nx, ny))
                    visited_inside_arr[nx][ny] = 1
while cheese_list:
    # print(f'######치즈 현황######')
    # for g in graph:
    #     print(g)
    
    last_cheese_cnt = len(cheese_list) # 마지막 치즈의 갯수
    melting_list = [] # 녹을 치즈를 저장할 배열
    change_air_list = []
    
    # 녹을 치즈들을 찾기
    for x, y in cheese_list:
        # print(f'x: {x}, y: {y}')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 외부 공기와 맞닿아있다면 녹을 치즈 배열에 추가
                if not graph[nx][ny]:
                    melting_list.append((x, y))
                    break
    
    # 녹을 치즈들을 치즈 배열에서 제외시키기
    cheese_list = list(set(cheese_list) - set(melting_list))
    
    # 녹을 치즈들을 외부 공기로 바꾸기
    for x, y in melting_list:
        graph[x][y] = 0
    
    # 변경될 공기 찾기
    for x, y in inside_arr_list:
        visited_inside_arr = [[0] * m for _ in range(n)]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 외부 공기와 맞닿은 내부 공기를 찾으면 bfs로 변경될 공기들을 찾는다.
                if not graph[nx][ny]:
                    change_air_bfs(x, y)
                    break
                    
    
    # 변경될 내부 공기들을 공기 배열에서 제외시키기
    if change_air_list:
        inside_arr_list = list(set(inside_arr_list) - set(change_air_list))
        
        # 변경될 내부 공기들을 외부 공기로 바꾸기
        for x, y in change_air_list:
            graph[x][y] = 0
            
    time += 1 # 1시간 증가

print(time)
print(last_cheese_cnt)
                    
    
        
            
            

        