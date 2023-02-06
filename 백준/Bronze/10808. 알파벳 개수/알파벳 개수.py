arr = [0] * 26


for i in input().rstrip():
    
    arr[ord(i) - 97] += 1

print(*arr)