from collections import deque

n = int(input())
dir = (-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)

def bfs():
    q = deque()
    q.append((n, 0, [n]))
    visited = [0] * 1000000
    
    while q:
        x, cnt, route = q.popleft()
        
        if x == 1:
            print(cnt)
            print(*route)
            break
        if x % 3 == 0 and not visited[x//3]:
            q.append((x // 3, cnt + 1, [*route, x // 3]))
            visited[x//3] = 1
        
        if x % 2 == 0 and not visited[x//2]:
            q.append((x // 2, cnt + 1, [*route, x // 2]))
            visited[x//2] = 1
            
        if x - 1 >= 1 and not visited[x-1]:
            q.append((x-1, cnt + 1, [*route, x-1]))
            visited[x-1] = 1

bfs()