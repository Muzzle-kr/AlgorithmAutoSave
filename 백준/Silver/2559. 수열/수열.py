N, K = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = K
total = sum(arr[left:right])
result = total

while right < N:
    total -= arr[left]
    total += arr[right]
    
    if total > result:
        result = total
    
    left += 1
    right += 1
    
print(result)