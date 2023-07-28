import heapq as hq

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    dist = [INF] * (N+1)
    dist[start] = 0
    
    while q:
        cur_dist, cur_node = hq.heappop(q)
        
        if cur_dist > dist[cur_node]:
            continue
        
        for next_node in edges[cur_node]:
            
            if dist[next_node] > cur_dist + 1:
                dist[next_node] = cur_dist + 1
                hq.heappush(q, (cur_dist+1, next_node))
    return max([0 if d == INF else d for d in dist[1:]])

N = int(input()) # 참석하는 사람의 수
M = int(input()) # 서로 알고있는 관계의 수

INF = int(1e9)
parent = [i for i in range(N+1)]
distance = [[]] * (N+1)
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in range(1, N+1):
    total = dijkstra(i)
    distance[i] = [total, i]

distance.sort()
visited = [False] * (N+1)
result = []

def handle_visit(node):
    for new_node in edges[node]:
        if not visited[new_node]:
            visited[new_node] = True
            handle_visit(new_node)
            
for total, node in distance[1:]:
    if not visited[node]:
        handle_visit(node)
        result.append(node)

print(len(result))
result.sort()
for r in result:
    print(r)