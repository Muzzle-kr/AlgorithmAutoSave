N = int(input())

result = []
for _ in range(N):
  li = list(input().split())
  calculation = 0
  for i, value in enumerate(li):
    i = float(i)
    if i == 0:
      calculation = float(value)
    elif value == '@':
      calculation *= 3
    elif value == '%':
      calculation += 5
    elif value == '#':
      calculation -= 7
  result.append(format(calculation, ".2f"))

print(*result, end="\n")