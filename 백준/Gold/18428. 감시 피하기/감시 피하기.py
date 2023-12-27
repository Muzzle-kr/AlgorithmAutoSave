import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
# 빈 좌표 값
empty_coord = []
board = [list(input().split()) for _ in range(n)]
teacher_coord = []

for i in range(n):
    for j in range(n):
        if board[i][j] == "T":
            teacher_coord.append((i,j))
        elif board[i][j] == "X":
            empty_coord.append((i,j))

combinations_coord = list(combinations(empty_coord, 3))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def observe_student(new_board):
    for x, y in teacher_coord:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            while 0 <= nx < n and 0 <= ny < n:
                if new_board[nx][ny] == "O":
                    break
                elif new_board[nx][ny] == "S":
                    return False
                else:
                    nx += dx[i]
                    ny += dy[i]
    return True

for cc in combinations_coord:
    # 새로운 보드판 생성
    new_board = [board[i][:] for i in range(n)]
    
    # 장애물 설치
    for x, y in cc:
        new_board[x][y] = "O"
    
    result = observe_student(new_board)
    
    if result:
        print("YES")
        break
else:
    print("NO")