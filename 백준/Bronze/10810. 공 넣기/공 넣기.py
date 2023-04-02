n, m = map(int, input().split())
arr = [0 for _ in range(n)]

for _ in range(m):
    i, j, ball = map(int, input().split())
    
    for k in range(i-1, j):
        arr[k] = ball
        
print(*arr)