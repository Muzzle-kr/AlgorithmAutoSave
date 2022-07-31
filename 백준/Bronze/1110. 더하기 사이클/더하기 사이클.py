N = int(input())
cycle = 0
result = -1
idx = 0
while N != result:
  if cycle == 0: 
    result = N
  if result < 10:
    result = int(str(result) + str(result))
  else:
    front = str(result)[1]
    middleSum = int(str(result)[0]) + int(str(result)[1])
    back = 0
    
    if middleSum < 10:
      back = middleSum
    else:
      back = int(str(middleSum)[1])    
      
    result = int(str(front) + str(back))
    
  cycle += 1
print(cycle)