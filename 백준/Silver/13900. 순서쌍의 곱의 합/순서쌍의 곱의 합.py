n = int(input())
arr = list(map(int, input().split()))
tmp_sum = sum(arr)
ans = 0

for a in arr:
    tmp_sum -= a
    ans += a * tmp_sum
    
print(ans)