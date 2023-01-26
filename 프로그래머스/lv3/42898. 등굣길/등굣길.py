def solution(m, n, puddles):
    dp = [[0] * (101) for _ in range(101)]

    for x, y in puddles:
        dp[y][x] = -1
    
    dp[1][1] = 1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1:
                continue
            
            a = 0
            b = 0
            
            if dp[i-1][j] != -1:
                a = dp[i-1][j]
            
            if dp[i][j-1] != -1:
                b = dp[i][j-1]
            
            dp[i][j] += (a + b) % 1000000007
    return dp[n][m]