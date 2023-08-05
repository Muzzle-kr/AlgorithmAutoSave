import copy
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

def fill(arr, mode, x, y):
    
    for m in mode:
        nx = x
        ny = y
        while True:
            nx += dx[m]
            ny += dy[m]
            
            # 범위 넘어가면 중단
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            
            # 벽에 막히면 중단
            if arr[nx][ny] == 6:
                break
            
            # 감시 처리
            arr[nx][ny] = 7
            
def dfs(depth, arr):
    global ans
    
    if depth == len(cctvs):
        cnt = 0
        
        for i in range(N):
            cnt += arr[i].count(0)
        
        ans = min(ans, cnt)
        return
                
    tmp = copy.deepcopy(arr)
    x, y, nth = cctvs[depth]
    for mode in cctv_mode[nth]:
        fill(tmp, mode, x, y)
        dfs(depth+1, tmp)
        # 보드 초기화
        tmp = copy.deepcopy(arr)
        
        
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
ans = sys.maxsize
    
    
for i in range(N):
    for j in range(M):
        if 0 < graph[i][j] < 6:
            cctvs.append((i, j, graph[i][j]))

dfs(0, graph)
print(ans)

