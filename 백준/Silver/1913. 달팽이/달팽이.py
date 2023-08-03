N = int(input())
target = int(input())
graph = [[0] * N for _ in range(N)]


# 좌측
num = N**2
x, y, i = 0, 0, 0

while num > 0:
    y = i
    for j in range(i, N-i):
        x = j
        if graph[x][y] == 0:
            graph[x][y] = num
            num -= 1
    
    for j in range(i, N-i):
        y = j
        if graph[x][y] == 0:
            graph[x][y] = num
            num -= 1
    
    for j in range(i, N-i):
        x = N - j - 1
        if graph[x][y] == 0:
            graph[x][y] = num
            num -= 1
            
    for j in range(i, N-i):
        y = N - j - 1
        if graph[x][y] == 0:
            graph[x][y] = num
            num -= 1
    i += 1

for g in graph:
    print(*g)
    
for i in range(N):
    for j in range(N):
        if graph[i][j] == target:
            print(i+1, j+1)