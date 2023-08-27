n = int(input())
m = int(input())
vips = [int(input()) for i in range(m)]

if n == 1:
    if m == 1:
        print(0)
        exit()
    else:
        print(1)
        exit()
        
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# vip가 1명 이상 있다면
ans = 1


        
if m > 0:
    tmp_vip = 0
    
    for i in range(m):
        ans *= dp[vips[i] - 1 - tmp_vip]
        tmp_vip = vips[i]
    ans *= dp[n-tmp_vip]
else:
    ans = dp[n]

print(ans)