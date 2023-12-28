n = int(input())
arr = sorted(list(map(int, input().split())))
min_total = int(1e10)
ans = 0

if n % 2 == 1:
    ans = arr[n // 2]
else:
    ans = arr[n // 2 - 1]

print(ans)