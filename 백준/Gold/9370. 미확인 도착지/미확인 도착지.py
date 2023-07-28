import heapq as hq
import sys

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    INF = sys.maxsize
    distance = [INF] * (n+1)
    distance[start] = 0
    
    while q:
        cur_dist, cur_node = hq.heappop(q)
        
        for next_dist, next_node in edges[cur_node]:
            cost = cur_dist + next_dist
            
            if distance[next_node] > cost:
                distance[next_node] = cost
                
                hq.heappush(q, (cost, next_node))
    return distance

input = sys.stdin.readline
T = int(input())    

for _ in range(T):
    # 교차로, 도로, 목적지 후보 개수
    n, m, t = map(int, input().split())
    # 출발지, g, h
    s, g, h = map(int, input().split())
    visited = [False] * (n+1)
    edges = [[] for _ in range(n+1)]
    
    for _ in range(m):
        # a, b, distance
        a, b, d = map(int, input().split())
        
        edges[a].append((d, b))
        edges[b].append((d, a))
    
    candidates = []
    
    for _ in range(t):
        candidates.append(int(input()))
    
    dist_start = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    result = []
    
    for candidate in candidates:
        if dist_start[g] + dist_g[h] + dist_h[candidate] == dist_start[candidate] or dist_start[h] + dist_g[candidate] + dist_h[g] == dist_start[candidate]:
            result.append(candidate)
    print(*sorted(result))