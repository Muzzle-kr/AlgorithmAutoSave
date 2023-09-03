N = int(input())
ans = ""

if not N:
    print(0)
else:
    while N:
        if N % (-2):
            ans = '1' + ans
            N = N // -2 + 1
        else:
            ans = '0' + ans
            N //= -2
    print(ans)
