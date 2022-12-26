import math

def getNumberOfDivisor(n):
        count = 0
        if n <= 2:
            # print(f'n : {n}, 약수의 갯수: {n}')
            return n
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n // i == i:   
                    count += 1
                else:
                    count += 2

        # print(f'n : {n}, 약수의 갯수: {count}')
        return count
def solution(number, limit, power):
    answer = 0
    
    for i in range(number):
        i += 1
        
        eof = getNumberOfDivisor(i)
        # print(f'eof : {eof}')
        if eof > limit:
            answer += power
        else:
            answer += eof
        
    return answer

	