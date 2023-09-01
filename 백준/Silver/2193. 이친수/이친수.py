N = int(input())

if N == 1:
    print(1)
    exit()
    
dp = [0] * N
dp[0], dp[1] = 1, 1

for i in range(2, N):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N-1])