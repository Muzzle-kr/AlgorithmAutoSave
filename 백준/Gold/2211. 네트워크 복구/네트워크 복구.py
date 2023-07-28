import heapq as hq
import sys

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    INF = sys.maxsize
    dist[start] = 0
    
    while q:
        cur_dist, cur_node = hq.heappop(q)
        
        for next_dist, next_node in edges[cur_node]:
            cost = cur_dist + next_dist
            
            if dist[next_node] > cost:
                dist[next_node] = cost
                parent[next_node] = cur_node
                hq.heappush(q, (cost, next_node))
    return dist

input = sys.stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
INF = sys.maxsize
dist = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split()) 
    edges[a].append((c, b))
    edges[b].append((c, a))
    
dist = [INF] * (N+1)
parent = [0] * (N+1)
dijkstra(1)

print(N-1)
for i in range(2, N+1):
    print(i, parent[i])