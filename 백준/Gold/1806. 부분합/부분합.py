import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

if M == 0:
  print(0)
  
lt = 0
rt = 0
lengthArr = []
total = arr[lt]

while rt < N or lt < rt:
  try:
    if total >= M:
      lengthArr.append(rt - lt + 1)
      total -= arr[lt]
      lt += 1
    else:
      rt += 1
      total += arr[rt]
  except:
    break

if len(lengthArr) > 0:
  print(min(lengthArr))
else:
  print(0)