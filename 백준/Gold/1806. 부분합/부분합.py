# 8 2
# 1 2 3 4 5 6 7 8

# 가장 긴 짝수 연속한 부분의 수열을 구하라
# 총 M개 삭제가 가능하기에 총 길이의 arr 
# 슬라이딩 윈도우로 구하기
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
  # print(f'lt = {lt}, rt = {rt}')
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
  # print(lengthArr)
  print(min(lengthArr))
else:
  print(0)