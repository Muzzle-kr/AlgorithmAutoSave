import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(int(input()))

cur = 1
ans = 0    
for _ in range(M):
    ans += 1
    
    dice = int(input())
    cur += dice
    
    if cur >= N:
        print(ans)
        break 

    cur += graph[cur-1]
    
    if cur >= N:
        print(ans)
        break 