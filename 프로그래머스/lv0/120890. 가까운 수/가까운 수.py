def solution(array, n):
    answer = 0
    diff = 9999999
    array.sort()
    
    for i in array:
        if max(n, i) - min(n, i) < diff:
            answer = i
            diff = max(n, i) - min(n, i)
    return answer
