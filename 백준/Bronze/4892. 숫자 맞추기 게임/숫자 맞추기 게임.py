# n1 = 3*n0
# n1이 짝수면 n2 = n1/2, 홀수면 (n1 + 1) / 2
# n3 = 3 * n2
# n4 = n3 / 9 (몫)
# n1 이 짝수였다면 n0 = 2*n4, 홀수였다면 n0 = 2*n4 + 1
import math
count = 1

while(True):
    num = int(input())
    oddOrEven = ""
    result = 0
    
    if num == 0:
        break
    else:
        num1 = num * 3
        if num % 2 == 0:
            oddOrEven = "even"
        else:
            oddOrEven = "odd"
        
    if oddOrEven == "even":
        result = math.ceil((num -1) / 2)
    else: 
        result = math.floor((num) / 2)
    
    print(f'{count}. {oddOrEven} {result}')
    count += 1