import math

arr = []
for _ in range(5):
    num = int(input())
    arr.append(num)

arr.sort()
print(int(sum(arr)/len(arr)))
print(arr[2])