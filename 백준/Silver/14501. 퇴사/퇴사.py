N = int(input())

items = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    time, earn = items[i]
    
    if i + items[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+time] + earn)

print(dp[0])