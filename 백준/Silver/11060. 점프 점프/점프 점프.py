from collections import deque
n = int(input())
arr = list(map(int, input().split()))


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [False] * (n+1)
    visited[0] = True
    
    while q:
        p, cnt = q.popleft()
        
        if p == n-1:
            return cnt
        
        for i in range(p+1, p+arr[p]+1):
            if i <= n and i >= 0 and not visited[i]:
                q.append((i, cnt + 1))
                visited[i] = True
        
    return -1



print(bfs())