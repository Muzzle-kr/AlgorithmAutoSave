from collections import deque


def solution(s):
    dq = deque(list(s))
    length = len(s)
    answer = 0
    
    # 홀수면 올바른 괄호를 만들 수 없음
    if length % 2 == 1:
        return 0
    
    
    for i in range(length):
        stack = []
        
        dq.append(dq.popleft())
        
        for i in dq:
            if len(stack) == 0:
                stack.append(i)
                continue
            
            if i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
        
        if len(stack) == 0:
            answer += 1

    return answer