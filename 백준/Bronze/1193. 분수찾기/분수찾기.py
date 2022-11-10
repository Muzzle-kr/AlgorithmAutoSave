numerator = 1 # 분자
denominator = 1 # 분모
count = 1
N = int(input())

def printResult(a, b):
  print(str(a) + '/' + str(b))
  
  
if N == 1:
    print('1/1');
    exit()

if N == 2:
    print('1/2');
    exit()
    
while (count < N):

    
    if denominator == numerator:
      denominator += 1
      count += 1
      continue
    
    # 분자가 더 클 때 (왼쪽 끝)
    if denominator < numerator:
        # print(f"분자가 더 클 때 (왼쪽 끝) {numerator}/{denominator}")
        originalNumerator = numerator
        while (originalNumerator != denominator):
            denominator += 1
            numerator -= 1
            count += 1
            # print(f"작업 후 count: {count} 값: {numerator}/{denominator}")
            
            if count == N:
              printResult(numerator, denominator)
              exit()
        
        denominator += 1
        count += 1      
        
        if count == N:
          printResult(numerator, denominator)
          exit()
      
        continue
    # 분모가 더 클 때 (위쪽 끝)
    else:
        # print(f"분모가 더 클 때, {numerator}/{denominator}")
        originalDenominator = denominator
        while (originalDenominator != numerator):
            denominator -= 1
            numerator += 1
            count += 1
            # print(f"작업 후 count: {count} 값: {numerator}/{denominator}")
            
            if count == N:
              printResult(numerator, denominator);
              exit()
        
        numerator += 1
        count += 1        
        
        if count == N:
          printResult(numerator, denominator)
          exit()
        continue

