import heapq as hq
import sys

def dijkstra(sx, sy):
    queue = []
    hq.heappush(queue, (0, sx, sy, -1))
    mirror = [[INF] * W for _ in range(H)]
    mirror[sx][sy] = 0
    
    while queue:
        cnt, x, y, direction = hq.heappop(queue)
        
        if cnt > mirror[x][y] + 1:
            continue
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] != '*':
                # 방향이 같거나 처음 움직이는 경우 거울을 설치하지 않음.
                new_cnt = cnt
                
                # 방향이 다를 경우 거울 설치
                if direction != k and direction != -1:
                    new_cnt += 1
                
                if mirror[nx][ny] > new_cnt:
                    mirror[nx][ny] = new_cnt
                    hq.heappush(queue, (new_cnt, nx, ny, k))
    return mirror
                
# 거울의 최솟값. 꺾는 부분을 거울이라고 생각하면 됨.
input = sys.stdin.readline
INF = int(1e9)
W, H = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx, sy = 0, 0
ex, ey = 0, 0

for x in range(H):
    for y in range(W):
        if graph[x][y] == 'C':
            if sx == 0 and sy == 0:
                sx, sy = x, y
            else:
                ex, ey = x, y

result1 = dijkstra(sx, sy)[ex][ey]
result2 = dijkstra(ex, ey)[sx][sy]
print(min(result1, result2))