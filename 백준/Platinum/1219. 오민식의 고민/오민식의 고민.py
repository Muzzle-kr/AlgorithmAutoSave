import sys
from collections import deque
input = sys.stdin.readline
fees = []
N, S, E, D = map(int, input().split())

for i in range(D):
    s, e, w = map(int, input().split())
    fees.append((s, e, w))
    
costs = list(map(int, input().split()))
edges = []
result = [-1 * sys.maxsize] * N
result[S] = costs[S]

for i in fees:
    s, e, w = i
    w = costs[e] - w
    edges.append((s, e, w))

for _ in range(N-1):
    for i in edges:
        s, e, w = i
        if result[s] != -1 * sys.maxsize and result[e] < result[s] + w:
            result[e] = result[s] + w


def bfs(S, E):
    q = deque()
    q.append(S)
    visited = [False]*(N)
    visited[S] = True
    while q:
        now = q.popleft()
        if now ==  E:
            return True
        
        for s, e, w in edges:
            if s==now:
                if not visited[e]:
                    visited[e] = True
                    q.append(e)
    return False

isCycle = False
for i in edges:
        s, e, w = i
        if result[s] != -1 * sys.maxsize and result[e] < result[s] + w:
            if bfs(s, E):
                isCycle = True
                break

if result[E] == -1 * sys.maxsize:
    print("gg")
else:
    if isCycle:
        print("Gee")
    else:
        print(result[E])