from collections import deque

def solution(board):
    N = len(board)
    INF = int(1e9)
    answer = INF
    direction = [[0, 1, 0], [1, 0, 1], [-1, 0, 2], [0, -1, 3]]
    cost_map = [[[INF] * N for _ in range(N) ] for _ in range(4)]
    dq = deque()
    dq.append([0, 0, 0, 0])
    dq.append([0, 0, 0, 1])
    
    while dq:
        x, y, cost, d = dq.popleft()
            
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            nd = direction[i][2]
                
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                new_cost = 100 if nd == d else 600
                tot_cost = new_cost + cost
                if tot_cost < cost_map[nd][nx][ny]:            
                    cost_map[nd][nx][ny] = tot_cost
                    
                    if nx == N-1 and ny == N-1:
                        continue
                    
                    dq.append((nx, ny, tot_cost, nd))
    
    for i in range(4):
        answer = min([answer, cost_map[i][N-1][N-1]])
    return answer