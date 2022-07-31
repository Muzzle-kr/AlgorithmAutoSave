from itertools import combinations
import sys

input = sys.stdin.readline

#  N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N, d, k, c = map(int, input().split())

arr = []
for i in range(N):
  arr.append(int(input()))

for i in range(k-1):
  arr.append(arr[i])
# lt, rt 초기 세팅 차이가 3이면 length 4  
lt = 0
rt = k-1
lengthArr = []

while lt < N:
  length = len(set(arr[lt:rt + 1] + [c]))
  lengthArr.append(length)
  rt += 1
  lt += 1

print(max(lengthArr))