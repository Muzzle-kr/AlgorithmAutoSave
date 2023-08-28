n, k = map(int, input().split())

dp = [10001] * (k + 1)
coins = [int(input()) for _ in range(n)]
dp[0] = 0
    
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])