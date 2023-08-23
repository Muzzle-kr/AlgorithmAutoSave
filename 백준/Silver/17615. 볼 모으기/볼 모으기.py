import sys

N = int(input())
arr = list(map(str, sys.stdin.readline().rstrip()))
red = arr.count('R')
blue = N - red

# 더 적은 개수의 볼이 정답 후보
ans = min(red, blue)
cnt = 0

# 앞에서부터 연속된 불을 계산
for i in range(N):
    if arr[i] != arr[0]: break
    cnt += 1
    
if arr[0] == "R": 
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)
    
cnt = 0
# 뒤에서부터 연속된 불을 계산
for i in range(N-1, -1, -1):
    if arr[i] != arr[N-1]: break
    cnt += 1
    
if arr[N-1] == "R": 
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)

print(ans)