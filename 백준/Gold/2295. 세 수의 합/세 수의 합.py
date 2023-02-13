def func():
    N = int(input())

    arr = []

    for _ in range(N):
        arr.append(int(input()))
    arr.sort()    
    
    # set을 해야 sum_arr의 length가 줄어들어 시간복잡도가 줄어든다.
    sum_arr = set()
    
    for i in range(N):
        for j in range(i, N):
            sum_arr.add(arr[i] + arr[j])
    
    result = []
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            
            if arr[i] - arr[j] in sum_arr:
                return arr[i]
print(func())