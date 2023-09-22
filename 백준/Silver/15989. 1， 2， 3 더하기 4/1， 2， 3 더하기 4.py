N = int(input())
arr = [0, 1, 2, 3]
for i in range(4, 10001):
        arr.append(1 + (i // 2) + (arr[i-3]))

for _ in range(N):
    cnt = 0
    number = int(input())
    print(arr[number])