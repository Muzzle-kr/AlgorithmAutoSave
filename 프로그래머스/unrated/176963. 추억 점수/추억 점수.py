def solution(name, yearning, photo):
    answer = []
    nameToYearning = {}
    
    for idx, n in enumerate(name):
        nameToYearning[n] = yearning[idx]
    
    answer = []
    for p in photo:
        total = 0
        
        for eachPhoto in p:
            if eachPhoto in nameToYearning:
                total += nameToYearning[eachPhoto]
        answer.append(total)
        
    
    return answer