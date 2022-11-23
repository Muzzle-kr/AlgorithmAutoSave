import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

sequence = [0] * (max(arr) + 1)
left = 0
right = 0
result = 0

while right < N:
    if sequence[arr[right]] != M:
        sequence[arr[right]] += 1
        right += 1
    else:
        # result.append(right-left)
        sequence[arr[left]] -= 1
        left += 1
    
    result = max(result, right-left)
print(result)