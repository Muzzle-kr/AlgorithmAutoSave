def solution(n):
    answer = 0
    divide = 1234567
    memo = [0, 1]
    
    for i in range(2, 100001):
        sum = memo[i-2] + memo[i-1]
        memo.append(sum)
    
    answer = memo[n] % 1234567
    return answer