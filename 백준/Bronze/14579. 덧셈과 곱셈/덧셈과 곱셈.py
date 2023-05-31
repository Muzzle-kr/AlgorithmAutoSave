a, b = map(int, input().split())
ans = 1

for i in range(a, b+1):
    tmp = 0
    for j in range(i+1):
        tmp += j
    ans *= tmp

print(ans%14579)