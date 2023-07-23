n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1): graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    
    # 일방 통행이라면 반대 case 1 추가
    if c == 0:
        graph[a][b] = 0
        graph[b][a] = 1
    else:
        graph[a][b] = 0
        graph[b][a] = 0
        
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(graph[s][e])