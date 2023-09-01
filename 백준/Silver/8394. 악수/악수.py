N = int(input())
dp = [1] * (N)
dp[1] = 2

for i in range(2, N):
    dp[i] = dp[i-2] % 10 + dp[i-1] % 10

print(dp[N-1]%10)