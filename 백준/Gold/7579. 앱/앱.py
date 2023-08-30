N, M = map(int, input().split())
bytes = [0] + list(map(int, input().split())) #byte
costs = [0] + list(map(int, input().split())) #cost
dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)] # i번째 앱까지 비용 j로, 얻을 수 있는 최대 메모리를 저장
result = sum(costs) #열의 최댓값

for i in range(1, N+1):
    byte = bytes[i]
    cost = costs[i] 
    
    for j in range(1, sum(costs)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte)
        
        if dp[i][j] >= M:
            result = min(result, j)
print(result)