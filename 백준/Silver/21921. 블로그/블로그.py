import sys

# 입력을 받는 부분은 그대로 유지
N, X = map(int, input().split())
arr = list(map(int, input().split()))

result = -1  # 결과값 초기화
count = 0  # 최대값을 갖는 섹션의 개수 초기화
total = sum(arr[:X])  # 초기 total 값 계산

if total > result:
    result = total
    count = 1

for i in range(1, N - X + 1):
    total = total - arr[i - 1] + arr[i + X - 1]
    
    if total > result:
        result = total
        count = 1
    elif total == result:
        count += 1

if result <= 0:
    print("SAD")
else:
    print(result)
    print(count)
