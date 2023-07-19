import heapq as hq

def dijkstra(start):
    dist = [float('inf')] * n
    dist[start] = 0
    
    q = []
    hq.heappush(q, (0, start))
    
    while q:
        cur_time, cur_node = hq.heappop(q)
        
        if cur_time > dist[cur_node]:
            continue
    
        for next_time, next_node in graph[cur_node]:
            next_time += cur_time
            
            # 시야에 보이지 않거나 넥서스일 경우
            if next_node == n-1 or see[next_node] == 0:
                if next_time < dist[next_node]:
                    dist[next_node] = next_time
                    hq.heappush(q, (next_time, next_node))
    if dist[n-1] == float('inf'):
        return -1
    else:
        return dist[n-1]
                
n, m = map(int, input().split())
see = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))
    
print(dijkstra(0))
    