def solution(n):
    
    arr = [0] * (n + 5)
    answer = 0
    for i in range(1, n + 1):
        for j in range(i * i, n + 1, i):
            arr[j] += 1
    
    for i in range(2, n + 1):
        if arr[i] == 1:
            answer += 1
    return answer