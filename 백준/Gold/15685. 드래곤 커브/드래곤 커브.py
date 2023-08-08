n = int(input())
graph = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    
    graph[x][y] = 1
    curve = [d]
    
    for i in range(g):
        length = len(curve)
        for k in range(length-1, -1, -1):
            curve.append((curve[k]+1)%4)
    
    for c in curve:
        
        # 1세대
        x += dx[c]
        y += dy[c]
        
        graph[x][y] = 1

ans = 0

for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i+1][j+1] and graph[i][j+1]:
            ans += 1
print(ans)