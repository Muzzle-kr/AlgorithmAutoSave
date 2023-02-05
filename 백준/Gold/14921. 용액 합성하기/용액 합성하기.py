n = int(input())

arr = list(map(int, input().split()))
minSum = int(1e9)

if n == 2:
    print(sum(arr))
    
else:
    
    
    lt = 0
    rt = n - 1
    
    while lt < rt:
        sum = arr[lt] + arr[rt]
        
        if sum > 0:
            rt -= 1
        else:
            lt += 1
        
        if abs(minSum) > abs(sum):
            minSum = sum
    
    print(minSum)