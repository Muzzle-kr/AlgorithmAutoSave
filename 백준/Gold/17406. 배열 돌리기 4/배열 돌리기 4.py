from itertools import permutations
from copy import deepcopy
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]
ans = sys.maxsize

for p in permutations(rcs, K):
    # 2. 회전
    copy_graph = deepcopy(graph)  # 원본리스트 카피
    
    for r, c, s in p:
        r -= 1
        c -= 1
        
        for n in range(s, 0, -1):
            tmp = copy_graph[r-n][c+n]
            
            copy_graph[r-n][c-n+1:c+n+1] = copy_graph[r-n][c-n:c+n]  # ->
            
            for row in range(r-n, r+n):  # ↑
                copy_graph[row][c-n] = copy_graph[row+1][c-n]
                
            copy_graph[r+n][c-n:c+n] = copy_graph[r+n][c-n+1:c+n+1]  # <-
            
            for row in range(r+n, r-n, -1):  # ↓
                copy_graph[row][c+n] = copy_graph[row-1][c+n]
                
            copy_graph[r-n+1][c+n] = tmp

    for row in copy_graph:
        ans = min(ans, sum(row))

print(ans)