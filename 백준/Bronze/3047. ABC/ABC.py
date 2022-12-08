arr = []


arr = list(map(int, input().split()))
arr.sort()
    
result = []

for i in input():
    if i == "C":
        result.append(arr[2])
    elif i == "B":
        result.append(arr[1])
    else:
        result.append(arr[0])
        
print(*result)
    