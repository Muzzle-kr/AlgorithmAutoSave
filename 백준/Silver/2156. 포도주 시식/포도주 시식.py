N = int(input())
wine = [int(input()) for _ in range(N)]


dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    dp[i][1] = wine[i]
    
'''
dp[x][0] => 이번 포도주를 안마시고 저번 포도주의 최댓값
dp[x][1] => 이번 포도주를 마시고 저번 포도주를 안마신 것
dp[x][2] => 이전 포도주와 이번 포도주를 마신 것

'''
for i in range(1, N):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = dp[i-1][1] + wine[i]
        
print(max(dp[N-1]))