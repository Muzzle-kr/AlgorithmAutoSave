r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
count = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

flag = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == "W":
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == "S":
                        flag = True
                        break
    if flag:
        break
    
if flag:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if graph[i][j] == ".":
                graph[i][j] = "D"
    
    for g in graph:
        print("".join(g))