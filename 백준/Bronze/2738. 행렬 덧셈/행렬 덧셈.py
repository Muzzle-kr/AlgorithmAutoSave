import math
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
matrix = [[0 for j in range(b)] for i in range(a)]
for n in range(2):
  
  for i in range(a):
    values = list(map(int, input().split()))
    for j in range(b):
      if n == 0:
        matrix[i][j] = values[j]
      else:
        matrix[i][j] = matrix[i][j] + values[j]
      

for i in range(a):
  print(*matrix[i])
