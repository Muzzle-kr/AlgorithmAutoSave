from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

s_x, s_y, s_d = map(int, input().split())
e_x, e_y, e_d = map(int, input().split())

# 동서남북
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
change_dir = [[2, 3], [2, 3], [0, 1], [0, 1]]
    
def bfs():
    q = deque()
    q.append((s_x-1, s_y-1, s_d-1, 0))
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    visited[s_x-1][s_y-1][s_d-1] = 1
    
    while q:
        x, y, d, cnt = q.popleft()
        
        if (x, y, d) == (e_x-1, e_y-1, e_d-1):
            return cnt

        # 1~3칸 직진
        for dis in range(1, 4):
            nx = x + direction[d][0] * dis
            ny = y + direction[d][1] * dis
            nd = d
            
            if 0 <= nx < n and 0 <= ny < m:
                # 벽으로 막혀있으면 탈출
                if graph[nx][ny]:
                    break
                
                if not visited[nx][ny][nd]:
                    visited[nx][ny][nd] = 1
                    q.append((nx, ny, nd, cnt+1))

        for nd in change_dir[d]:
            if not visited[x][y][nd]:
                visited[x][y][nd] = 1
                q.append((x, y, nd, cnt+1))
                
    
print(bfs())
