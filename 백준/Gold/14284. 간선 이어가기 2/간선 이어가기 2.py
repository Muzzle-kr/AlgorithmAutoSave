import heapq as hq

def dijkstra(start, end):
    q = []
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    hq.heappush(q, (0, start))
    
    while q:
        dist, now = hq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for next_dist, next in edges[now]:
            cost = dist + next_dist
            
            if cost < distance[next]:
                distance[next] = cost
                hq.heappush(q, (cost, next))
                
    return distance[end]

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
    
s, e = map(int, input().split())

print(dijkstra(s, e))