from itertools import permutations
def solution(expression):
    answer = 0
    number = []
    symbol = []
    
    
    tmp = ""
    for e in expression:
        if e == "+" or e == "-" or e == "*":
            number.append(int(tmp))
            tmp = ""
            symbol.append(e)
        else:
            tmp += e
    
    setSymbol = set(symbol)
    permutation  = list(permutations(setSymbol, len(setSymbol)))
    number.append(int(tmp))
    
    for p in permutation:
        tmpNumber = number[:]
        tmpSymbol = symbol[:]

        for i in p:
            j = 0
            while j < len(tmpSymbol):
                if tmpSymbol[j] == i:
                    if i == "+":
                        tmpNumber[j] += tmpNumber[j+1]
                    elif i == "-":
                        tmpNumber[j] -= tmpNumber[j+1]
                    else:
                        tmpNumber[j] *= tmpNumber[j+1]
                    tmpNumber.pop(j+1)
                    tmpSymbol.pop(j)
                    j -= 1  
                j += 1
            
        if len(tmpNumber) > 1:
            if tmpSymbol[0] == "+":
                tmpNumber[0] += tmpNumber[1]
            elif tmpSymbol[0] == "-":
                tmpNumber[0] -= tmpNumber[1]
            else:
                tmpNumber[0] *= tmpNumber[1]
        
        # print(f'tmpNumber: {tmpNumber}, tmpSymbol: {tmpSymbol}')
        answer = max(answer, abs(tmpNumber[0]))
    return answer