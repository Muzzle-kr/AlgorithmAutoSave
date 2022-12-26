def solution(t, p):
    answer = 0
    length = len(p)
    
    s = ""
    starting = 0
    while starting < len(t):
        count = 0
        
        for idx in range(len(t)):
            s += t[idx + starting]
            count += 1
            
            if count >= length:
                if int(s) <= int(p):
                    answer +=1
                starting += 1
                s = ""
                break
        if starting + length > len(t):
            break
        
    return answer