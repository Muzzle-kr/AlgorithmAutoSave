import sys

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
largest = 0

def dfs(x, y, route, largest):
    largest = max(largest, len(route))
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] not in route:
            route.add(graph[nx][ny])
            largest = dfs(nx, ny, route, largest)
            route.remove(graph[nx][ny])
    
    return largest

initial_route = set([graph[0][0]])
largest = dfs(0, 0, initial_route, largest)
print(largest)