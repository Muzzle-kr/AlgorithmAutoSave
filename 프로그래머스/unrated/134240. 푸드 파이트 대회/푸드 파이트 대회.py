import math
def solution(food):
    
    answer = ""
    opposite = ""
    for idx, f in enumerate(food):
        
        if idx == 0:
            continue
        
        placeFood = str(idx) * (math.floor(f/2))
        answer += placeFood
        opposite = placeFood + opposite
        
    answer = answer + "0" + opposite
    return answer