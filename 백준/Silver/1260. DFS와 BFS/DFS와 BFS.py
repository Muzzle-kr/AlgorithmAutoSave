import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]

    
for _ in range(m):
    a, b = map(int, input().split())
    
    arr[a].append(b)
    arr[b].append(a)

visit = [0] * (n + 1)

dfsArr = []

for i in arr:
    i.sort()

def dfs(v):
    visit[v] = 1
    dfsArr.append(v)
    
    for i in arr[v]:
        if visit[i] == 0:
            dfs(i)
    return
dfs(v)

visit = [0] * (n + 1)

bfsArr = []
print(*dfsArr)


def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 1
    
    while q:
        vv = q.popleft()
        bfsArr.append(vv)
        if len(bfsArr) == n:
            break
        for i in arr[vv]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)
    print(*bfsArr)
    
bfs(v)