import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, targetIdx = map(int, input().split())
    q = list(map(int, input().split()))
    idxQueue = list(range(len(q)))
    idxQueue[targetIdx] = "요놈이다"
    answer = 0
    
    while True:
        maxValue = max(q)
        
        if q[0] == maxValue:
            if idxQueue[0] == "요놈이다":
                answer += 1
                break
            else:
                q.pop(0)
                idxQueue.pop(0)
                answer += 1
        else:
            q.append(q.pop(0))
            idxQueue.append(idxQueue.pop(0))    
            
            
        
    print(answer)