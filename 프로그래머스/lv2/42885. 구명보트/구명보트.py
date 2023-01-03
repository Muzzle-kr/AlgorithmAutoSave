from collections import deque


def solution(people, limit):    
    sortedArray = sorted(people, reverse=True)
    dq = deque(sortedArray)
    count = 0
    while len(dq) > 0:
        weight = 0
        if len(dq) == 1:
            dq.pop()
            count += 1
            break
        
        weight = dq[0] + dq[-1]
        if weight <= limit:
            dq.pop()
            dq.popleft()
        else:
            dq.popleft()
        count += 1
    return count