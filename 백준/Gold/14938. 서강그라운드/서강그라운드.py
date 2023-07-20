import heapq as hq

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
INF = int(1e9)
def dijkstra(start):
    dist = [INF] * (n+1)
    q = []
    hq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        cur_dist, cur_node = hq.heappop(q)
        
        if cur_dist > dist[cur_node]:
            continue
        
        for next_dist, next_node in edges[cur_node]:
            next_dist += cur_dist
            
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                hq.heappush(q, (next_dist, next_node))
    return sum([items[i-1] for i in range(1, n+1) if dist[i] <= m])
edges = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    edges[a].append((l, b))
    edges[b].append((l, a))

result = 0
for i in range(1, n+1):
    result = max(result, dijkstra(i))
print(result)