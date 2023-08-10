import sys


def one_check(b, N, M):
    dx = [1, -1]
    dy = [1, -1]
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                continue
            check_x = False
            check_y = False
            for i in range(2):
                nx = x + dx[i]
                if 0 <= nx < M and board[y][nx] == 1:
                    check_x = True
                ny = y + dy[i]
                if 0 <= ny < N and board[ny][x] == 1:
                    check_y = True
            if check_x and check_y:
                return f'{y+1} {x+1}'

    return None


N, M, K = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

seed = 0

for i in board:
    for j in i:
        if j == 1:
            seed += 1

if 2*K == seed:
    print(0)
    exit(0)

print(2*K - seed)

if K == 1:
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                print(f'{y+1} {x+1}') 
                exit(0)

if 2*K - 1 == seed:
    check = one_check(board, N, M)
    if check is not None:
        print(check)
        exit(0)

start_x, start_y = 2001, 2001
end_x, end_y = -1, -1

for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            start_x = min(x, start_x)
            start_y = min(y, start_y)
            end_x = max(x, end_x)
            end_y = max(y, end_y)

if start_x == end_x:
    for i in range(2*K - seed):
        print(f'{start_y + seed - K + i + 1} {start_x + 1}')
    exit(0)
if start_y == end_y:
    for i in range(2*K - seed):
        print(f'{start_y + 1} {start_x + seed - K + i + 1}')