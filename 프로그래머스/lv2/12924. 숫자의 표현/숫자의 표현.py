def solution(n):
    answer = 0
    result = []    
    for i in range(1, n // 2 + 1):
        sum = 0
        tmp = []
        while True: 
            sum += i
            if sum > n:
                break
            elif sum == n:
                tmp.append(i)
                result.append(tmp)
                answer += 1
                break
            tmp.append(i)
            i += 1
    answer += 1
    return answer