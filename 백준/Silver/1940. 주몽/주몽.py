N = int(input())
M = int(input())

sorted_arr = sorted(list(map(int, input().split())))

left = 0
right = N - 1
cnt = 0    

while left < right:
    if sorted_arr[left] + sorted_arr[right] > M:
        right -= 1
    elif sorted_arr[left] + sorted_arr[right] < M:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1
print(cnt)