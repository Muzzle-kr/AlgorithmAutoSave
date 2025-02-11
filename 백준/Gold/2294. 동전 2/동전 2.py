n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
INF = 1e9

dp = [INF] * (k + 1)
dp[0] = 0

for i in range(k + 1):
    
    if dp[i] != INF:
        for coin in coins:
            if i + coin <= k:
                dp[coin + i] = min(dp[i + coin], dp[i] + 1)
    
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
