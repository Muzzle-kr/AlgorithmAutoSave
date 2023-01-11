def solution(n, left, right):
    answer = []
    
    for i in range(left + 1, right + 2):
        
        if i % n == 0:
            answer.append(n)
            continue
        if i % n <= i // n:
            answer.append((i // n) + 1)
            continue
        answer.append((i % n))
        

    return answer