for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())))[1:-1]
    if arr[2] - arr[0] > 3:
        print("KIN")
    else:
        print(sum(arr))