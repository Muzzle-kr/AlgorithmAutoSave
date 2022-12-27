def solution(polynomial):
    s = list(polynomial.split(" "))
    answer = ''
    sum = 0
    sumOfNum = 0
    lastSymbol = ""
    for idx, i in enumerate(s):
        if "x" in i:
            if len(i) > 1:
                sum += int(i[0:-1])
            else:
                sum += 1
        elif i == "+":
            continue
        else:
            sumOfNum += int(i)
    

        # print(f'현재 sum == {sum}')
    if sumOfNum > 0:
        if sum == 1:
            answer = "x + " + str(sumOfNum)
        elif sum == 0:
            answer = str(sumOfNum)
        else:
            answer = str(sum) + "x + " + str(sumOfNum)
    else:
        if sum == 1:
            answer = "x"
        elif sum == 0:
            answer = ""
        else:    
            answer = str(sum) + "x"
    return answer