def convertToBinary(n):
    string = ""
    
    while n > 1:
        string = str(n % 2) + string
        n = n // 2
    
    string = str(n) + string
    return string
    
def findNumberOfOne(binary):
    count = 0
    for i in binary:
        if i == "1":
            count += 1
            
    return count
    
def solution(n):
    answer = 0
    count = findNumberOfOne(convertToBinary(n))
    
    while True:
        n += 1
        if findNumberOfOne(convertToBinary(n)) == count:
            answer = n
            break
    return answer