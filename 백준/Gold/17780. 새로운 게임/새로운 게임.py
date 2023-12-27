import sys
read = sys.stdin.readline

# →, ←, ↑, ↓
dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def move(idx):
    x, y, d = chess[idx]
    
    # 가장 아래에 있는 말인지 여부 확인
    if put_chess_map[x][y][0] != idx:
        return False
            
    nx, ny = x + dir[d][0], y + dir[d][1]
    
    if not 0 <= nx < N or not 0 <= ny < N or board[nx][ny] == 2:
        if 0 <= d <= 1:
            nd = (d+1) % 2
        else:
            nd = (d-1) % 2 + 2
        
        # 방향 전환
        chess[idx][2] = nd
        
        # 새로 이동할 칸
        nx, ny = x + dir[nd][0], y + dir[nd][1]
        
        # 새로 이동할 칸에 도달하지 못한다면 실패 처리
        if not 0 <= nx < N or not 0 <= ny < N or board[nx][ny] == 2:
            return False
    
    move_target = []
    
    for i, key in enumerate(put_chess_map[x][y]):
        # 이동할 말들 담기
        if key == idx:
            move_target = put_chess_map[x][y][i:]
            put_chess_map[x][y] = put_chess_map[x][y][:i]
            break
    
    # 초기화 시키기(맨 밑 말만 움직이기 때문에 무조건 없어짐)
    put_chess_map[x][y] = []
    
    # 빨간 칸이라면 반대로 쌓기
    if board[nx][ny] == 1:
        move_target = reversed(move_target)
    
    # 말을 한마리씩 이동시키기
    for mt in move_target:
        put_chess_map[nx][ny].append(mt)
        chess[mt][0], chess[mt][1] = nx, ny
    
    if len(put_chess_map[nx][ny]) >= 4:
        return True
    
    return False
        

N, K = map(int, input().split())
board = [list(map(int, read().split())) for _ in range(N)]
put_chess_map = [[[] for _ in range(N)] for _ in range(N)]
chess = [[] for _ in range(K)]

for i in range(K):
    x, y, d = map(int, read().split())
    chess[i] = [x-1, y-1, d-1]
    put_chess_map[x-1][y-1].append(i)
    
ans = 1

while ans <= 1000:
    for i in range(K):
        flag = move(i)
        if flag:
            print(ans)
            sys.exit()
    ans += 1
print(-1)