import math

def convertToN(n, k):
    sum = ""
    
    while n > 0:
        n, mod = divmod(n, k)
        sum += str(mod)
    return sum[::-1]
        
def checkPrimeNumber(n):
    n = int(n)
    
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    converted = ""
    
    if k != 10: 
        converted = convertToN(n, k)    
    else:
        converted = str(n)
        
    chr = ""
    # 마지막 계산을 위한 보정
    converted = converted + "0"
    
    for i in range(len(converted)):
        if converted[i] != "0":
            chr += converted[i]
        else:
            if chr != "":
                if checkPrimeNumber(chr):
                    answer += 1
                chr = ""
    return answer