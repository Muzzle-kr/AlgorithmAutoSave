n = int(input())

arr = list(map(int, input().split()))
minSum = int(1e10)
result = []
if n == 2:
    print(*sorted(arr))
    
else:
    lt = 0
    rt = n - 1
    
    while lt < rt:
        sum = arr[lt] + arr[rt]
                
        if abs(minSum) > abs(sum):
            minSum = sum
            result = [arr[lt], arr[rt]]
            
        if sum > 0:
            rt -= 1
        else:
            lt += 1
    
    print(*sorted(result))