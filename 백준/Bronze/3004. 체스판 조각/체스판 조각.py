import math
N = int(input())

result = [1, 2, 4, 6, 8, 12, 16,]
preValue = 4

for i in range(9, 120):
  if i % 2 == 1:
      result.append(result[-1] + preValue)
      preValue += 1
  else:
      result.append(result[-1] + preValue)

print(result[N])  