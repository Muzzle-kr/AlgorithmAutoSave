from itertools import combinations
N = int(input())

arr = []

max_num = -1

for i in range(N):
    arr.append(int(input()))
    
arr.sort(reverse=True)

for i in range(len(arr) - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        max_num = arr[i] + arr[i + 1] + arr[i + 2]
        break

print(max_num)