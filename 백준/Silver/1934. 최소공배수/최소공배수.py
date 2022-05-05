import sys

input = sys.stdin.readline

def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

N = int(input())
resultArr = []
for _ in range(N):
  a, b = map(int, input().split())
  resultOfGcd = gcd(a, b)
  result = int(a * b / resultOfGcd)
  resultArr.append(result)

for i in range(len(resultArr)):
  print(resultArr[i])