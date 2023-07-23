def find_minimum_path(friends):
    result = [float('inf')] * (N+1)
    
    for i in range(1, N+1):        
        move_total = 0
        
        for f in friends:
            move_total += graph[f][i]        
        
        result[i] = move_total
    return result.index(min(result))

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    
    # 자기 자신으로 가는 구간 0으로 초기화    
    for i in range(1, N+1): graph[i][i] = 0
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
    k = int(input())
    friends = list(map(int, input().split()))
    
    result = find_minimum_path(friends)
    print(result)