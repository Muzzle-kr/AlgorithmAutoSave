N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1
for i in arr:
    for j in i:
        print(j, end = " ")
    print()