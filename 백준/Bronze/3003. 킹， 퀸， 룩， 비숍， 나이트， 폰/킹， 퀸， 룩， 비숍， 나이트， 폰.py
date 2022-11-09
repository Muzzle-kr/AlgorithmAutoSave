arr = [1, 1, 2, 2, 2, 8]

arr2 = list(map(int, input().split()));

for idx, n in enumerate(arr):
    if idx != len(arr) - 1:
        print(n - arr2[idx], end=" ")
    else:
        print(n - arr2[idx])