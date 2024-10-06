N = int(input())
arr = sorted(list(map(int, input().split())))
target = int(input())

left = 0
right = N - 1
answer = 0

while left < right:
    total = arr[left] + arr[right]
    
    if total == target:
        answer += 1
        left += 1
        right -= 1
    elif total > target:
        right -= 1
    else:
        left += 1

print(answer)