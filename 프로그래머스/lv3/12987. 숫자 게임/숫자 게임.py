def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    for i in A:
        for j in B:
            if i < j:
                answer += 1
                B.remove(j)
                break            
    return answer