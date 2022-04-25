from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
N, M = map(int, input().split())
board = [input() for _ in range(N)]


def chk_valid_coordinate(y, x):
  return 0 <= x < M and 0 <= y < N

def bfs(y, x, d):
  chkBoard = [[False] * M for _ in range(N)]
  chkBoard[0][0] = True
  dq = deque()
  dq.append((0, 0, 1))
  while dq:
    y, x, d = dq.popleft()
    if y == N - 1 and x == M - 1:
      print(d)
      
    nd = d + 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if chk_valid_coordinate(ny, nx) and board[ny][nx] == '1' and not chkBoard[ny][nx]:
        chkBoard[ny][nx] = True
        dq.append((ny, nx, nd))

bfs(0, 0, 0)