from collections import deque

def bfs(board, sx, sy, ex, ey, x_length, y_length):
    queue = deque()
    queue.append([sx, sy, 0])
    visited = [[0] * y_length for _ in range(x_length)]
    visited[sx][sy] = 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # print(f'sx: {sx}, sy: {sy}, ex: {ex}, ey: {ey}')
    while queue:
        x, y, count = queue.popleft()
        
        # print(f'x: {x}, y: {y}, count: {count}')
        if x == ex and y == ey:
            return count
        
        for i in range(4):
            nx = x
            ny = y
            
            # print(f'nx: {nx}, ny: {ny}, i: {i}')
            while True:
                nx += dx[i]
                ny += dy[i]    
                
                # 게임판을 나가거나 장애물에 부딪힐 경우
                if nx < 0 or nx >= x_length or ny < 0 or ny >= y_length or board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                                
            if 0 <= nx < x_length and 0 <= ny < y_length:
                if not visited[nx][ny] and board[nx][ny] != 'D':
                    visited[nx][ny] = 1
                    queue.append([nx, ny, count+1])
    return -1

def solution(board):
    
    
    x_length = len(board)
    y_length = len(board[0])
    sx, sy = [0, 0]
    ex, ey = [len(board)-1, len(board)-1]
    
    for i in range(x_length):
        for j in range(y_length):
            if board[i][j] == 'R':
                sx, sy = [i, j]
            elif board[i][j] == 'G':
                ex, ey = [i, j]
    
    answer = bfs(board, sx, sy, ex, ey, x_length, y_length)
    
    return answer