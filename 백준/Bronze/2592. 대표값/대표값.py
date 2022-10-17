import math

arr = []
mode = [0 for i in range(1000)]


for _ in range(10):
    num = int(input())
    arr.append(num)
    mode[num-1] = mode[num-1] + 1
    
print(int(sum(arr) / len(arr)))
print(mode.index(max(mode)) +1)