import math
def convertToBinary(n):
    return bin(n)[2:]
    
def solution(numbers):
    answer = []
    
    
    for n in numbers:
        binary = convertToBinary(n)
        
        count = 0
        for b in range(len(binary)-1, -1, -1):
            if binary[b] == '1':
                count += 1
            else:
                break
        
        val = math.ceil(n + (2**(count-1)))
        answer.append(val)
    return answer