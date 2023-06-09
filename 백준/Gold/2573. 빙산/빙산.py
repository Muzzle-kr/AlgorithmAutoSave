from collections import deque
n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]
ices_list = []
largest_size = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if iceberg[i][j] != 0:
            ices_list.append((i, j))
            
def bfs(i, j):
    dq = deque([(i, j)])
    visited[i][j] = 1
    sea_list = []
    
    while dq:
        bx, by = dq.popleft()
        sea = 0
        
        for i in range(4):
            nx = dx[i] + bx
            ny = dy[i] + by
            
            if 0 <= nx < n and 0 <= ny < m:
                if not iceberg[nx][ny]:
                    sea += 1
                
                elif iceberg[nx][ny] != 0 and not visited[nx][ny]:
                    dq.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            sea_list.append((bx, by, sea))

    for x, y, sea_cnt in sea_list:
        iceberg[x][y] = max(0, iceberg[x][y] - sea_cnt)
    return 1        

year = 0
check = False

while ices_list:
    visited = [[0] * m for _ in range(n)]
    del_list = []
    count = 0
    
    for i, j in ices_list:
        if not visited[i][j]:
            count += bfs(i, j)
    
        if iceberg[i][j] == 0:
            del_list.append((i, j))

    # 빙산이 2개 이상으로 쪼개진 경우
    if count > 1:
        check = True
        break
    
    # 빙산이 다 녹은 경우
    if count == 0:
        break

    # 다 녹은 빙하 제거
    ices_list = list(set(ices_list) - set(del_list))
    year += 1
    
if check:
    print(year)
else:
    print(0)