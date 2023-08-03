import sys

def count_odds(x):
    cnt = 0
    for char in x:
        if char in '13579':
            cnt += 1
    return cnt

def cal(x, cnt):
    if len(x) == 1:
        ans[0] = min(count_odds(x) + cnt, ans[0])
        ans[1] = max(count_odds(x) + cnt, ans[1])
        return
    
    elif len(x) == 2:
        cal(str(int(x[0]) + int(x[1])), cnt + count_odds(x))
    
    else:
        odds = count_odds(x)
        
        for i in range(1, len(x) - 1):
            for j in range(i + 1, len(x)):
                cal(str(int(x[:i]) + int(x[i:j]) + int(x[j:])), cnt + odds)

input = sys.stdin.readline
ans = [sys.maxsize, -sys.maxsize]         
x = input().rstrip()

cal(x, 0)

print(ans[0], ans[1])