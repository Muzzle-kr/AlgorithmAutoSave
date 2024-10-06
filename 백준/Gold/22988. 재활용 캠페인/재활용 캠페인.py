N, K = map(int, input().split())
perfumes = list(map(int, input().split()))
perfumes.sort()
answer = 0

# 이미 K 이상인 향수는 따로 처리
for i in range(N-1, -1, -1):
    if perfumes[i] >= K:
        answer += 1
    else:
        break
    
left = 0
right = N - 1 - answer
rest_count = N - answer

while left < right:
    total = perfumes[left] + perfumes[right]
    
    # 절반 용량보다 많다면 반납한다.
    if total >= K / 2:
        answer += 1
        rest_count -= 2
        left += 1
        right -= 1
    # 절반 용량보다 적다면 더 큰 용량을 찾고, 작은 용량은 나머지로 넣는다.
    else:
        left += 1

answer += rest_count // 3
print(answer)