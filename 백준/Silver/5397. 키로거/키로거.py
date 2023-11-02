for _ in range(int(input())):
    word = input()
    stack1 = list()
    stack2 = list()
    
    for w in word:
        if w == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif w == '>':
            if stack2:
                stack1.append(stack2.pop())
        elif w == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(w)
    stack1.extend(reversed(stack2))
    print("".join(stack1))