import heapq as hq

def dijkstra(start, end):
    q = []
    hq.heappush(q, (0, start))
    dist[start][start] = 0
    
    while q:
        cur_dist, cur_node = hq.heappop(q)
        
        if cur_dist > dist[start][cur_node]:
            continue
        
        for next_dist, next_node in edges[cur_node]:
            next_dist += cur_dist
            
            if next_dist < dist[start][next_node]:
                dist[start][next_node] = next_dist
                hq.heappush(q, (next_dist, next_node))
    
    return dist[start][end]
N, E = map(int, input().split())
INF = int(1e9)
dist = [[INF] * (N+1) for _ in range(N+1)]

# 0으로 초기화
for i in range(1, N+1):
    dist[i][i] = 0
    
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    
    edges[a].append((c, b))
    edges[b].append((c, a))

n, m = map(int, input().split())

ds1n = dijkstra(1, n)
ds1m = dijkstra(1, m)
dsnm = dijkstra(n, m)
dsmn = dijkstra(m, n)
dsnN = dijkstra(n, N)
dsmN = dijkstra(m, N)

path1 = ds1n + dsnm + dsmN
path2 = ds1m + dsmn + dsnN

result = min(path1, path2)
print(result if result < INF else -1)