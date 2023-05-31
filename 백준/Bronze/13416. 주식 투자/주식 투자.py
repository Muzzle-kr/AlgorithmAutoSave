import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = int(input())    
    ans = 0
    
    for _ in range(t):
        a, b, c = map(int, input().split())
        hi_price = max(a, b, c)

        if hi_price > 0:
            ans += hi_price
    print(ans)