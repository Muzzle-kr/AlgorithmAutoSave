result = []
for _ in range(2):
    arr = []
    for _ in range(10):
        arr.append(int(input()))
    
    arr.sort()
    result.append(sum(arr[7:]))

print(*result)