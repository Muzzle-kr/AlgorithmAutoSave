from collections import deque

def solution(A, B):
    answer = 0
    isFind = 0
    dq = deque(A)

    if A == B:
        return 0
    
    for _ in range(len(A) - 1):
        dq.appendleft(dq.pop())
        answer += 1
        if "".join(dq) == B:
            isFind = 1
            break
    
    if isFind:
        return answer
    else:
        return -1