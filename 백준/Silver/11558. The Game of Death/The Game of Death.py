from collections import deque

def bfs():
    q = deque()
    q.append((1, 0))
    visited = [False] * (n+1)
    visited[0] = True
    
    while q:
        x, cnt = q.popleft()

        # print(f'x: {x}, cnt: {cnt}')
        if x == n:
            return cnt
        
        next = arr[x]
        if not visited[next]:
            visited[next] = True
            q.append((next, cnt+1))
        
    return 0
    
T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0]
    
    for _ in range(n):
        arr.append(int(input()))
    
    print(bfs())