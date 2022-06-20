repeat = int(input())

for i in range(repeat):
    num = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))