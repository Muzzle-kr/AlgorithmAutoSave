from collections import deque

def bfs(s, t):
    q = deque()
    q.append((s, t, 0))
    
    while q:
        x, goal, cnt = q.popleft()
        
        if x == goal:
            return cnt
        
        if x+1 <= goal:
            q.append((x+1, goal, cnt+1))
        
        if x*2 <= goal+3:
            q.append((x*2, goal+3, cnt+1))
        
    return 0

for _ in range(int(input())):
    s, t = map(int, input().split())    
    print(bfs(s, t))