import heapq as hq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

nearest = [float('inf')] * (n+1)
distance = [float('inf')] * (n+1)

q = [(0, start)]

while q:
    dist, now = hq.heappop(q)
    
    if dist > distance[now]:
        continue
    
    for next, next_dist in graph[now]:
        cost = dist + next_dist
        
        if cost < distance[next]:
            distance[next] = cost
            nearest[next] = now
            hq.heappush(q, (cost, next))
ans = []
node = end

while node != start:
    ans.append(node)
    node = nearest[node]
    
ans.append(str(start))
ans.reverse()

print(distance[end])
print(len(ans))
print(*ans)