import heapq as hq

def dijkstra(start):
    visited = [0] * (N+1)
    d = [int(1e9)] * (N+1)
    d[start] = 0
    
    heap = []
    hq.heappush(heap, (0, start))
    
    while heap:
        dist, current = hq.heappop(heap)
        
        if d[current] < dist:
            continue
        
        # 방문 처리
        visited[current] = 1
        for next, distance in graph[current]:
            cost = dist + distance
            
            if distance != 0 and visited[next] == 0 and cost < d[next]:
                d[next] = d[current] + distance
                hq.heappush(heap, (cost, next))
    
    return d
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

FromXDist = dijkstra(X)
answer = 0

for i in range(1, N+1):
    FromTownDist = dijkstra(i)
    answer = max(answer, FromTownDist[X] + FromXDist[i])

print(answer)