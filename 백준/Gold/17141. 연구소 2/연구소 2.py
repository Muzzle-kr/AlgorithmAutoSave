'''
모든 빈칸에 바이러스를 퍼뜨리는 최소 시간 구하기
예외: 모든 빈칸에 바이러스를 퍼뜨릴 수 없은면 -1 return
'''

from itertools import combinations
from collections import deque
import copy
n, v = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
can_virus = []
result = int(1e9)

# 바이러스가 존재하는 지 확인
def check_exist_virus_in_graph(new_graph):
    for i in range(n):
        for j in range(n):
            if not new_graph[i][j]:
                return True
    return False

def bfs(cv):
    q = deque()
    new_graph = copy.deepcopy(graph)
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    
    # 바이러스 바꿔주기
    for i, j in cv:
        new_graph[i][j] = "v"
        q.append((i, j, 0))
    
    # 남은 빈 바이러스는 빈칸으로 바꿔주기
    for i, j in can_virus:
        if (i, j) not in cv:    
            new_graph[i][j] = 0
            
        
    while q:
        x, y, c = q.popleft()
        
        cnt = max(cnt, c)
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] != 1 and new_graph[nx][ny] != "v":
                    visited[nx][ny] = True
                    new_graph[nx][ny] = "v"
                    q.append((nx, ny, c+1))
        
    
    if check_exist_virus_in_graph(new_graph):
        return int(1e9)
    else:
        return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            can_virus.append((i, j))
            
can_virus_list = list(combinations(can_virus, v))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for cv in can_virus_list:
    result = min(result, bfs(cv))
    
print(result if result != int(1e9) else -1)