repeat = int(input())

for i in range(1, repeat+1):
  print(" " * (repeat - i) + "*" * i)
  
  if i == repeat:
    for j in range(repeat-1, 0, -1):
      print(" " * (repeat - j) + "*" * j)
