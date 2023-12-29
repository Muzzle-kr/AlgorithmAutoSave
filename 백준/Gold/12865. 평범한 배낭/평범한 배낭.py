N, K = map(int, input().split())
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    w, v = items[i][0], items[i][1]
    
    for j in range(1, K+1):
        # 무게가 더 크면 이전 가치를 가져오기
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])