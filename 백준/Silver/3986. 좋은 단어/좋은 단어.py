n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    stack = []
    
    for i in range(len(word)):
        if not stack:
            stack.append(word[i])
        else:
            if stack[-1] == word[i]:
                stack.pop()
            else:
                stack.append(word[i])
    
    if not stack:
        cnt += 1
        
print(cnt)