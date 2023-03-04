import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
N, M = map(int, input().split())

matrix = [[0] * N for _ in range(N)]

for i in range(M):
  i, j = map(lambda x: x - 1, map(int, input().split()))
  matrix[i][j] = matrix[j][i] = 1
 
ans = 0 
chk = [False] * N

def dfs(now): 
  for nxt in range(N):
    if matrix[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      dfs(nxt)

for i in range(N):
  if not chk[i]:
    ans += 1
    chk[i] = True
    dfs(i)

print(ans)