def solution(numbers):
    answer = [0] * len(numbers)
    
    indexStack = []
    valueStack = []
    
    for idx, val in enumerate(numbers):
        if idx == 0:
            indexStack.append(idx)
            valueStack.append(val)
        else:
            if val > valueStack[-1]:
                while valueStack and val > valueStack[-1]:
                    answer[indexStack.pop()] = val
                    valueStack.pop()
            indexStack.append(idx)
            valueStack.append(val)
    
    while indexStack:
        answer[indexStack.pop()] = -1

    return answer