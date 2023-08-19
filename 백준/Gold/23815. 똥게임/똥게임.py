import sys
input = sys.stdin.readline

def cal(o, a, b):
    if o == "+": return a+b
    elif o == "*": return a*b
    elif o == "-": return a-b
    else: return a//b
    
N = int(input())
dp = [1, -10]

for _ in range(N):
    a, b = input().rstrip().split()
    a_o, a_n = a
    b_o, b_n = b
    
    if dp[0] > 0:
        c = max(cal(a_o, dp[0], int(a_n)), cal(b_o, dp[0], int(b_n)))
    d = max(cal(a_o, dp[1], int(a_n)), cal(b_o, dp[1], int(b_n)))
    
    dp[1] = max(dp[0], d)
    dp[0] = c
    
    if max(dp) <= 0:
        print('ddong game')
        break
else:
    print(max(dp))