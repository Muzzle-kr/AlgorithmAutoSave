import sys
import heapq
import math


def check_prime_number(n):
    
    if n < 2:
        return False
    elif n == 2:
        return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def dijkstra():
    q = []
    INF = float('inf')
    heapq.heappush(q, (0, 0))
    distance = [INF] * (n+2)
    distance[0] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        x, y = edges[now]
        
        if distance[now] < dist:
            continue
        
        for i in range(n+2):
            nx, ny = edges[i]
            dist_diff = int(((x-nx)**2 + (y-ny)**2)**0.5)
            
            if check_prime_number(dist_diff):
                cost = math.floor(dist + dist_diff)

                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))
                    
    return -1 if distance[-1] == INF else distance[-1]

input = sys.stdin.readline
x1, y1, x2, y2 = map(int, input().split())
n = int(input())
edges = [(x1, y1)]

for _ in range(n):
    x, y = map(int, input().split())
    edges.append((x, y))

edges.append((x2, y2))
print(dijkstra())