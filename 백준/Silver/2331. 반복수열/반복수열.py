def resSquareNum(num, p):
    sum = 0
    
    for i in str(num):
        sum += int(i) ** p
    return sum


num, p = map(int, input().split())
answer = [num]
lastIndex = 0

while True:
    
    newSquareNum = resSquareNum(answer[-1], p)    
    
    if newSquareNum in answer:
        lastIndex = answer.index(newSquareNum)
        break
    
    answer.append(newSquareNum)

answer = answer[:lastIndex]
print(len(answer))