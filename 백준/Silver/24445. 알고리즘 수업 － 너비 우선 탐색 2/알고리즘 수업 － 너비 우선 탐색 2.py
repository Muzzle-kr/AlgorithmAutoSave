from collections import deque
n, m, r = map(int, input().split())
lines = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    
    lines[s].append(e)
    lines[e].append(s)
    
for i in range(1, n+1):
    lines[i].sort(reverse=True)
def bfs(s):
    q = deque()
    q.append(s)
    visit = [0 for _ in range(n+1)]
    order = 1
    visit[s] = order
    
    while q:
        c = q.popleft()
        
        for i in lines[c]:
            if visit[i] == 0:
                order += 1
                visit[i] = order
                q.append(i)
            
    return visit[1:]

result = bfs(r)

for a in result:
    print(a)