n = int(input())
arr = [int(input()) for _ in range(n)]
arr = [0] + arr
dp = [1] * (n+1)

for i in range(1, n+1):
    for j in range(1, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
