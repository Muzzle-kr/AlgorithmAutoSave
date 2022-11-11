import sys
input = sys.stdin.readline


while True:
    stack = []
    sentence = input().rstrip()
    if len(sentence) == 1:
        break
    
    for w in sentence:
        if w == "[" or w == '(':
            stack.append(w)
        elif w == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(w)
                break
        elif w == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(w)
            
    if len(stack) > 0:
        print("no")
    else:
        print("yes")
            
            