import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = {}
def DFS(now, visited):
    if visited == (1 << N) - 1:
        if graph[now][0]:
            return graph[now][0]
        else:
            return int(1e9)
    
    if (now, visited) in dp:
        return dp[(now, visited)]
    
    min_cost = int(1e9)
    
    for next in range(1, N):
        if graph[now][next] == 0 or visited & (1 << next):
            continue
        
        cost = DFS(next, visited | (1 << next)) + graph[now][next]
        min_cost = min(min_cost, cost)
    dp[(now, visited)] = min_cost
    return min_cost
print(DFS(0, 1))