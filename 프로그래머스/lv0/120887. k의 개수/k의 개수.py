def solution(i, j, k):
    answer = 0
    
    for s in range(i, j + 1):
        s = str(s)
        if len(s) > 1:
            for each in s:
                if each == str(k):
                    answer += 1
        else:
            if s == str(k):
                answer += 1
    return answer