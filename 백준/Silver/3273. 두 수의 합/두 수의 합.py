n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
count = 0

lt = 0
rt = len(arr) - 1


while lt < rt:
    total = arr[lt] + arr[rt]
    # print(f'arr: {arr}, lt: {lt}, rt: {rt}, total: {total}')
    if total == x:
        count += 1
        lt += 1
        continue
    
    if total > x:
        rt -= 1 
    else:
        lt += 1

print(count)