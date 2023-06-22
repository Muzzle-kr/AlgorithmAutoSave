n = int(input())
time = []
earn = []
dp = [0 for _ in range(n+1)]

for _ in range(n):
    t, e = map(int, input().split())
    time.append(t)
    earn.append(e)
    
for i in range(n-1, -1, -1):
    # 퇴사일을 넘어갈 경우 이전 값을 가져옴
    if i + time[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[time[i]+i] + earn[i])
print(dp[0])