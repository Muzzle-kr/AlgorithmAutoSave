def solution(survey, choices):
    score = {
        "R":0, 
        "T":0, 
        "C":0, 
        "F":0, 
        "J":0, 
        "M":0,
        "A":0,
        "N":0
    } 
    
    negativeScore = [3, 2, 1]
    positiveScore = [1, 2, 3]
    order = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    answer = ''
    
    for idx, i in enumerate(survey):
        if choices[idx] != 4:
            if choices[idx] < 4:
                score[i[0]] += negativeScore[choices[idx]-1]
            else:
                score[i[1]] += positiveScore[choices[idx]-5]
    
    for i in order:
        if score[i[0]] >= score[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    
    return answer