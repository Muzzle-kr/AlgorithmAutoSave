H, W = map(int, input().split())
blocks = list(map(int, input().split()))
ans = 0

for i in range(1, W-1):
    left = max(blocks[:i])
    right = max(blocks[i+1:])
    
    min_height = min(left, right)
    
    if min_height > blocks[i]:
        ans += min_height - blocks[i]
print(ans)