from collections import deque
from itertools import combinations
import copy

def bfs(virus):
    new_graph = copy.deepcopy(graph)
    q = deque()
    visited = [[-1] * n for _ in range(n)]    
    
    # 선택된 활성화 바이러스 표기
    for x, y in virus:
        q.append((x, y))
        visited[x][y] = 0
    time = 0
    vac_cnt = 0
    
    while q:
        x, y = q.popleft()
        
            
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            
            # 벽을 벗어나면 skip
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            # 벽을 만나거나 방문한 칸은 skip
            if new_graph[nx][ny] == 1 or visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
            
            if graph[nx][ny] == 0:
                vac_cnt += 1
                time = max(time, visited[nx][ny])
    
    if vac_cnt != empty_cnt:
        return -1
    else:
        return time

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus_arr = []
empty_cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus_arr.append((i, j))
        if graph[i][j] == 0:
            empty_cnt += 1

virus_combi = list(combinations(virus_arr, m))
answer = []

for virus in virus_combi:
    time = bfs(virus)
    if time != -1:
        answer.append(time)

if not answer:
    print(-1)
else:
    print(min(answer))