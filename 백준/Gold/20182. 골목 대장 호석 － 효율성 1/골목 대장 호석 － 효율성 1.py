import heapq as hq

def dijkstra(start, end):
    INF = int(1e9)
    distance = [INF] * (N+1)
    q = []
    hq.heappush(q, (0, start, 0))
    distance[start] = 0
    max_min_dist = INF
    
    while q:
        dist, cur, max_dist = hq.heappop(q)
        
        if cur == end:
            max_min_dist = min(max_min_dist, max_dist)
            
        if distance[cur] < dist:
            continue
        
        for next_dist, next in edges[cur]:
            cost = dist + next_dist

            # 갖고 있는 돈보다 더 많이 쓰는 경우 pass
            if cost > C:
                continue
                
            if cost < distance[next]:
                distance[next] = cost
                hq.heappush(q, (cost, next, max(max_dist, next_dist)))
    return -1 if distance[end] == INF else max_min_dist
    
N, M, A, B, C = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

print(dijkstra(A, B))