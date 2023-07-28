import heapq as hq
import sys

def fox_dijkstra():
    INF = int(1e9)
    dist = [INF] * (N+1)
    dist[1] = 0
    q = []
    hq.heappush(q, (0, 1))

    while q:
        cur_dist, cur_node = hq.heappop(q)
        
        if cur_dist > dist[cur_node]:
            continue
        
        for next_dist, next_node in edges[cur_node]:
            next_dist += cur_dist
            
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                hq.heappush(q, (next_dist, next_node))
    return dist

def wolf_dijkstra():
    INF = int(1e9)
    dist = [[INF] * (N+1) for _ in range(2)]
    # 빠르게 dist[1], 느리게 dist[0]
    dist[0][1] = 0
    q = []
    hq.heappush(q, (0, 1, False))

    while q:
        cur_dist, cur_node, speed_mode = hq.heappop(q)
        
        if not speed_mode and cur_dist > dist[0][cur_node]: continue
        if speed_mode and cur_dist > dist[1][cur_node]: continue
        
        for next_dist, next_node in edges[cur_node]:
            cost = cur_dist
            
            # 느리게 이동했다면 빠르게 이동
            if not speed_mode:
                cost += next_dist // 2
                
                if cost < dist[1][next_node]:
                    dist[1][next_node] = cost
                    hq.heappush(q, (dist[1][next_node], next_node, True))
            
            # 빠르게 이동했다면 느리게 이동
            else:
                cost += next_dist * 2
                
                if cost < dist[0][next_node]:
                    dist[0][next_node] = cost
                    hq.heappush(q, (dist[0][next_node], next_node, False))
                        
    return [min(dist[0][i], dist[1][i]) for i in range(N+1)]
        
input = sys.stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c*2, b))
    edges[b].append((c*2, a))

fox_dist = fox_dijkstra()
wolf_dist = wolf_dijkstra()

ans = 0
for i in range(1, N+1):
    if fox_dist[i] < wolf_dist[i]:
        ans += 1
print(ans)