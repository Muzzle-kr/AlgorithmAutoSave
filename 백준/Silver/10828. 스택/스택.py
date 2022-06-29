import sys

input = sys.stdin.readline
stack = []
repeat = int(input())

for _ in range(repeat):
  order = input().rstrip()
  length = len(stack)
  
  # print("order === %s typeof ==== %s" % (order, type(order)))
  if order.find('push') != -1:
    list = order.split(" ")
    num = list[1]    
    stack.append(num)

  elif order == 'pop':
    if length > 0:
      print(stack.pop())
    else: 
      print(-1)
      
  elif order == 'size':
    print(length)

  elif order == 'empty':
    if length == 0:
      print(1)
    else:
      print(0)
    
  elif order == 'top':
    if length > 0:
      print(stack[length-1])
    else:
      print(-1)