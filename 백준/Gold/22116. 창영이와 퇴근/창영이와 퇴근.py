import heapq as hq

def dijkstra():
    q = []
    hq.heappush(q, (0, 0, 0))
    dist[0][0] = 0
    
    while q:
        slope_diff, x, y  = hq.heappop(q)
        
        if dist[x][y] < slope_diff:
            continue
        
        if x == n - 1 and y == n - 1: 
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                diff = max(slope_diff, abs(graph[x][y] - graph[nx][ny]))
                
                if dist[nx][ny] > diff:
                    dist[nx][ny] = diff
                    hq.heappush(q, (diff, nx, ny))
                
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dist = [[INF] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dijkstra()
print(dist[-1][-1])