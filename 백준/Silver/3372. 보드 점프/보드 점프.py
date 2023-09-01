N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(dp[-1][-1])
            break
        
        cur_cnt = graph[i][j]
        
        if i + cur_cnt < N:
            dp[i+cur_cnt][j] += dp[i][j]
        
        if j + cur_cnt < N:
            dp[i][j+cur_cnt] += dp[i][j]