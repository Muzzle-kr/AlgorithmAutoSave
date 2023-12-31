V, E = map(int, input().split())
dist = [[int(1e9)] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

answer = int(1e9)

for i in range(1, V+1):
    answer = min(answer, dist[i][i])
    
print(answer if answer != int(1e9) else -1)