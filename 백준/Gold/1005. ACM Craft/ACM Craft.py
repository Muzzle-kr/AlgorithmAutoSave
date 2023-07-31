import heapq as hq
import sys

def dijkstra():
    queue = []
    dist = [INF] * (N+1)
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            hq.heappush(queue, (times[i], i))
            dist[i] = times[i]
    
    while queue:
        cur_dist, cur_node = hq.heappop(queue)
        
        for next_node in edges[cur_node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                next_dist = cur_dist + times[next_node]
                if dist[next_node] > next_dist:
                    dist[next_node] = next_dist
                    hq.heappush(queue, (next_dist, next_node))
    return dist
                

input = sys.stdin.readline
T = int(input())
INF = sys.maxsize
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    edges = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    
    for _ in range(K):
        a, b = map(int, input().split())
        edges[a].append(b)
        indegree[b] += 1

    W = int(input())
    
    print(dijkstra()[W])