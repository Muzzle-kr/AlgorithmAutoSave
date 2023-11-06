n = int(input())
arr = [0] + list(map(int, input().split()))
INF = int(1e9)

dp = [INF] * (n+1)


for i in range(1, n+1):
    price = arr[i]
    cnt = i
    
    if cnt > n:
        continue
    
    dp[cnt] = min(price, dp[cnt])
    
    for j in range(n-cnt+1):
        dp[cnt+j] = min(dp[cnt+j], dp[j] + price)    
        
print(dp[-1])