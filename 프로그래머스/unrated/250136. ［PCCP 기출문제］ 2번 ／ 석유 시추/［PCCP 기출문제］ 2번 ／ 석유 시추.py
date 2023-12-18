from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    answer = 0
    
    direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    oil_named_map = {}
    
    visit = [[0] * m for _ in range(n)]
    oil_area_name = 1
    
    for j in range(m):
        for i in range(n):
            amount_oil = 0
            if land[i][j] == 1 and visit[i][j] == 0:
                # 오일 지역 번호 +1
                oil_area_name += 1
                visit[i][j] = oil_area_name
                
                queue = deque()
                queue.append((i, j))
                
                while queue:
                    dx, dy = queue.popleft()
                    amount_oil += 1
                    oil_named_map[oil_area_name] = amount_oil
                    
                    for k in range(4):
                        nx = dx + direction[k][0]  
                        ny = dy + direction[k][1]
                        
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and visit[nx][ny] == 0:
                                visit[nx][ny] = oil_area_name
                                queue.append((nx, ny))
    
    for j in range(m):
        oil_arr = []
        oil_cnt = 0
        
        for i in range(n):
            visit_oil_name = visit[i][j]
            if visit_oil_name != 0 and visit_oil_name not in oil_arr:
                oil_cnt += oil_named_map[visit_oil_name]
                oil_arr.append(visit_oil_name)
        answer = max(answer, oil_cnt)
            
    return answer