N, M = map(int, input().split())

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

ddx = [-1, -1, 1, 1]
ddy = [-1, 1, 1, -1]

graph = [list(map(int, input().split())) for _ in range(N)]

# 비바라기 시전
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]



for _ in range(M):
    clouds_graph = [[0] * N for _ in range(N)]
    for i, j in clouds:
        clouds_graph[i][j] = 1
    
    # 방향, 속도
    d, s = map(int, input().split())
    water_copy = []
    disappeared_clouds = []
    
    # 구름에서 비내리기!
    while clouds:
        i, j = clouds.pop()

        
        nx = (i + dx[d-1] * s) % N
        ny = (j + dy[d-1] * s) % N
        
        graph[nx][ny] += 1
        water_copy.append((nx, ny))
        disappeared_clouds.append((nx, ny))
    
    # 물 복사 마법!
    while water_copy:
        i, j = water_copy.pop()
        cnt = 0
        
        for k in range(4):
            nx = i + ddx[k]
            ny = j + ddy[k]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > 0:
                cnt += 1
        
        graph[i][j] += cnt
            
    # 구름 생성!
    for i in range(N):
        for j in range(N):
            
            # 2 이상일 경우 구름 생성
            if graph[i][j] >= 2 and (i, j) not in disappeared_clouds:
                clouds.append((i, j))
                graph[i][j] -= 2    
                
waters = 0
for i in range(N):
    for j in range(N):
        waters += graph[i][j]

print(waters)