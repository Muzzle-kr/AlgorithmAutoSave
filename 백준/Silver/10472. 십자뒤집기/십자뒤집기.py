import copy
from collections import deque

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]



def convert_board(board, x, y):
    copy_board = copy.deepcopy(board)
    
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < 3 and 0 <= ny < 3:
            copy_board[nx][ny] = '.' if board[nx][ny] == '*' else '*'
    
    return copy_board

def convert_to_binary(board):
    binary_str = ''
    
    for i in range(3):
        for j in range(3):
            binary_str += '0' if board[i][j] == '.' else '1'
    
    return int(binary_str, 2)

def bfs(goal):
    q = deque()
    init_board = [['.'] * 3 for _ in range(3)]
    q.append((init_board, 0))
    visit = [0] * 1000 # board는 총 9칸이므로 2의 9승, 9자리까지 커버 가능
    visit[convert_to_binary(init_board)] = 1
    
    while q:
        board, time = q.popleft()
        
        if board == goal:
            return time
        
        for i in range(3):
            for j in range(3):
                next_board = convert_board(board, i, j)
                binary_code = convert_to_binary(next_board)
                
                if not visit[binary_code]:
                    q.append((next_board, time + 1))
                    visit[binary_code] = 1
                    
def solution(board):
    result = bfs(board)
    return result

T = int(input())
for _ in range(T):
    board = [list(input().strip()) for _ in range(3)]
    time = solution(board)
    print(time)