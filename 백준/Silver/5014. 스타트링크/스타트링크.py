import sys
from collections import deque
input = sys.stdin.readline

F, G, S, U, D  = map(int, input().split())
q = deque()
q.append(G)
num = [0] * 1000002
chk = [0] * 1000002
chk[G] = 1
isFind = False

while q:
    a = q.popleft()
    
    if a == S:
        isFind = True
        print(num[a])
        break
    
    if a - D >= 1 and chk[a - D] == 0:
        q.append(a - D)
        num[a - D] = num[a] + 1
        chk[a-D] = 1
        
    if a + U <= F and chk[a + U] == 0:
        q.append(a + U)
        num[a + U] = num[a] + 1
        chk[a+U] = 1
if not isFind:
    print("use the stairs")