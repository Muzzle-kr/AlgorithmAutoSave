from collections import deque
arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort()

dp = [0] * len(arr)
dp[0] = arr[0][2]

for i in range(1, len(arr)):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i][2])
    
print(dp[-1])