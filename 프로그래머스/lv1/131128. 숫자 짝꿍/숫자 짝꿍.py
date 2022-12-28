def solution(X, Y):
    answer = ""
    n1 = [0] * 10
    n2 = [0] * 10
    
    for i in X:
        n1[int(i)] += 1
    for i in Y:
        n2[int(i)] += 1
        
    for i in range(9, -1, -1):
        n = n1[i] if n1[i] < n2[i] else n2[i]
        
        if n != 0:
            answer += str(i) * n
    
    if len(answer) == 0:
        return "-1"
    elif len(answer) == answer.count("0"):
        return "0"
    else:
        return answer