for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    result = 0
    
    for i in range(1, n):
        result += arr[i]-arr[i-1]
        
    print(result*2)
        
        
    