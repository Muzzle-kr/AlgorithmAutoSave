def solution(dartResult):
    answer = [0, 0, 0, 0]
    tmp = ""
    idx = 0
    digit = ""
    
    for i in dartResult:
        if i.isdigit():
            digit += i
        elif i == "S" or i == "D" or i == "T":
            idx += 1
            answer[idx] = int(digit)
            digit = ""
            if i == "S":
                continue
            elif i == "D":
                answer[idx] **= 2
            else:
                answer[idx] **= 3
        else:
            if i == "*":
                answer[idx] *= 2
                answer[idx-1] *= 2
            else:       
                answer[idx] *= -1
    return sum(answer[1:])