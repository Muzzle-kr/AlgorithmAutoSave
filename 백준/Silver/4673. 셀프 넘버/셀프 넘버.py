import math

result = []
for i in range(1, 10000):
  total = i
  for j in range(len(str(i))):
    total += int(str(i)[j])
  result.append(total)


for i in range(1, 10000):
    try:
      if result.index(i):
        continue
    except:
      print(i)