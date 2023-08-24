N = int(input())
student_order = list(map(int, input().split()))
ans = [0] * (N)

for i in range(N):
    height = i + 1
    
    if i == 0:
        ans[student_order[i]] = height
        continue
    
    taller = 0
    
    for j in range(N):
        if taller == student_order[i] and ans[j] == 0:
            ans[j] = height
            break
        
        if ans[j] > height or ans[j] == 0:
            taller += 1
            continue

print(*ans)
        
        
                                                                                                                                        