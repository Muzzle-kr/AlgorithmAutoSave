N = int(input())

cnt = 0
for i in range(1, N):
    for j in range(i, N):
        c = N - (i + j)
        
        if c < j:
            break
        
        if c < i + j:
            cnt += 1
print(cnt)