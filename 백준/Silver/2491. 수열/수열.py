n = int(input())
arr = list(map(int, input().split()))
last_value = 0
result = 0

long_cnt = 0
short_cnt = 0
for i in range(n):
    if arr[i] > last_value:
        long_cnt += 1
        short_cnt = 1
        last_value = arr[i]
    elif arr[i] < last_value:
        short_cnt += 1
        long_cnt = 1
        last_value = arr[i]
    else:
        long_cnt += 1
        short_cnt += 1
        last_value = arr[i]
        
    result = max(result, long_cnt, short_cnt)

print(result)