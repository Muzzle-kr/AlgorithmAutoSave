from collections import deque

n, m = map(int, input().split())
s, e = map(int, input().split())
visited = [0] * (n+1)
teleport = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    teleport[x].append(y)
    teleport[y].append(x)
    
def bfs(s):
    q = deque()
    q.append((s, 0))
    visited[s] = 1
    
    while q:
        s_p, cnt = q.popleft()
        
        # 주예가 방주 만난 곳에 도착했다면
        if s_p == e:
            print(cnt)
            break
        
        if 1 <= s_p + 1 <= n and not visited[s_p+1]:
            visited[s_p+1] = 1
            q.append((s_p+1, cnt+1))
        if 1 <= s_p - 1 <= n and not visited[s_p-1]:
            visited[s_p-1] = 1
            q.append((s_p-1, cnt+1))
        
        # 텔레포트 계산하기
        for e_p in teleport[s_p]:
            if not visited[e_p]:
                visited[e_p] = 1
                q.append((e_p, cnt+1))
bfs(s)