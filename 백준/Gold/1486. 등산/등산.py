import heapq as hq
import sys
import string

def find_index(alphabet):
    if alphabet in lower_case:
        return lower_case.index(alphabet) + 26
    
    if alphabet in upper_case:
        return upper_case.index(alphabet)
        
def dijkstra(sx, sy):
    q = []
    hq.heappush(q, (0, sx, sy))
    time = [[INF] * M for _ in range(N)]
    time[sx][sy] = 0
    
    while q:
        cur_time, cx, cy = hq.heappop(q)
        
        if cur_time > time[cx][cy]:
            continue
        
        cur_height = find_index(graph[cx][cy])
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            
            if 0 <= nx < N and 0 <= ny < M:
                next_height = find_index(graph[nx][ny])
                cost = cur_time
                
                if abs(cur_height - next_height) > T:
                    continue
                
                if cur_height >= next_height:
                    cost += 1
                else:
                    cost += (next_height - cur_height) ** 2
                
                if cost < time[nx][ny]:
                    time[nx][ny] = cost
                    hq.heappush(q, (cost, nx, ny))
    return time

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

input = sys.stdin.readline
N, M, T, D = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
INF = sys.maxsize

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

tq = []

for i in range(N):
    for j in range(M):
        hq.heappush(tq, (-find_index(graph[i][j]), i, j))

timeFromStart = dijkstra(0, 0)

while tq:
    height, x, y = hq.heappop(tq)
    timeFromMaxHeight = dijkstra(x, y)
    # 이동 거리가 D보다 크면 Skip
    if timeFromStart[x][y] + timeFromMaxHeight[0][0] > D: continue
    
    # 찾으면 print 후 종료
    print(find_index(graph[x][y]))
    break
    
