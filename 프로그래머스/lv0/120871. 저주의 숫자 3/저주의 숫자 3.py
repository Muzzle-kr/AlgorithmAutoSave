import math

def solution(n):
    previous = 0
    arr = [0]
    
    for _ in range(1, 200):
        if previous < 10:
            if previous == 3:
                previous += 1
                continue
            elif previous % 3 == 0:
                previous += 1
                continue
            else:
                arr.append(previous)
                previous += 1   
                continue
        else:
            if previous % 3 == 0:
                previous += 1
                continue
            
            isCatch = False
            for i in str(previous):
                if i == "3":
                    previous += 1
                    isCatch = True
                    break
                
            if isCatch:
                continue
            else:
                arr.append(previous)
                previous += 1
    return arr[n]