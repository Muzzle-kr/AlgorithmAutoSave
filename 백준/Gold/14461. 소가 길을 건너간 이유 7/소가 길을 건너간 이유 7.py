
import heapq as hq
import sys

def dijkstra():
    q = []
    hq.heappush(q, (0, 0, 0, 0))
    
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0
    ans = INF
    
    while q:
        d, c, x, y = hq.heappop(q)
        
        if dist[x][y] < d: continue
        
        toN = (N - x - 1) + (N - y - 1)
        
        # 목적지까지 3칸 안에 갈 수 있다면
        if toN <= 2:
            ans = min(ans, d + toN * T)
            
        for i in range(16):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                cost = d + 3 * T + graph[nx][ny]
                
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                hq.heappush(q, (cost, c+1 , nx, ny))
                
    return ans
    
input = sys.stdin.readline
N, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1]
dy = [1, -1, 0, 0, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]

print(dijkstra())

