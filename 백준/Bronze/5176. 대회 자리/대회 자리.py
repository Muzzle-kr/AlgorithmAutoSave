for _ in range(int(input())):
    P, M = map(int, input().split())
    arr = [0] * (M+1)
    result = 0
    
    for _ in range(P):
        n = int(input())
        if arr[n] == 0:
            arr[n] = 1
        else:
            result += 1
    print(result)