import heapq
import sys

def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_walk_time(x1, y1, x2, y2):
    return get_distance(x1, y1, x2, y2) / 5

def get_cannon_time(x1, y1, x2, y2):
    dist = get_distance(x1, y1, x2, y2)
    return (abs(50-dist) / 5) + 2

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 1))
    
    time = [INF] * (N+3)
    visit = [False] * (N+3)
    
    while queue:
        cur_time, cur_node = heapq.heappop(queue)
        
        if visit[cur_node]:
            continue
        
        visit[cur_node] = True
        
        for i in range(1, N+3):
            if i == cur_node: continue
            
            next_time = get_walk_time(edges[cur_node-1][0], edges[cur_node-1][1], edges[i-1][0], edges[i-1][1])
            
            if cur_node != 1 and cur_node != N+2:
                next_time = min(next_time, get_cannon_time(edges[cur_node-1][0], edges[cur_node-1][1], edges[i-1][0], edges[i-1][1]))
            
            if next_time + cur_time < time[i]:
                time[i] = next_time + cur_time
                heapq.heappush(queue, (time[i], i))
    return time
            
            

input = sys.stdin.readline
INF = sys.maxsize
edges = []

SX, SY = map(float, input().split())
EX, EY = map(float, input().split())

edges.append((SX, SY))
N = int(input())

for _ in range(N):
    a, b = map(float, input().split())
    edges.append((a, b))
    
edges.append((EX, EY))

d = dijkstra()
print(d[N+2])