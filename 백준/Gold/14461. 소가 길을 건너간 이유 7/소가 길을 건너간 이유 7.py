import heapq as hq
import sys

def dijkstra():
    q = []
    hq.heappush(q, (0, 0, 0, 0))
    
    INF = sys.maxsize
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0
    ans = INF
    
    while q:
        d, c, x, y = hq.heappop(q)
        
        if dist[x][y] < d: continue
        
        remain = (N-1-x) + (N-1-y)
        
        if remain <= 2:
            ans = min(ans, d + remain * T)
            
        for k in range(16):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N:
                cost = graph[nx][ny] + d + 3 * T
                
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    hq.heappush(q, (cost, c + 1, nx, ny))
    return ans
input = sys.stdin.readline
N, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1,  0,  0,  0,  1,  2,  3,  2,  1,  0, -1, -2, -3, -2, -1]
dy = [0,  0,  1, -1,  3,  2,  1,  0, -1, -2, -3, -2, -1,  0,  1,  2]

print(dijkstra())