def solution(ingredient):
    answer = 0
    stack = []

    for i in ingredient:
        stack.append(i)
        
        if len(stack) > 3:
            if stack[-4::] == [1, 2, 3, 1]:
                # print("작업전 ", stack)
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                # print("작업 후 ", stack)
                answer += 1
    return answer