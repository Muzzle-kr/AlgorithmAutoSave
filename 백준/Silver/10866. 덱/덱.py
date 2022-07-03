from collections import deque
import sys

deq = deque([])
repeat = int(input())

for _ in range(repeat):
  input = sys.stdin.readline().rstrip()
  order = input
  length = len(deq)
  if order == "size":
    print(length)
  elif order == "empty":
    if length > 0:
      print(0)
    else:
      print(1)
  elif order == "front":
    if length > 0:
      print(deq[0])
    else: 
      print(-1)
  elif order == "back":
    if length > 0:
      print(deq[-1])
    else: 
      print(-1)
  elif order.find("push_") > -1:
    order1, dir = order.split("_")
    direction, number = dir.split(" ")
    if order1 == "push":
      if direction == "front":
        deq.appendleft(number)
      else: 
        deq.append(number)
  elif order.find("pop_") > -1:
    order1, direction = order.split("_")
    if order1 == "pop":
      if direction == "front":
        if length > 0:
          print(deq.popleft())
        else:
            print(-1)
      else:
        if length > 0:
          print(deq.pop())
        else:
            print(-1)
