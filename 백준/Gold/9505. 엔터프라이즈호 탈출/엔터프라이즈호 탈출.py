import heapq as hq

def dijkstra(i, j, graph, ship):
    q = []
    
    INF = int(1e9)
    visited = [[INF for _ in range(w)] for _ in range(h)]
    visited[i][j] = 0
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    hq.heappush(q, (0, i, j))
    
    while q:
        time, x, y = hq.heappop(q)
        
        if x == 0 or x == h-1 or y == 0 or y == w-1:
            return time
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx == i and ny == j:
                continue
            
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] > visited[x][y] + ship[graph[nx][ny]]:
                    visited[nx][ny] = visited[x][y] + ship[graph[nx][ny]]
                    hq.heappush(q, (visited[nx][ny], nx, ny))

for _ in range(int(input())):
    k, w, h = map(int, input().split())
    cooling_ship = {}
    
    for _ in range(k):
        a, c = input().split()
        cooling_ship[a] = int(c)
    
    graph = [list(input()) for _ in range(h)]
    
    isFlag = False
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "E":
                print(dijkstra(i, j, graph, cooling_ship))
                isFlag = True
                break
        if isFlag:
            break
        