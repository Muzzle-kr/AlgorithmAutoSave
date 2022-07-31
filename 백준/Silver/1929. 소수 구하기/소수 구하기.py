import math
a, b = map(int, input().split())

def checkPrime(a):
    if a == 1: 
        return False
    if a <= 3:
        return True
    squareRoot = int(math.sqrt(a))
    for i in range(2, squareRoot + 1):
        if a%  i == 0:
            return False
    return True
    
for i in range(a, b + 1):
    if checkPrime(i):
        print(i)
        

