import heapq as hq
import sys

def find_friend(V):
    if V == P:
        return True
    
    for node in parent[V]:
        if find_friend(node):
            return True
    return False

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    distance = [INF] * (V+1)
    distance[start] = 0
    
    while q:
        dist, now = hq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for next_dist, next in graph[now]:
            total_dist = dist + next_dist
            
            if distance[next] > total_dist:
                distance[next] = total_dist
                hq.heappush(q, (total_dist, next))
    return distance
                
input = sys.stdin.readline
INF = sys.maxsize
V, E, P = map(int, input().split())
graph = [[] for i in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

if dijkstra(1)[V] == dijkstra(1)[P] + dijkstra(P)[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")