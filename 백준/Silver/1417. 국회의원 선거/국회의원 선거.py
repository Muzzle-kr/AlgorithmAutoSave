n = int(input())
arr = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
    exit()

dasom = arr[0]
arr = sorted(arr[1:], reverse=True)
result = 0

while dasom <= arr[0]:
    dasom += 1
    arr[0] -= 1
    arr = sorted(arr, reverse=True)
    result += 1

print(result)