N = int(input())
temp = [0, 1, 2]
if N < 3:
    print(temp[N-1])
    exit()
    
dp = [0] * (N+1)
dp[1] = 0
dp[2] = 1
dp[3] = 2

for i in range(4, N+1):
    dp[i] = (dp[i-2] + dp[i-1]) * (i-1) % 1000000000
    
print(dp[N])