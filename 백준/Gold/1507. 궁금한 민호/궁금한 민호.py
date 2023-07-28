import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
discard = [[False] * N for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or j == k or k == i:
                continue
            
            if graph[i][j] == graph[i][k] + graph[k][j]:
                discard[i][j] = True
                
            if graph[i][j] > graph[i][k] + graph[k][j]:
                print(-1)
                exit(0)

ans = 0

for i in range(N):
    for j in range(N):
        if not discard[i][j]:
            ans += graph[i][j]
print(ans//2)