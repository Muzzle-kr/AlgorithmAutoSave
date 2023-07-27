import heapq as hq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    dist = [float('inf') for _ in range(M)]
    dist[start] = 0
    hq.heappush(q, (0, start, [start]))
    final_route = []
    closeness = float('inf')
    while q:
        cur_dist, cur_node, route = hq.heappop(q)
        
        if cur_node == M-1:
            if closeness > cur_dist:
                closeness = cur_dist
                final_route = route
            
        if cur_dist > dist[cur_node]: continue
        
        for next_node, next_dist in edges[cur_node]:
            if dist[next_node] > cur_dist + next_dist:
                dist[next_node] = cur_dist + next_dist
                hq.heappush(q, (dist[next_node], next_node, route + [next_node]))
    return final_route

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    edges = [[] for _ in range(M)]

    for _ in range(N):
        x, y, z = map(int, input().split())
        edges[x].append((y, z))
        edges[y].append((x, z))
        
    d = dijkstra(0)

    print(f"Case #{t+1}: ", end='')
    if len(d) == 0:
        print(-1)
    else:
        print(*d)