N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if arr[i] < arr[i-1]:
        x, y = i-1, i
        
        for j in range(N-1, 0, -1):
            if arr[j] < arr[x]:
                arr[j], arr[x] = arr[x], arr[j]
                a = arr[:i] + sorted(arr[i:], reverse=True)
                print(*a)
                exit()
print(-1)