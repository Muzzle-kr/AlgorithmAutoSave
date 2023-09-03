'''
이진탐색으로, 시간복잡도는 O(NlogN)
'''
N, K = map(int, input().split())
makgeolli = []

if N == 0 or K == 0:
    print(0)
    exit()
    
for _ in range(N):
    makgeolli.append(int(input()))
    
makgeolli.sort()

left = 0
right = makgeolli[-1]
result = 1

while left <= right:
    mid = (left + right) // 2
    total = 0
    
    if mid == 0:
        break
    
    for mak in makgeolli:
        total += mak // mid

    if total >= K:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)