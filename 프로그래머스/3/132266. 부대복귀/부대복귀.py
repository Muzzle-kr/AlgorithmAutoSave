from collections import deque

def solution(n, roads, sources, start):
    INF = int(1e9)
    answer = []
    dist = [0] * (n+1)
    matrix = [[] for _ in range(n+1)]
    
    for a, b in roads:
        matrix[a].append(b)
        matrix[b].append(a)
        
    dist = [INF] * (n+1)
    visit = [False] * (n+1)
    visit[start] = True
    dist[start] = 0        
    q = deque([start])
        
    while q:
        cur_node = q.popleft()
        
        for next_node in matrix[cur_node]:
            if dist[cur_node] + 1 < dist[next_node]:
                dist[next_node] = dist[cur_node] + 1
                visit[next_node] = True
                q.append(next_node)
    
    for source in sources:
        shortest_dist = dist[source]
        if shortest_dist == INF:
            answer.append(-1)
        else:
            answer.append(shortest_dist)
    return answer