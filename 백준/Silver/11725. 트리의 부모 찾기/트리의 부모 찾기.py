from collections import deque

N = int(input())
links = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    
    links[a].append(b)
    links[b].append(a)

answer = [0] * (N+1)    

def bfs():
    q = deque()
    q.append(1)
    
    while q:
        now = q.popleft()    
        for nxt in links[now]:
            if answer[nxt] == 0:
                answer[nxt] = now
                q.append(nxt)

bfs()

result = answer[2:]
for r in result:
    print(r)