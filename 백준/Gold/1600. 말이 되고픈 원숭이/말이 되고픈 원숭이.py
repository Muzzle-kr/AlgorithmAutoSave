from collections import deque
import sys
input = sys.stdin.readline
k = int(input())
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [[0, 1], [0, -1], [1, 0], [-1, 0]]
horse = [[1, -2], [1, 2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, -1], [-2, 1]]


# 원숭이를 먼저 다 쓰는 경우
# 원숭이를 벽에 막혔을 때만 쓰는 경우
# 원숭이를 마지막에 다 쓰는 경우

def bfs():
    visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    
    while q:
        x, y, z = q.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][z]-1

        # 일반 점프
        for i, j in dist:
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                if not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
        
        # 말과 같이 점프
        if z < k:
            for i, j in horse:
                hx = x + i
                hy = y + j
                if 0 <= hx < n and 0 <= hy < m and not graph[hx][hy]:
                    if not visited[hx][hy][z+1]:
                        visited[hx][hy][z+1] = visited[x][y][z] + 1
                        q.append((hx, hy, z+1))
    return -1
        
print(bfs())
