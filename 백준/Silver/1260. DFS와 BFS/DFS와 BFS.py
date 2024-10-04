import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().rstrip().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

visited = [False] * (N + 1)

for a in arr:
    a.sort()

dfs_result = []
bfs_result = []

def dfs(idx):
    visited[idx] = True
    dfs_result.append(idx)
    for next in arr[idx]:
        if not visited[next]:
            dfs(next)
    return

def bfs(idx):
    q = deque()
    q.append(idx)
    visited = [False] * (N + 1)
    visited[idx] = True

    while q:
        i = q.popleft()
        bfs_result.append(i)
        
        if len(bfs_result) == N:
            break
        
        for next in arr[i]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)