N = int(input())
nums = list(map(int, input().split()))
idx = [-1] * (N+1)

for i, v in enumerate(nums):
    idx[v] = i
    
longest = 0
cnt = 1

for num in range(1, N):
    if idx[num] < idx[num+1]: # 번호 i가 nums 배열 내에서 번호 i+1보다 앞에 존재한다면
        cnt += 1 # 오름차순 길이 증가
    else:
        longest = max(longest, cnt)
        cnt = 1
# 번호 배열의 전체 길이에서 1씩 차이나는 가장 긴 오름차순의 길이를 뺀다.
print(N - longest if N != 1 else 0)