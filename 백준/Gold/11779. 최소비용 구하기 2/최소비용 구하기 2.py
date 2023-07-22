import heapq as hq

def dijkstra(start):
    q = []
    distance = [float('inf')] * (n+1)
    nearest = [float('inf')] * (n+1)
    distance[start] = 0
    hq.heappush(q, (0, start))
    
    while q:
        c, now = hq.heappop(q)
        
        if c > distance[now]:
            continue
        
        for next_node, next_cost in graph[now]:
            cost = c + next_cost
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                nearest[next_node] = now
                q.append((cost, next_node))
    return distance, nearest
    
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

dist, nearest = dijkstra(start)

ans = []
node = end

while node != start:
    ans.append(node)
    node = nearest[node]

ans.append(start)
ans.reverse()

print(dist[end])
print(len(ans))
print(*ans)