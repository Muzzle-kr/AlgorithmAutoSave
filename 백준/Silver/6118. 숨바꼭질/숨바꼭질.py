import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()
    distance = 1
    shed = set()
    visited[1] = True
    
    for i in graph[1]:
        q.append((i, 1))
        visited[i] = True
        shed.add(i)

    while q:
        x, cnt = q.popleft()
        
        for xx in graph[x]:
            if not visited[xx]:
                q.append((xx, cnt+1))
                visited[xx] = True
                
                if cnt + 1 > distance:
                    distance = cnt + 1
                    shed = set([xx])
                else:
                    shed.add(xx)
    
    print(min(shed), distance, len(shed))    

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int ,input().split())
    
    graph[a].append(b)
    graph[b].append(a)

bfs()
