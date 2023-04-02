arr = []
maxLength = 0

for _ in range(5):
    tmp = list(input().strip())
    maxLength = max(maxLength, len(tmp))
    arr.append(tmp)

idx = 0
result = ""
while idx < maxLength:
    
    for j in range(5):
        if len(arr[j]) > idx:
            result += arr[j][idx]

    idx += 1

print(result)