from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
q = deque([])

for _ in range(N):
    order = input().rstrip()
    if "push" in order:
        num = order.split(" ")[1]
        q.append(num)
    elif order == "front":
        try:
            print(q[0])
        except:
            print(-1)
    elif order == "back":
        try:
            print(q[-1])
        except:
            print(-1)
    elif order == "size":
        try:
            print(len(q))
        except:
            print(-1)
    elif order == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order == "pop":
        try:
            print(q.popleft())
        except:
            print(-1)