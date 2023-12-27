from collections import deque

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    
    cnt = 0    
    s = maps[i][j]
    
    while dq:
        x, y = dq.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == s and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
    return cnt * s
                

N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dice = [1, 2, 3, 4, 5, 6]
# 동 서 북 남
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, dir, ans = 0, 0, 0, 0

for _ in range(K):
    # 칸이 없으면 방향 바꾸기
    if not 0 <= x + dx[dir] < N or not 0 <= y + dy[dir] < M:
        dir = (dir + 2) % 4
        
    x += dx[dir]
    y += dy[dir]
        
    # 점수 획득하기
    ans += bfs(x, y)
    
    # 이동 방향 결정
    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif dir == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        
    
    if dice[5] > maps[x][y]:
        dir = (dir + 1) % 4
    elif dice[5] < maps[x][y]:
        dir = (dir + 3) % 4
        
print(ans)