import sys
import heapq as hq
def dijkstra(start):
    queue = []
    hq.heappush(queue, (0, start))
    
    dist = [INF] * (N+1)
    dist[start] = 0
    
    while queue:
        cur_dist, cur_node = hq.heappop(queue)
    
        if dist[cur_node] < cur_dist: continue
            
        for next_dist, next_node in edges[cur_node]:
            # 오르막길 경우만 길을 가기
            if height[cur_node-1] < height[next_node-1]:
                next_dist += cur_dist
                
                if dist[next_node] > next_dist:
                    dist[next_node] = next_dist
                    hq.heappush(queue, (next_dist, next_node))
    return dist

input = sys.stdin.readline
INF = sys.maxsize
N, M, D, E = map(int, input().split())
height = list(map(int, input().split()))
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))


res1 = dijkstra(1)
res2 = dijkstra(N)
ans = []

for i in range(1, N+1):
    if res1[i] != INF and res2[i] != INF:
        ans.append(height[i-1] * E - (res1[i] + res2[i]) * D)

print(max(ans) if ans else "Impossible")