from collections import Counter

def solution(topping):
    answer = 0
    youngerBrother = set()
    bigBrother = Counter(topping)
    
    
    while topping:
        t = topping.pop()
        bigBrother[t] -= 1
        
        if bigBrother[t] == 0:
            del bigBrother[t]
            
        youngerBrother.add(t)
        
        if len(bigBrother) == len(youngerBrother):
            answer += 1
    
    return answer