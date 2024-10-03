rank = 1
while True:
    stack = []
    count = 0
    inputString = input()

    if '-' in inputString:
        break

    for i in inputString:
        if i == "{":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                count+=1
                stack.append('{')
    
    count+= len(stack)//2
        
    print(f'{rank}. {count}')
    rank+=1