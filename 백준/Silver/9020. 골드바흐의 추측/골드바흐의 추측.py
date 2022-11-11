import math
import sys
input = sys.stdin.readline
num = 10000
arr = [0 for i in range(10001)]
primeArr = []
for i in range(num):
  arr[i] = i

for i in range(2, num + 1):
  if arr[i] == 0:
    continue
  for j in range(i + i, num + 1, i):
    arr[j] = 0

for i in range(num):
  if arr[i] != 0:
    primeArr.append(arr[i])

for i in range(int(input())):
  result = [-10000, 100000]
  num = int(input())
  
  for j in primeArr:
    if j >= num:
      continue
    for k in primeArr:
      # print(f'num: {num}, j: {j}, k: {k}')
      if k >= num:
        break
      
      if j + k == num:
        if k - j  < result[1] - result[0] and j <= k:
          # print(f'j: {j}, k: {k}, result: {result}')
          result[0] = j
          result[1] = k
  print(result[0], result[1])