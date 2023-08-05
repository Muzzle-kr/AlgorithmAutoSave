import sys
from collections import deque

input = sys.stdin.readline
arr = [""] * 100001

def bfs():
    q = deque()
    q.append((0, 0, 1, 0, [[0, 0]])) # x, y, 방향, 시간
    board[0][0] = 2
    while q:
        x, y, d, time, tail = q.popleft()        

        if arr[time] == "L":
            d -= 1
        elif arr[time] == "D":
            d += 1
        
        if d < 0:
            d = 3
        elif d > 3:
            d = 0
            
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            return time + 1
        else:
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny, d, time+1, tail+[[nx, ny]]))
            elif board[nx][ny] == 0:
                # 꼬리가 위치한 칸을 비워준다.
                tx, ty = tail.pop(0)
                board[tx][ty] = 0
                board[nx][ny] = 2
                q.append((nx, ny, d, time+1, tail+ [[nx,ny]]))
            elif board[nx][ny] == 2:
                return time+1
            
N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

for _ in range(int(input())):
    second, d = input().split()
    arr[int(second)] = d


print(bfs())