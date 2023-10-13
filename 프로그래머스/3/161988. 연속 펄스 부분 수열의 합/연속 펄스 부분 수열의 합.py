def solution(sequence):
    answer = 0
    # -1, 1 순서
    
    isPlus = True
    sequence1 = 0
    sequence2 = 0
    
    for s in sequence:
        if isPlus:
            sequence1 += s
            sequence2 -= s
        else:
            sequence1 -= s
            sequence2 += s
        
        if sequence1 < 0:
            sequence1 = 0
        
        if sequence2 < 0:
            sequence2 = 0
        
        if sequence1 > answer:
            answer = sequence1
            
        if sequence2 > answer:
            answer = sequence2
            
        isPlus = not isPlus
    return answer