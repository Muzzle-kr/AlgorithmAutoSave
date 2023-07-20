import heapq as hq
N = int(input())
B = int(input())

def dijkstra(start):
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
        
INF = int(1e9)
edges = [[] for _ in range(N+1)]
dist = [INF] * (N+1)
for _ in range(B):
    a, b, d = map(int, input().split())
    edges[a].append((d, b))

s_p, e_p = map(int, input().split())
dijkstra(s_p)
print(dist[e_p])