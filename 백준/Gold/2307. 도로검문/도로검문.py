import sys
import heapq as hq

def block_dijkstra(a, b):
    queue = []
    hq.heappush(queue, (0, 1))
    dist = [INF] * (N+1)
    dist[1] = 0
    
    while queue:
        cur_dist, cur_node = hq.heappop(queue)
        
        if cur_dist > dist[cur_node]: continue
        
        for next_dist, next_node in edges[cur_node]:
            if (cur_node == a and next_node == b) or (cur_node == b and next_node == a):
                continue
            
            cost = cur_dist + next_dist
            if dist[next_node] > cost:
                dist[next_node] = cost
                hq.heappush(queue, (cost, next_node))
                
    return dist[N]
def dijkstra(start):
    queue = []
    hq.heappush(queue, (0, start))
    dist = [INF] * (N+1)
    dist[start] = 0
    
    while queue:
        cur_dist, cur_node = hq.heappop(queue)
        
        if cur_dist > dist[cur_node]: continue
        
        for next_dist, next_node in edges[cur_node]:
            cost = cur_dist + next_dist
            if dist[next_node] > cost:
                dist[next_node] = cost
                hq.heappush(queue, (cost, next_node))
    return dist[N]

input = sys.stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
INF = sys.maxsize
block_roads = []

for _ in range(M):
    a, b, t = map(int, input().split())
    edges[a].append((t, b))
    edges[b].append((t, a))
    block_roads.append((a, b))
# 도로를 막으려면 양방향을 다 막야아한다. (key point)
    
minimum_time = dijkstra(1)
result = 0

for a, b in block_roads:
    result = max(result, block_dijkstra(a, b) - minimum_time)

if result >= int(1e9):
    print(-1)
else:
    print(result)