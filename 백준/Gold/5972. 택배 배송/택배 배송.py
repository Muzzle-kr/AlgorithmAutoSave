import heapq as hq

def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    
    pq = []
    hq.heappush(pq, (0, start))
    
    while pq:
        cur_dist, cur_node = hq.heappop(pq)
        
        # 이미 방문한 노드면 pass
        if cur_dist > dist[cur_node]:
            continue
        
        for next_dist, next_node in graph[cur_node]:
            next_dist += cur_dist
            
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                hq.heappush(pq, (next_dist, next_node))
    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

result = dijkstra(1)
print(result[n])