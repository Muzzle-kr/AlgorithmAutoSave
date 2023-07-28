import heapq as hq
import sys

INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start):
    q = []
    cnt = 0
    hq.heappush(q, (0, cnt, start))
    dist = [[INF] * (K+1) for _ in range(N+1)]
    dist[start][cnt] = 0

    while q:
        cur_dist, cnt, cur_node = hq.heappop(q)
        
        if cur_dist > dist[cur_node][cnt]: continue    
        
        for next_dist, next_node in edges[cur_node]:
            cost = next_dist + cur_dist
            
            if dist[next_node][cnt] > cost:
                dist[next_node][cnt] = cost
                hq.heappush(q, (cost, cnt, next_node))
                
            if cnt < K and dist[next_node][cnt+1] > cur_dist:
                    dist[next_node][cnt+1] = cur_dist
                    hq.heappush(q, (cur_dist, cnt + 1, next_node))
    return dist
N, M, K = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))    

print(min(dijkstra(1)[N]))