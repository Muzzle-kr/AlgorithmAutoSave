n = int(input())
length = len(str(n))
ans = 0

for i in range(1, length):
    ans += i * (10 ** i - (10 ** (i-1)))

ans += (n - (10 ** (length - 1)) + 1) * length

print(ans)