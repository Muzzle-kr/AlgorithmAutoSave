import heapq as hq

def dijkstra(start, end, money):
    q = []
    hq.heappush(q, (0, start, money))
    cost[start] = 0
    
    while q:
        shame, now, remain_money = hq.heappop(q)
        
        if now == end:
            return shame
        
        if cost[now] > shame:
            cost[now] = shame
            
        for next_shame, next in edges[now]:
            # 남은 비용이 0 이상일 경우 골목길을 갈 수 있음
            if remain_money - next_shame >= 0:
                if cost[next] > next_shame:
                    cost[next] = max(shame, next_shame)
                    hq.heappush(q, (max(shame, next_shame), next, remain_money - next_shame))        
    return -1        
N, M, A, B, C = map(int, input().split())

INF = int(1e9)
cost = [INF for _ in range(N+1)]
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    
    edges[a].append((c, b))
    edges[b].append((c, a))
    
print(dijkstra(A, B, C))