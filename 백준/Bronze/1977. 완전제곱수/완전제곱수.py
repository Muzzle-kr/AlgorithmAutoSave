import math

floor = int(input())
ceiling = int(input())

perfectSquare = []
for i in range(floor, ceiling + 1):
  if math.sqrt(i) % 1 == 0.0:
    perfectSquare.append(i)

if len(perfectSquare) >= 1:
  print(sum(perfectSquare))
  print(perfectSquare[0])  
else:
  print(-1)
