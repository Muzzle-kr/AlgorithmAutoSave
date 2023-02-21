def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(arrayA, arrayB):
    answer = 0
    
    tmp = []
    for a in arrayA:
        if not tmp:
            tmp.append(a)
            continue
        else:
            gcdd = gcd(tmp[-1], a)
            tmp.append(gcdd)
            
    tmp2 = []

    for b in arrayB:
        if not tmp2:
            tmp2.append(b)
            continue
        else:
            gcdd = gcd(tmp2[-1], b)
            tmp2.append(gcdd)

    gcd1 = tmp[-1]
    gcd2 = tmp2[-1]

    
    # print(gcd1, gcd2)
    for i in range(len(arrayA)):
        if gcd2 != 1 and arrayA[i] % gcd2 == 0:
            gcd2 = 0
            return 0
        
        if gcd1 != 1 and arrayB[i] % gcd1 == 0:
            gcd1 = 0
            return 0
        
    return max(gcd1, gcd2)