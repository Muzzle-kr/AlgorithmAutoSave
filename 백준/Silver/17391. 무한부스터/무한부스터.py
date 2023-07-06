from collections import deque

ROW, COL = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(ROW)]
direction = [[0, 1], [1, 0]]
visited = [[0 for _ in range(COL)] for _ in range(ROW)]
visited[0][0] = 0
dq = deque()
dq.append((0, 0))

while dq:
    y, x = dq.popleft()
    
    for i in range(2):
        next_y, next_x = y, x
        for j in range(board[y][x]):
            next_y, next_x = next_y + direction[i][0], next_x + direction[i][1]
            if 0 <= next_y < ROW and 0 <= next_x < COL and visited[next_y][next_x] == 0:
                dq.append((next_y, next_x))
                visited[next_y][next_x] = visited[y][x] + 1


print(visited[-1][-1])