import sys
input = sys.stdin.readline
from collections import deque

L = int(input())
ML, MK = map(int, input().split())
C = int(input())
Z = [int(input()) for _ in range(L)]

dq = deque()
cnt = 0
answer = True

for i in range(min(ML, L)):
    if cnt == 0:
        if Z[i] - MK * (i + 1) <= 0:
            dq.append(0)
        else:
            dq.append((Z[i] - MK * (i + 1)))
            cnt += 1
    else:
        if Z[i] - MK * (i + 1 - cnt) <= 0:
            dq.append(0)
        else:
            dq.append((Z[i] - MK * (i + 1 - cnt)))
            cnt += 1

for i in range(ML, L):
    if dq[0] == 0:
        dq.popleft()
        
        if Z[i] - MK * (ML - cnt) <= 0:
            dq.append(0)
        else:
            dq.append((Z[i] - MK * (ML - cnt)))
            cnt += 1
            
    else:
        dq.popleft()
        
        if C > 0:
            C -= 1
        else:
            answer = False
            break
    
        
        if Z[i] - MK * (ML - cnt) <= 0:
            dq.append(0)
            cnt -= 1
        else:
            dq.append((Z[i] - MK * (ML - cnt)))

if answer:
    while dq:
        if dq[0] == 0:
            dq.popleft()
        else:
            dq.popleft()
            cnt -= 1
            
            if C > 0:
                C -= 1
            else:
                answer = False
                break
            

if answer:
    print("YES")
else:
    print("NO")