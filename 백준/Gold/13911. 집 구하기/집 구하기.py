import heapq as hq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    dist = [float('inf')] * (V+3)
    dist[start] = 0
    hq.heappush(q, (0, start))
    
    while q:
        cur_dist, cur_node = hq.heappop(q)
        
        if dist[cur_node] < cur_dist:
            continue
        
        
        for next_node, next_dist in edges[cur_node]:
            # 가상의 노드는 skip
            if next_node == m_node or next_node == s_node:
                continue
            
            if dist[next_node] > cur_dist + next_dist:
                dist[next_node] = cur_dist + next_dist
                hq.heappush(q, (dist[next_node], next_node))
    return dist
V, E = map(int, input().split())
edges = [[] for _ in range(V+3)] # 가상의 노드 2개 추가

for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
    edges[v].append((u, w))

M, m_condition = map(int, input().split())
m_list = list(map(int, input().split()))
S, s_condition = map(int, input().split())
s_list = list(map(int, input().split()))

m_node = V+1
s_node = V+2

# 가상 노드 연결
for m in m_list:
    edges[m_node].append((m, 0))
    edges[m].append((m_node, 0))

for s in s_list:
    edges[s_node].append((s, 0))
    edges[s].append((s_node, 0))

dist_m = dijkstra(m_node)
dist_s = dijkstra(s_node)


result = float('inf')
for i in range(1, V+1):
    if i in m_list: continue
    if i in s_list: continue
    
    if dist_m[i] <= m_condition and dist_s[i] <= s_condition:
        result = min(result, dist_m[i] + dist_s[i])

if result == float('inf'):
    print(-1)
else:
    print(result)