def solution(my_str, n):
    answer = []
    currentLength = 0
    tmp = ""
    for s in my_str:
        if currentLength == n:
            answer.append(tmp)
            tmp = s
            currentLength = 1
        else:
            tmp += s
            currentLength += 1
    
    if tmp != "":
        answer.append(tmp)
    return answer