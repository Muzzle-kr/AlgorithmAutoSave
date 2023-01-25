def solution(N, number):
    arr = [[]] + [[int(str(N) * i)] for i in range(1, 9)]
    
    if [number] in arr:
        return arr.index([number])
    
    # 1번으로 나올 수 있는 것은 5뿐이므로 2부터 시작
    for i in range(2, 9):
        for j in range(1, i):
            for a in arr[j]:
                for b in arr[i-j]:
                    arr[i].append(a + b)
                    arr[i].append(a * b)
                    arr[i].append(a - b)
                    if b != 0:
                        arr[i].append(a // b)
        if number in arr[i]:
            return i
        arr[i] = list(set(arr[i]))

    return -1    