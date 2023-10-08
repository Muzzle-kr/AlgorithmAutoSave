import sys
sys.setrecursionlimit(10**6)

def solution(grid):
    # 좌는 x,y -> y, -x, 우는 x,y -> y, x
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    h = len(grid)
    w = len(grid[0])
    
    def dfs(tx, ty, td, x, y, d, cnt, route_set):        
        # 이미 방문한 경로라면 return
        if (x, y, d) in visited:
            return -1
        
        # 방문 처리
        visited[(x, y, d)] = True
        
        # 왼쪽, 오른쪽 방향 전환
        if grid[x][y] == 'L':
            d = (d - 1) % 4
        elif grid[x][y] == 'R':
            d = (d + 1) % 4
        
        cnt += 1    
        nx = (x + direction[d][0])
        ny = (y + direction[d][1])
        
        # 범위를 벗어나면 반대편으로 이동
        if nx < 0:
            nx = h - 1  
        elif nx >= h:
            nx = 0
            
        if ny < 0:
            ny = w - 1  
        elif ny >= w:
            ny = 0
        
        if nx == tx and ny == ty and d == td:
            return cnt
        
        return dfs(tx, ty, td, nx, ny, d, cnt, route_set)
    
    result_arr = []
    visited = {}
    
    for i in range(h):
        for j in range(w):
            for k in range(4):
                # 이미 방문했다면 skip
                if (i, j, k) in visited:
                    continue
                
                route_set = set()
                result = dfs(i, j, k, i, j, k, 0, route_set)
                if result != -1:
                    result_arr.append(result)
    return sorted(result_arr)