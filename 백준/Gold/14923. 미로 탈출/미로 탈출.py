from collections import deque

def bfs(hx, hy):
    q = deque()
    q.append((hx-1, hy-1, 0, 0))
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[hx-1][hy-1][0] = True
    
    while q:
        x, y, cnt, magic = q.popleft()
        
        # print(f'x: {x}, y: {y}, cnt: {cnt}, magic: {magic}')
        if x == ex - 1 and y == ey - 1:
            return cnt
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][magic]:
                # 갈 수 있는 길이라면
                if graph[nx][ny] == 0:
                    q.append((nx, ny, cnt + 1, magic))
                    visited[nx][ny][magic] = True
                # 막힌 길이라면 마법을 쓸 수 있는지 확인하고 쓴다.
                else:
                    if not magic:
                        q.append((nx, ny, cnt + 1, 1))
                        visited[nx][ny][magic] = True
    return -1
n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(hx, hy))