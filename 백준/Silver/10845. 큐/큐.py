import sys
from collections import deque

input = sys.stdin.readline
dq = deque([])
repeat = int(input())

for _ in range(repeat):
  order = input().rstrip()
  length = len(dq)
  
  if order.find('push') != -1:
    list = order.split(" ")
    num = list[1]    
    dq.append(num)

  elif order == 'pop':
    if length > 0:
      print(dq.popleft())
    else: 
      print(-1)
      
  elif order == 'size':
    print(length)

  elif order == 'empty':
    if length == 0:
      print(1)
    else:
      print(0)
    
  elif order == 'front':
    if length > 0:
      print(dq[0])
    else:
      print(-1)
  
  elif order == 'back':
    if length > 0:
      print(dq[length-1])
    else:
      print(-1)