for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    
    for j in range(2, n):
        ans = max(ans, abs(arr[j] - arr[j-2]))
    
    print(ans)