bird = int(input())

scope = pow(10,9)
num = 1
i = 1
while num < scope:
    if i > bird:
        i = 1
        
    bird = bird - i
    
    if bird <= 0:
        break;
    num += 1
    i +=1

print(num)