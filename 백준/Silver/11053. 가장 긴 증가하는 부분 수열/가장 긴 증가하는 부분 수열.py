N = int(input())

arr = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    for j in range(i):
        # print(f'i: {i}, j: {j}')
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp) + 1)