def solution(topping):
    answer = 0
    topping1 = [0] * len(topping)
    topping2 = [0] * len(topping)
    
    tmp2 = []
    for i in range(len(topping) - 1, -1, -1):
        if not tmp2:
            tmp2.append(topping[i])
            topping2[i] += 1
        else:
            if topping[i] not in tmp2:
                tmp2.append(topping[i])
                topping2[i] = topping2[i + 1] + 1
            else:
                topping2[i] = topping2[i + 1]
    
    tmp = []      
    for i in range(len(topping)):
        if not tmp:
            tmp.append(topping[i])
            topping1[i] += 1
        else:
            if topping[i] not in tmp:
                tmp.append(topping[i])
                topping1[i] = topping1[i-1] + 1
            else:
                topping1[i] = topping1[i-1]
                
    
    for i in range(len(topping)-1):
        if topping1[i] == topping2[i+1]:
            answer += 1
    return answer