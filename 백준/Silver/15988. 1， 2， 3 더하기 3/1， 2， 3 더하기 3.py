arr = [0, 1, 2, 4]

for i in range(4, 1000001):
    arr.append((arr[i-1] + arr[i-2] + arr[i-3]) % 1000000009)


for _ in range(int(input())):
    n = int(input())
    print(arr[n])