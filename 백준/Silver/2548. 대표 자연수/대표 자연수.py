'''
6
4 3 2 2 9 10
'''

N = int(input())
sorted_arr = sorted(list(map(int, input().split())))

mid = N // 2
minimum_total = int(1e9)
answer = 0
for i in range(mid, -1, -1):
    mid_num = sorted_arr[i]
    total = 0
    
    for n in sorted_arr:
        abs_num = abs(mid_num - n)
        total += abs_num
    
    if total <= minimum_total:
        minimum_total = total
        answer = mid_num
    else:
        break
print(answer)
    