import math
import sys
input = sys.stdin.readline

def isPrimeNumber(num):
  if num == 1 or num == 2 or num == 3:
      return True
  
  if num % 2 == 0:
      return False
  
  for i in range(3, math.ceil(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  
  return True

  
while True:
  num = int(input())
  
  if num == 0:
    break
  
  count = 0
  # num 보다 크고, 2num보다 작거나 같은 수
  for i in range(num + 1, num * 2 + 1):
    if isPrimeNumber(i):
      # print(f'{i}는 소수입니다.')
      count += 1
  print(count)