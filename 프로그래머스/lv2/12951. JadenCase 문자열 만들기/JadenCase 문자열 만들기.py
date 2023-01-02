def solution(s):
    answer = list(s)
    lastChar = ""
    for i in range(len(s)): 
        # print(f'lastChar: {lastChar}, answer[i] = {answer[i]}')
        if lastChar == "" or lastChar == " ":
            answer[i] = answer[i].upper()
        else:
            answer[i] = answer[i].lower()
        lastChar = answer[i]
    return "".join(answer)