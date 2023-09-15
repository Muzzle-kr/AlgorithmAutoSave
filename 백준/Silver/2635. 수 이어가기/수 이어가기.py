N = int(input())

ans = 0
ans_arr = []
for i in range(1, N+1):
    arr = [N, i]

    while arr[-2] - arr[-1] >= 0:
        arr.append(arr[-2] - arr[-1])
        
    if ans < len(arr):
        ans = len(arr)
        ans_arr = arr
    
print(ans)
print(*ans_arr)