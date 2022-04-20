import sys
input = sys.stdin.readline
fixed, variable, price = map(int, input().split())

if variable >= price: 
  print(-1)
else:
  print(fixed // (price - variable) + 1)