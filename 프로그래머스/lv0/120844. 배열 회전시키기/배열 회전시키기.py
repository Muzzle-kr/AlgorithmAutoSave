from collections import deque

def solution(numbers, direction):
    dq = deque(numbers)    
    if direction == "right":
        dq.appendleft(dq.pop())
    else:
        dq.append(dq.popleft())

    return list(dq)
